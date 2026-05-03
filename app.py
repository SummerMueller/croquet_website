import flask as fk

app = fk.Flask(__name__)

todos = []

@app.route("/")
def home():
   return fk.render_template("index.html")

@app.route("/api/todos", methods=["POST"])
def add_todos():
   new_todo = fk.request.json
   todos.append(new_todo["task"])
   return {"status": "okay"}

@app.route("/api/todos", methods=["GET"])
def get_todos():
   return fk.jsonify(todos)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=10000)
