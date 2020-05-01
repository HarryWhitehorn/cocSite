#cocSite - main
import data
import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html",clans=data)

data = data.ClanGen.generateRandom(100)

if __name__ == '__main__':
    app.run()