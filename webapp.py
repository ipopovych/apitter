from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, StringField, validators
from decipher import friendslist, userdict
from getfriends import request_friends
from mapmaker import geoloc, createmap
import json


# App configuration
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'secretkey'


class ReusableForm(Form):
    name = StringField('Twitter account:', validators=[validators.InputRequired(message='enter name'), validators.Length(min=1, message=None)])


@app.route("/", methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        print("Account entered: ", name)

        if form.validate():
           # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
        return redirect("/map/"+name)
    return render_template('hello.html', form=form)


@app.route('/map/<name>')
def usermap(name="ippvch"):
    js = request_friends(name)
    if not js:
        print("error getting info from API")
        return redirect("/wearesoorry")

    data = json.load(open(js, encoding='utf-8'))
    friends = friendslist(data)
    locationdict = userdict(data, param="location")
    geodict = {loc: geoloc(loc) for loc in locationdict.values()}
    map_data = [(f[1], geodict[locationdict[f[2]]]) for f in friends]
    print('Map data collected')
    createmap(map_data)
    return render_template('friendsmap.html')


@app.route("/wearesorry")
def tryagain():
    return("Try again later.")


@app.route("/map/")
def badinput():
    return("Sorry. Please go back and enter the name")


if __name__ == "__main__":
    app.run(debug=True)
