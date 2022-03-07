from flask import Flask, render_template, request, redirect, url_for, session, flash
import random # needed for random number generation

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myverysecretkey' #used so session cookies can be encryptec

def check_for_winner(player):

    #initialise result
    result = False
    #check rows
    for i in range(3):

            result = True
    #check columns
    if result == False:
        for i in range(3):

                result = True
    #check diagonals
    if result == False:

            result = True
        else:

                result = True
    # return result
    return result

@app.route("/")
def home():
    # check if get variables exist
    if request.args.get('r') and request.args.get('c'):
        # retrieve the get variables
        r = int(request.args.get('r'))
        c = int(request.args.get('c'))

        # adjust the game board for user choice
        session['board'][r][c] = 'x'

        # check if won
        r = check_for_winner('x')

        # if won ...
        if r is True:
            flash('Congratulations you won!')
            session['gameon'] = False

        # else do computer turn
        else:
            # generate random number for cc and cr

            # check if cc and cr is a valid option


            # update game board


            # check if computer has one

            if r is True:
                flash('You lost!')
                session['gameon'] = False

    # otherwise start new game
    else:
        # delete any existing board in the session
        session.pop('board')
        # initialise game board

        # set gameon to be true
        session['gameon'] = True
        # message user to confirm new game
        flash('New game started!')
    # update game board
    session['board'] = session['board']


    return render_template('Paper Scissors Rock Lizard Spock.html', board=session['board'], gameon=session['gameon'])

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    app.run(host, port, debug=True)