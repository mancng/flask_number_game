from flask import Flask, render_template, redirect, request, session, flash
import random
import re

NUM_REGEX = re.compile(r'^[-+]?[0-9]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    # del session['random']
    if not 'random' in session:
        session['random'] = random.randrange(0, 3)
        session['guess'] = False
        print "New random is:", session['random']
    else:
        print "Existing random is: ", session['random']
    return render_template('index.html')

@app.route('/guessing', methods=['POST'])
def process():
    guess = request.form['get_num']
    if int(guess) > int(session['random']):
        flash("Too high", "red")
    elif int(guess) < int(session['random']):
        flash("Too small", "red")
    elif int(guess) == int(session['random']):
        session['guess'] = True
        print "You've got it!"
        flash("{} was the number!".format(session['random']), "green")
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    del session['random']
    return redirect('/')


app.run(debug=True)