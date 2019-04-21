import evaluate as model
import tweets as tweets
from flask import Flask, render_template, jsonify
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
   return render_template('./index.html')


@app.route('/get/<symbol>')
def hello_world(symbol):
   # print(symbol)
   # symbol='NIFTY'
   t = tweets.tweet(symbol)
   return jsonify(t)

@app.route('/trade/<symbol>')
def trade(symbol):
   print('######'+symbol+'#####')
   res = model.trade(symbol)
   return res



if __name__ == '__main__':
   app.run(debug=True)

