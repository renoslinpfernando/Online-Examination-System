# Online Examination System

A beginner-friendly demonstration web application built with **Python Flask, HTML, CSS and JavaScript**. It uses sample data stored in Python memory; no database setup is required.

## 1. Requirements
- Windows 10/11, macOS or Linux
- Python 3.9 or newer
- VS Code (recommended)

## 2. Extract and open
1. Download `Online_Examination_System.zip`.
2. Extract the ZIP file.
3. Open the extracted `online_examination_system` folder in VS Code.
4. Open **Terminal → New Terminal**.

## 3. Install and run

### Windows PowerShell
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, use Command Prompt:
```bat
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

5. Open this address in your browser: **http://127.0.0.1:5000**

Stop the server with `Ctrl + C` in the terminal.

## 4. Demo login accounts

| Role | Username | Password |
|---|---|---|
| Student | `student` | `student123` |
| Admin | `admin` | `admin123` |

## 5. How to test
1. Sign in as the student.
2. Select **Start Examination**.
3. Answer the multiple-choice questions.
4. Submit before the 10-minute timer ends. The page also submits automatically when the timer reaches zero.
5. View your score and percentage.
6. Sign out and sign in as admin to add questions and view demo results.

## 6. Main modules
- Authentication: demo student/admin login and logout.
- Student dashboard: examination access and previous results.
- Examination: MCQ display, countdown timer and submission.
- Evaluation: automatic comparison with answer keys and score calculation.
- Admin dashboard: add questions and view submitted results.

## 7. Important limitations
- This is an **educational demo**, not a production examination platform.
- Data is held in memory. Added questions and results disappear when the Flask server restarts.
- Demo passwords and the Flask secret key are for local learning only. A real deployment needs secure password hashing, a strong secret key, persistent database storage, CSRF protection, HTTPS, server-side time enforcement and audit logs.
- The timer is implemented in the browser for demonstration. Production systems must enforce exam deadlines on the server.

## 8. Project structure
```text
online_examination_system/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── student_dashboard.html
│   ├── admin_dashboard.html
│   ├── exam.html
│   ├── result.html
│   └── 404.html
├── static/
│   ├── css/style.css
│   └── js/timer.js
└── diagrams/
    ├── use_case.puml
    ├── class_diagram.puml
    ├── activity_diagram.puml
    ├── sequence_diagram.puml
    └── deployment_diagram.puml
```

## 9. Assignment explanation
**Objective:** To develop a web-based system that allows students to attend objective examinations online and receive automatically calculated results.

**Expected outcome:** The system reduces manual evaluation work, provides a simple examination interface, and allows an administrator to maintain the question set.

**Future enhancement:** Add a database, student registration, password hashing, randomized questions, negative marking, downloadable reports, and server-side exam time validation.
