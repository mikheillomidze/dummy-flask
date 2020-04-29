import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"message": "Hello world", "server": request.environ['SERVER_NAME']}


@app.route("/load")
def load_server():
    proc = int(request.args.get("proc", 1))
    loop_length = request.args.get("loop-length", "1000")
    for _ in range(proc):
        subprocess.Popen(["python3", "dummy_worker.py", loop_length])
    return {"proc": proc, "loop_length": loop_length}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
