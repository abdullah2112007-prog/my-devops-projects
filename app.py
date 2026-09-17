from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Welcome Abdullah!</h1>
    <h2>Cloud & DevOps Learning</h2>
    <p>Days Completed: 45</p>
    """

app.run(host="0.0.0.0", port=5000)