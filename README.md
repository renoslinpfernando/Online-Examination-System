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

---

## ✨ Key Features

### Student Module
- Student Login
- Student Dashboard
- View Available Examinations
- Attend Multiple Choice Questions (MCQs)
- Countdown Timer
- Automatic Examination Submission
- View Examination Results

### Admin Module
- Admin Login
- Admin Dashboard
- Add New Questions
- Manage Question Bank
- View Student Results

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| HTML | Web Page Structure |
| CSS | User Interface Design |
| JavaScript | Timer and Interactive Functions |

## 📂 Main Modules

1. **Authentication Module:** Provides student and administrator login.
2. **Student Module:** Allows students to attend online examinations.
3. **Examination Module:** Displays questions and manages the examination timer.
4. **Evaluation Module:** Automatically evaluates submitted answers.
5. **Result Module:** Displays examination scores and percentages.
6. **Admin Module:** Allows administrators to add questions and view results.

## 📊 UML Diagrams

The project includes the following UML diagrams in the `diagrams` folder:

- Use Case Diagram
- Class Diagram
- Activity Diagram
- Sequence Diagram
- Deployment Architecture Diagram

## 🚀 Future Enhancements

- Integration with MySQL database.
- Student registration functionality.
- Secure password encryption.
- Random question generation.
- Downloadable examination reports.
- Advanced examination monitoring.

## 🎯 Expected Outcome

The system provides an efficient online platform for conducting examinations. It reduces manual evaluation work, saves time, and generates examination results automatically.

## 📝 Conclusion

The Online Examination System simplifies the traditional examination process through automation. It provides separate functionalities for students and administrators and offers a user-friendly platform for conducting online examinations.

---

**Project Title:** Online Examination System

**Project Type:** Web-Based Application

**Developed Using:** Python Flask, HTML, CSS and JavaScript

**Data Storage:** In-memory Sample Data

