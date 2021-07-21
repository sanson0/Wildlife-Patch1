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
    survey_links = list(mongo.db.survey_links.find())
    return render_template("surveys.html", survey_links=survey_links)


# add link to wildlife surveys page
@app.route("/add_link", methods=["GET", "POST"])
def add_link():
    if request.method == "POST":
        survey = {
            "survey_title": request.form.get("survey_title"),
            "survey_link": request.form.get("survey_link"),
        }
        mongo.db.survey_links.insert_one(survey)
        flash("Link Successfully Added")       
    return render_template("add_link.html")


# edit link to wildlife surveys page
@app.route("/edit_link/<survey_id>", methods=["GET", "POST"])
def edit_link(survey_id):
    if request.method == "POST":
        submit = {
           "survey_title": request.form.get("survey_title"),
           "survey_link": request.form.get("survey_link"),
        }
        mongo.db.survey_links.update({"_id": ObjectId(survey_id)}, submit)
        flash("Link Successfully Updated")

    survey = mongo.db.survey_links.find_one({"_id": ObjectId(survey_id)})
    return render_template("edit_link.html", survey=survey)


# delete link in the wildlife surveys page
@app.route("/delete_link/<survey_id>")
def delete_link(survey_id):
    mongo.db.survey_links.remove({"_id": ObjectId(survey_id)})
    flash("Link Successfully Deleted")
    return redirect(url_for("surveys"))


# load people's projects page, contributions from other users
@app.route("/get_peoplesprojects")
def get_peoplesprojects():
    tasks = list(mongo.db.tasks.find())
    return render_template(
        "peoplesprojects.html", tasks=tasks)


# search function for home page projects
@app.route("/search_pps", methods=["GET", "POST"])
def search_pps():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("peoplesprojects.html", tasks=tasks)


# Create an account
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


# login to account
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


# load profile page and display own projects only
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    tasks = list(mongo.db.tasks.find())
    if session["user"]:

        return render_template(
            "profile.html", username=username, tasks=tasks)

    return redirect(url_for("login"))


# logout of account
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add own project to people's project page
@app.route("/addownproject", methods=["GET", "POST"])
def addownproject():
    if request.method == "POST":
        on_homepage = "on" if request.form.get("on_homepage") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "estimated_cost": request.form.get("estimated_cost"),
            "estimated_time": request.form.get("estimated_time"),
            "image_url": request.form.get("image_url"),
            "image_description": request.form.get("image_description"),
            "created_by": session["user"],
            "on_homepage": on_homepage
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")        
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("addownproject.html", categories=categories)


@app.route("/contact_users")
def contact_users():
    users = list(mongo.db.users.find())
    return render_template("contact_users.html", users=users)


# load categories page (if admin)
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add category (if admin)
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


# edit a project (if admin)
@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        on_homepage = "on" if request.form.get("on_homepage") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "estimated_cost": request.form.get("estimated_cost"),
            "estimated_time": request.form.get("estimated_time"),
            "image_url": request.form.get("image_url"),
            "image_description": request.form.get("image_description"),
            "created_by": session["user"],
            "on_homepage": on_homepage
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


# edit categories (if admin)
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


# delete project (if admin)
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


# delete project (if admin/user)
@app.route("/delete_task_pps/<task_id>")
def delete_task_pps(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_peoplesprojects"))


# delete category (if admin)
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)