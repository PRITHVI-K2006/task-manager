from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return "Task Manager v3 - Add, Update and View Tasks"

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

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = data["status"]
            return jsonify({"message": "Status updated", "task": task})
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks", methods=["GET"])
def view_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)