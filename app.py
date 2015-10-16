#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)
guesses = ['Python','Java','C++']
questions = ['Is it compiled?','Does it run on a VM?']

@app.route('/')
def index():
##    return '<h1>Guess the Language!</h1>'
    return render_template('index.html')

@app.route('/question/<int:id>')
def question(id):
    return render_template('question.html', question=questions[id])
    

@app.route('/guess/<int:id>')
def guess(id):
##    return('<h1>Guess The Language!</h1>'
##           '<p>My guess: {0}</p>').format(guesses[id])
    return render_template('guess.html', guess=guesses[id])

if __name__ == '__main__':
    app.run(debug=True)
##    app.run(host='0.0.0.0')
##    app.run(host='0.0.0.0', port=5000, debug=True)
