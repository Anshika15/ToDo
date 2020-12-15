from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

todos = []

@app.route("/")
def tasks():
    if "todos" not in session:
        session["todos"] = []
    return render_template("tasks.html", todos=session["todos"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task").strip()
        if len(todo) >= 1:
            session["todos"].append(todo)
            return redirect("/")
        else:
            return redirect("/")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        return render_template("delete.html")
    else:
        todelete = request.form.get("todel").strip()
        if len(todelete) >= 1:
            if todelete in session["todos"]:
                session["todos"].remove(todelete)
                return redirect("/")
            else:
                return redirect("/")
        else:
            return redirect("/")

@app.route("/deleteAll")
def deleteAll():
    session["todos"].clear();
    return redirect("/")