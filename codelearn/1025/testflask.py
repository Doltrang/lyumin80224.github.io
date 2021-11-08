from flask import Flask,request,render_template
import flask
app = Flask(__name__)
##############################################
chart_data = [
    {
    'country': "USA",
    'visits': 23725
    },
    {
    'country': "China",
    'visits': 1882
    },
    {
    'country': "Japan",
    'visits': 1809
    },
    {
    'country': "Germany",
    'visits': 1322
    },
    {
    'country': "UK",
    'visits': 1122
    },
    {
    'country': "France",
    'visits': 1114
    },
    {
    'country': "India",
    'visits': 984
    },
    {
    'country': "Spain",
    'visits': 711
    },
    {
    'country': "Netherlands",
    'visits': 665
    },
    {
    'country': "Russia",
    'visits': 580
    },
    {
    'country': "South Korea",
    'visits': 443
    },
    {
    'country': "Canada",
    'visits': 441
    }
]
##############################################
@app.route("/")     # "/"指定網站路徑
def hello_world():  # 自定義一個要對應路徑的def
     return render_template('input.html') # 提供一個return來回應網址要求(request)

@app.route("/data")
def data():
    m = request.args.get('m')
    n = request.args.get('n')
    return "<p>有一些資料{}&{}</p>".format(m,n)

from flask import jsonify
import pandas as pd
@app.route("/data2")
def data2():
    df=pd.DataFrame.from_dict(chart_data)
    m = request.args.get('m')
    n = request.args.get('n')
    if m != 'None' or n !='None':
        df=df[(df.visits > int(n)) & (df.visits < int(m))]
    return jsonify(df.to_dict('records'))

@app.route("/charts")
def charts():
    m = request.args.get('m')
    n = request.args.get('n')
    data=[m,n]
    return render_template('charts.html',data=data)
    #Charts.html必須放在templates資料夾下
##############################################
app.run() #wbbsite,RESTful API