from flask import Flask,render_template,request,jsonify
import pandas as pd
app = Flask(__name__)
###############
c= [
  {
    "country": "USA",
    "visits": 23725
  },
  {
    "country": "China",
    "visits": 1882
  },
  {
    "country": "Japan",
    "visits": 1809
  },
  {
    "country": "Germany",
    "visits": 1322
  },
  {
    "country": "UK",
    "visits": 1122
  },
  {
    "country": "France",
    "visits": 1114
  },
  {
    "country": "India",
    "visits": 984
  },
  {
    "country": "Spain",
    "visits": 711
  },
  {
    "country": "Netherlands",
    "visits": 665
  },
  {
    "country": "Russia",
    "visits": 580
  },
  {
    "country": "South Korea",
    "visits": 443
  },
  {
    "country": "Canada",
    "visits": 441
  }
]
################################
@app.route("/")     # "/"指定網站路徑
def index():  # 自定義一個要對應路徑的def
    mx = request.args.get('mx')
    mn = request.args.get('mn')
    return render_template('chart4.html',args = [mx,mn])

@app.route("/chart")
def chart3():
    mx = request.args.get('mx')
    mn = request.args.get('mn')
    return render_template('chart3.html',args = [mx,mn])
    #確認Chart3.html必須在templates底下
    #確認js資料夾挪至static底下，並更改html中的js路徑為static/js

#/data?mx=30000&mn=1000
@app.route("/data")
def data():
    df = pd.DataFrame(c)
    mx = request.args.get('mx')
    mn = request.args.get('mn')
    if mx != None and mn != None and mx != 'None' and mn != 'None':
        df = df[(df.visits >= int(mn))&(df.visits <= int(mx))]
    return jsonify(df.to_dict(orient='records'))

@app.route("/chart4")
def chart4():
    mx = request.args.get('mx')
    mn = request.args.get('mn')
    return render_template('chart4.html',args = [mx,mn])
###############
app.run(debug=True)