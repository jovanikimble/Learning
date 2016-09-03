
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
	return "%d" % highlow.apple(int(request.args.get('guess')))

if __name__ == '__main__':
    app.run()

