from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime, date
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, SelectField, widgets
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, InputRequired
import random


class MultiCheckboxField(SelectMultipleField):
    # a custom object to use in SubmitVideo form,
    # need to import widgets from wtforms above
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SubmitVideo(FlaskForm):
    url = StringField('URL', validators=[DataRequired(message="You must submit a URL"), URL(message="Not a valid URL")])
    description = TextAreaField('Description', validators=[DataRequired()])
    topics = MultiCheckboxField('Topics for this video', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit URL')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddksididkdkdl'

#connect to database
con = sqlite3.connect("video.db", check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

### Form models ####
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


########## routes ##########
@app.route('/')
@app.route('/index')
def index():
    if 'username' not in session:
        session['username'] = None

        if session['username']:
            sql = """
                      select v.video_id, url, description, subject_name, topic_description
                        from videos v, video_topics vt, subjects s, topics t
                        where s.subject_code = t.subject_id
                        and t.topic_id = vt.topic_id
                        and vt.video_id = v.video_id
                        and v.video_id in (
                            select video_id
                            from video_topics
                            where topic_id in (
                                select topic_id
                                from topics
                                where subject_id in (
                                    select subject_code
                                    from users u, enrolments e, classes c
                                    where u.username = e.student_id
                                    and c.classid = e.class_id
                                    and username = ?)))
                        order by subject_id asc, vt.topic_id asc, date_added desc"""

            cur.execute(sql, (session['username'],))
            results = cur.fetchall()

            for row in results:
                print(row['video_id'], row['url'], row['description'])

        return render_template('index.html', my_results=results)

    else:
        sql = """
                     select v.video_id, url, description,subject_name, topic_description
                     from videos v, video_topics vt, subjects s, topics t
                     where s.subject_code = t.subject_id
                     and t.topic_id = vt.topic_id
                     and vt.video_id = v.video_id
                     order by date_added desc
                     limit 6;"""
        cur.execute(sql)
        results = cur.fetchall()

        for row in results:
            print(row['video_id'], row['url'], row['description'])

        return render_template('index.html', results=results)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            un = form.username.data
            pw = form.password.data
            sql = """
                    select * 
                    from users
                    where username = ?
                    and password = ?;"""

            cur.execute(sql, (un, pw))
            result = cur.fetchall()

            if len(result) == 1:
                session['username'] = result[0][0]
                session['firstname'] = result[0][1]
                session['lastname'] = result[0][2]
                session['is_teacher'] = result[0][3]
                if session['is_teacher']:
                    session['teacher_code'] = result[0][4]
                return redirect(url_for('index'))
            else:
                flash("Username or password incorrect, try again")
        else:
            flash("There is something missing!")
    return render_template('login.html', title='Login', form=form)

# @app.route('/submit_video', methods=['POST'])
# def login():
#     form = LoginForm()
#     if session['username']:
#         form = SubmitVideo()
#     # get the subject & topic combinations to choose from
#     my_topics = []
#
#     sql = """
#             select topic_id, topic_description, s.subject_code
#             from topics t, subjects s, enrolments e, users u, classes c where t.subject_id = s.subject_code
#             and s.subject_code = c.subject_code
#             and c.classid = e.class_id
#             and e.student_id = u.username
#             and u.username = ?
#             order by s.subject_code asc, topic_id asc;"""
#
#     cur.execute(sql, (session['username'], ))
#     results = cur.fetchall()
#     for row in results:
#         my_topics.append((row['topic_id'], row['subject_code']+' - '+row['topic_description']))
#     form.topics.choices = my_topics
#
#     # deal with the post data
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             print('I got the data!')
#             for k, v in form.data.items():
#                 print(k, v)
#
#         #now deal with the data
#         video_url = form.url.data
#         video_description = form.description.data
#         video_topics = []
#         for v in form.topics.data:
#             video_topics.append(int(v)) #though not necessary -> see the form
#
#         sql_video = """
#                         insert
#                         into videos(url, description, submitter)
#                         values(?, ?, ?);"""
#
#         cur.execute(sql_video, (video_url, video_description, session['username']))
#         con.commit()
#
#         #now get the video_id for the just submitted video
#         video_videoID = cur.lastrowid
#         print(video_videoID)
#
#         #now we know the id of the video, we can add the topics
#         sql_topics = """
#             insert
#             into video_topics(video_id, topic_id)
#             values (?, ?);"""
#
#
#         for topic in video_topics:
#             cur.execute(sql_topics, (video_videoID, topic))
#
#         con.commit()
#
#     return render_template('submit_video')

@app.route('/logout')
def logout():
    if session['username']:
    # clear out the session
        session['username'] = None
        session['firstname'] = None
        session['lastname'] = None
        session['is_teacher'] = None
        session['teacher_code'] = None
        flash("You have successfully logged out")

    return redirect(url_for('index'))

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)

