from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("template.html")



if __name__ == "__main__":
    app.run("127.0.0.1", debug= True)