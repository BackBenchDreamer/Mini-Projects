from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask app
app = Flask(__name__)

# Get the current working directory (the folder where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the SQLite database file within the same folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(current_dir, "test.db")

# Turn off modification tracking to save resources
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)


# Create a model for the Todo table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique task ID
    content = db.Column(db.String(200), nullable=False)  # Task description
    completed = db.Column(db.Integer, default=0)  # Completion status (0 = not completed)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Timestamp for task creation

    def __repr__(self):
        return "<Task %r>" % self.id


# Create the database tables if they do not exist
with app.app_context():
    db.create_all()  # This ensures the table is created before any queries are made


# Route to the homepage, handles both GET and POST requests
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["task"]
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your task."
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("index.html", tasks=tasks)


# Route to delete a task by ID
@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting the task."


# Route to update a task by ID
@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["task"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task."
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("index.html", update_task=task, tasks=tasks)


# Run the Flask app only if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
