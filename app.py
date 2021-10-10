import os
import datetime
from flask import send_from_directory, request, Flask, render_template
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qrs.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class qrs(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    qry = db.Column(db.String(256))
    qrytime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, qry):
        self.qry = qry

db.create_all()

@app.route('/stats')
def stats():
    vals = qrs.query.all()
    # print("Stats are: ")
    # print(vals)
    return render_template("stats.html", values = qrs.query.all())


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Go to stats!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    # print(req['queryResult']['queryText'])
    # pprint(req['queryResult'])
    # print(type(req))

    qryTxt = req['queryResult']['queryText']

    # print("Query: ", qryTxt)

    qry = qrs(qryTxt)
    db.session.add(qry)
    db.session.commit()

    ft = "Sorry, didn't get you!"

    if('fulfillmentText' in req['queryResult'].keys()):
        ft = req['queryResult']['fulfillmentText']

    return {
        'fulfillmentText': ft
    }

if __name__ == "__main__":
    app.debug = False
    app.run()