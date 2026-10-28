from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return "Task Manager v1 - Add Task"

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": "Pending"
    }
    tasks.append(task)
    return jsonify({"message": "Task created", "task": task}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)