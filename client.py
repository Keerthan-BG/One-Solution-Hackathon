import socket
import time
import requests

HOST = '127.0.0.1'


def get_port():
    try:
        res = requests.get("http://127.0.0.1:8000/get-port")
        return res.json()["port"]
    except:
        return None


last_port = None

while True:
    port = get_port()

    if port is None:
        print("[CLIENT] Waiting for API...")
        time.sleep(1)
        continue

    if port != last_port:
        print(f"\n[CLIENT] 📡 New port: {port}")
        last_port = port

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)

        print(f"[CLIENT] 🔄 Connecting to {port}...")
        client.connect((HOST, port))

        client.send("HELLO_SERVER".encode())
        response = client.recv(1024).decode()

        print(f"[CLIENT] ✅ Connected → {response}")

        client.close()
        time.sleep(3)

    except:
        time.sleep(1)