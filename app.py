import flask

app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.config["TOKEN"]="clock"
app.secret_key="bharath"

@app.route('/',methods=["GET","POST"])
def display_fun():
   return flask.render_template('index.html')


app.run(host="0.0.0.0")
