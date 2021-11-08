from flask import Flask,render_template

app = Flask(__name__)
##############################################

##############################################
@app.route("/")     # "/"指定網站路徑
def index():  # 自定義一個要對應路徑的def
     return render_template('info1.html')

@app.route("/info1")     # "/"指定網站路徑
def info1():  # 自定義一個要對應路徑的def
     return render_template('info1.html')

@app.route("/info2")     # "/"指定網站路徑
def info2():  # 自定義一個要對應路徑的def
     return render_template('info2.html')

@app.route("/charts")     # "/"指定網站路徑
def charts():  # 自定義一個要對應路徑的def
     return render_template('charts.html')
##############################################
app.run() #wbbsite,RESTful API