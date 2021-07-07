import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")

# load home page
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


# search function for home page projects
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


# load wildlife surveys page
@app.route("/surveys")
def surveys():
    return render_template("surveys.html")

# load people's projects page, contributions from other users
@app.route("/get_peoplesprojects")
def get_peoplesprojects():
    peoplesprojects = list(mongo.db.peoplesprojects.find())
    return render_template(
        "peoplesprojects.html", peoplesprojects=peoplesprojects)


# search function for people's projects
@app.route("/search_pps", methods=["GET", "POST"])
def search_pps():
    query = request.form.get("query")
    peoplesprojects = list(
        mongo.db.peoplesprojects.find({"$text": {"$search": query}}))
    return render_template(
        "peoplesprojects.html", peoplesprojects=peoplesprojects)


# 
@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    if request.method == "POST":
        # check if name already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("createaccount"))

        createaccount = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(createaccount)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Account sucessfully created")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("createaccount.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    peoplesprojects = list(mongo.db.peoplesprojects.find())
    if session["user"]:

        return render_template(
            "profile.html", username=username, peoplesprojects=peoplesprojects)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/addownproject", methods=["GET", "POST"])
def addownproject():
    if request.method == "POST":
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "estimated_cost": request.form.get("estimated_cost"),
            "estimated_time": request.form.get("estimated_time"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.peoplesprojects.insert_one(task)
        flash("Task Successfully Added")
        
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("addownproject.html", categories=categories)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "estimated_cost": request.form.get("estimated_cost"),
            "estimated_time": request.form.get("estimated_time"),
            "due_date": request.form.get("due_date"),
            "image_url": request.form.get("image_url"),
            "image_description": request.form.get("image_description"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/edit_task_pps/<peoplesproject_id>", methods=["GET", "POST"])
def edit_task_pps(peoplesproject_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "estimated_cost": request.form.get("estimated_cost"),
            "estimated_time": request.form.get("estimated_time"),
            "due_date": request.form.get("due_date"),
            "image_url": request.form.get("image_url"),
            "image_description": request.form.get("image_description"),
            "created_by": session["user"]
        }
        mongo.db.peoplesprojects.update(
            {"_id": ObjectId(peoplesproject_id)}, submit)
        flash("Task Successfully Updated")

    peoplesproject = mongo.db.peoplesprojects.find_one(
        {"_id": ObjectId(peoplesproject_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_task_pps.html", peoplesproject=peoplesproject, categories=categories)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)



@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/delete_project/<peoplesproject_id>")
def delete_project(peoplesproject_id):
    mongo.db.peoplesprojects.remove({"_id": ObjectId(peoplesproject_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_peoplesprojects"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)