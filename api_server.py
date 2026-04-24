from flask import Flask, jsonify, render_template

app = Flask(__name__)

current_port = 5000
attack_count = 0
defense_count = 0
logs = []


def add_log(message):
    logs.append(message)
    if len(logs) > 50:
        logs.pop(0)


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/get-data")
def get_data():
    return jsonify({
        "port": current_port,
        "attacks": attack_count,
        "defenses": defense_count,
        "logs": logs
    })


@app.route("/get-port")
def get_port():
    return jsonify({"port": current_port})


@app.route("/update-port/<int:port>", methods=["POST"])
def update_port(port):
    global current_port
    current_port = port
    add_log(f"[INFO] Port updated → {port}")
    return jsonify({"status": "updated"})


@app.route("/attack", methods=["POST"])
def attack():
    global attack_count
    attack_count += 1
    add_log(f"[ATTACK] Attempt #{attack_count}")
    return jsonify({"status": "attack recorded"})


@app.route("/defense", methods=["POST"])
def defense():
    global defense_count
    defense_count += 1
    add_log(f"[DEFENSE] Triggered #{defense_count}")
    return jsonify({"status": "defense recorded"})


if __name__ == "__main__":
    app.run(port=8000, debug=True)