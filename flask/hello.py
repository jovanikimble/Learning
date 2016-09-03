
from flask import render_template, request
import os
import highlow
from flask import Flask

app = Flask(__name__,static_url_path="")
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/highlow')
def highlow2():
    return render_template("highlow.html")

@app.route('/handle_highlow')
def handle_highlow():
  num = highlow.generator()
  guess = int(request.args.get('guess'))
  s = ' Guess: {0} Actual: {1}'.format(guess, num)
  if guess > num:
    return "Guess was too high" + s
  elif guess < num:
    return "Guess was too low" + s
  else:
    return "Guess was just right" + s

if __name__ == '__main__':
    app.run()

