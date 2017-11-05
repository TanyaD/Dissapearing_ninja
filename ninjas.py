from flask import Flask, request, redirect, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def display_all():
    return render_template('tmnt.html')

@app.route('/ninja/<color>')
def color(color):
    if color=="blue":
        color="donatello"
        return render_template("ninjas.html", color=color)

    if color=="red":
        color="raphael"
        return render_template("ninjas.html", color=color)

    if color=="purple":
        color="donatello"
        return render_template("ninjas.html", color=color)

    if color=="orange":
        color="michelangelo"
        return render_template("ninjas.html", color=color)

    else:
        color="notapril"
        return render_template("ninjas.html", color=color)





app.run(debug=True)

