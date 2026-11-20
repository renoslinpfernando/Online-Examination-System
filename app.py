from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = "replace-this-demo-secret-key"

# Demo data is stored in Python memory. It resets whenever the server restarts.
USERS = {
    "student": {"password": "student123", "role": "student", "name": "Demo Student"},
    "admin": {"password": "admin123", "role": "admin", "name": "Administrator"},
}
QUESTIONS = [
    {"id": 1, "question": "Which language is primarily used with Flask?", "options": ["Java", "Python", "C++", "PHP"], "answer": 1},
    {"id": 2, "question": "Which HTML tag creates a hyperlink?", "options": ["<link>", "<a>", "<href>", "<url>"], "answer": 1},
    {"id": 3, "question": "What does CSS stand for?", "options": ["Computer Style Sheets", "Creative Style System", "Cascading Style Sheets", "Colorful Style Sheets"], "answer": 2},
    {"id": 4, "question": "Which data type stores True or False in Python?", "options": ["int", "str", "list", "bool"], "answer": 3},
    {"id": 5, "question": "Which method starts a Flask development server?", "options": ["app.run()", "app.start()", "flask.begin()", "server.open()"], "answer": 0},
]
RESULTS = []

def login_required(role=None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if "username" not in session:
                return redirect(url_for("login"))
            if role and session.get("role") != role:
                flash("You do not have permission to view that page.", "error")
                return redirect(url_for("dashboard"))
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        user = USERS.get(username)
        if user and secrets.compare_digest(user["password"], password):
            session.clear()
            session.update(username=username, role=user["role"], name=user["name"])
            return redirect(url_for("dashboard"))
        flash("Invalid username or password. Please try again.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required()
def dashboard():
    if session["role"] == "admin":
        return render_template("admin_dashboard.html", questions=QUESTIONS, results=RESULTS)
    my_results = [r for r in RESULTS if r["username"] == session["username"]]
    return render_template("student_dashboard.html", questions=QUESTIONS, results=my_results)

@app.route("/exam")
@login_required("student")
def exam():
    # Only expose question text/options to the browser, never the correct answers.
    public_questions = [{"id": q["id"], "question": q["question"], "options": q["options"]} for q in QUESTIONS]
    if not public_questions:
        flash("No questions are available yet.", "error")
        return redirect(url_for("dashboard"))
    session["exam_started"] = datetime.utcnow().timestamp()
    return render_template("exam.html", questions=public_questions, duration=10)

@app.route("/submit_exam", methods=["POST"])
@login_required("student")
def submit_exam():
    if not session.get("exam_started"):
        flash("Please start the examination before submitting.", "error")
        return redirect(url_for("dashboard"))
    answers = request.form
    score = 0
    for q in QUESTIONS:
        selected = answers.get(f"q{q['id']}")
        if selected is not None and selected.isdigit() and int(selected) == q["answer"]:
            score += 1
    total = len(QUESTIONS)
    result = {
        "username": session["username"],
        "name": session.get("name", session["username"]),
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100, 1) if total else 0,
        "submitted_at": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    }
    RESULTS.append(result)
    session.pop("exam_started", None)
    return render_template("result.html", result=result)

@app.route("/admin/add-question", methods=["POST"])
@login_required("admin")
def add_question():
    question = request.form.get("question", "").strip()
    options = [request.form.get(f"option{i}", "").strip() for i in range(4)]
    correct = request.form.get("correct", "")
    if not question or any(not option for option in options) or not correct.isdigit() or int(correct) not in range(4):
        flash("Please complete the question, all four options, and the correct answer.", "error")
    else:
        QUESTIONS.append({"id": max([q["id"] for q in QUESTIONS], default=0) + 1,
                          "question": question, "options": options, "answer": int(correct)})
        flash("Question added successfully.", "success")
    return redirect(url_for("dashboard"))

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
