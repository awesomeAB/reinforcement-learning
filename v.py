# import evaluate as model
import tweets as tweets
# model.trade('^GSPC_2011')
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def index():
   return render_template('./index.html')


@app.route('/hello')
def hello_world():
   t = tweets.tweet('crypto')
   return t[0]

if __name__ == '__main__':
   app.run(debug=True)

