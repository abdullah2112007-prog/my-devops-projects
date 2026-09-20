from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎓 Student Management System</h1>
    <h2>Cloud & DevOps Project</h2>
    <p>Welcome to my project!</p>
    <p>Built using Python and Flask.</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About Project</h2>
    <p>This project combines Cloud Computing and DevOps skills.</p>
    <p>Days 1-45 completed.</p>
    """

@app.route("/students")
def students():
    return """
    <h2>Student List</h2>
    <ul>
        <li>Abdullah</li>
        <li>Student 2</li>
        <li>Student 3</li>
    </ul>
    """

app.run(host="0.0.0.0", port=5000)

