from flask import Flask, render_template, request, jsonify
import os
import yfinance as yf
import datetime as dt

app = Flask(__name__)

def process(symbol):
    stock = yf.Ticker(symbol)
    rslt = ""
    if stock.info['logo_url'] == '':
        rslt += "Output:"
        rslt += "Please enter a valid symbol"
        return rslt
    shortN = stock.info['shortName']
    regularMP = stock.info['regularMarketPrice']
    marketPC = stock.info['regularMarketPrice'] - stock.info['previousClose']
    marketPCP = marketPC / stock.info['previousClose'] * 100
    rslt += "Output:"
    current = dt.datetime.now()
    rslt += current.strftime("%a %b %d %H:%M:%S PDT %Y")
    rslt += f"{regularMP} {marketPC:.02f} ({marketPCP:.02f}%)"
    return rslt

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine

@app.route("/")
def index():
    return render_template('./home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
