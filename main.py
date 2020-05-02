#cocSite - main
import data
import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    clans = data.ClanGen.generateRandom(100)
    return flask.render_template("index.html",clans=clans)

@app.route("/img")
def img():
    return flask.render_template("img.html")

if __name__ == '__main__':
    app.run()