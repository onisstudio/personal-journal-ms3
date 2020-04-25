import os
from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'personal_journal'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect('entries/' + session["username"])

    return render_template("login.html")


@app.route('/entries/<username>')
def entries(username):
    return render_template("entries.html",
                           username=username,
                           entries=mongo.db.entries.find(
                               {'entry_user': username, 'entry_status': '1'}).sort("entry_created", -1),
                           entries_num=mongo.db.entries.count_documents(
                               {'entry_user': username, 'entry_status': '1'})
                           )


@app.route('/add_entry')
def add_entry():
    return render_template('addentry.html',
                           username=session["username"],
                           feelings=mongo.db.feelings.find())


@app.route('/insert_entry', methods=['POST'])
def insert_entry():
    entries = mongo.db.entries
    form_data = request.form.to_dict()
    form_data['entry_user'] = session["username"]
    form_data['entry_status'] = '1'
    form_data['entry_created'] = datetime.datetime.utcnow()
    entries.insert_one(form_data)
    return redirect("/")


@app.route('/edit_entry/<entry_id>')
def edit_entry(entry_id):
    the_entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    all_feelings = mongo.db.feelings.find()
    return render_template('editentry.html', entry=the_entry,
                           feelings=all_feelings)


@app.route('/update_entry/<entry_id>', methods=['POST'])
def update_entry(entry_id):
    entries = mongo.db.entries
    entries.update({'_id': ObjectId(entry_id)},
                   {
        '$set': {
            'entry_story': request.form.get('entry_story'),
            'feeling_name': request.form.get('feeling_name'),
            'entry_updated': datetime.datetime.utcnow()
        }
    })
    return redirect("/")


@app.route('/_archive_entry')
def archive_entry():
    entry_id = request.args.get('entry_id', 0)
    entries = mongo.db.entries
    entries.update_one({'_id': ObjectId(entry_id)},
                       {
        '$set': {'entry_status': '2'}
    })
    return jsonify(entry_id)


@app.route('/_unarchive_entry')
def unarchive_entry():
    entry_id = request.args.get('entry_id', 0)
    entries = mongo.db.entries
    entries.update_one({'_id': ObjectId(entry_id)},
                       {
        '$set': {'entry_status': '1'}
    })
    return jsonify(entry_id)


@app.route('/_delete_entry')
def delete_entry():
    entry_id = request.args.get('entry_id', 0)
    mongo.db.entries.remove({'_id': ObjectId(entry_id)})
    return jsonify(entry_id)


@app.route('/archive/<username>')
def archive(username):
    return render_template("entries.html",
                           username=username,
                           entries=mongo.db.entries.find(
                               {'entry_user': username, 'entry_status': '2'}).sort("entry_created", -1),
                           entries_num=mongo.db.entries.count_documents(
                               {'entry_user': username, 'entry_status': '2'})
                           )


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
