import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'personal_journal'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_entries')
def get_entries():
    return render_template("entries.html", entries=mongo.db.entries.find())

@app.route('/add_entry')
def add_entry():
    return render_template('addentry.html',
    feelings=mongo.db.feelings.find())

@app.route('/insert_entry', methods=['POST'])
def insert_entry():
    entries = mongo.db.entries
    form_data = request.form.to_dict()
    form_data['entry_created'] = datetime.datetime.utcnow()
    entries.insert_one(form_data)
    return redirect(url_for('get_entries'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
