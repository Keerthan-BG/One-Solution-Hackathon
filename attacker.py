import socket
import random
import time
import requests

HOST = '127.0.0.1'

while True:
    try:
        # 🔥 Smarter attacker (sometimes hits correct port)
        if random.random() < 0.3:
            try:
                port = requests.get("http://127.0.0.1:8000/get-port").json()["port"]
            except:
                port = random.randint(5000, 6000)
        else:
            port = random.randint(5000, 6000)

        attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        attacker.settimeout(1)

        attacker.connect((HOST, port))
        attacker.send("HACK".encode())

        print(f"[ATTACKER] 🚨 Tried port {port}")

        attacker.close()

    except:
        print(f"[ATTACKER] ❌ Failed on port {port}")

    # 📊 send attack log to UI
    try:
        requests.post("http://127.0.0.1:8000/attack")
    except:
        pass

    time.sleep(1)