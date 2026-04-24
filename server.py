import socket
import threading
import time
import random
import requests

HOST = '127.0.0.1'
PORT = random.randint(5000, 6000)
FAILED_ATTEMPTS = 0
LAST_PORT = None

lock = threading.Lock()


def update_port_api(port):
    try:
        requests.post(f"http://127.0.0.1:8000/update-port/{port}")
    except:
        pass


def send_attack_log():
    try:
        requests.post("http://127.0.0.1:8000/attack")
    except:
        pass


def send_defense_log():
    try:
        requests.post("http://127.0.0.1:8000/defense")
    except:
        pass


def shift_port_periodically():
    global PORT
    while True:
        time.sleep(20)
        with lock:
            PORT = random.randint(5000, 6000)
            update_port_api(PORT)
            print(f"\n[INFO] 🔄 Periodic port shift → {PORT}")


def start_server():
    global PORT, FAILED_ATTEMPTS, LAST_PORT

    while True:
        with lock:
            current_port = PORT

        if LAST_PORT != current_port:
            print(f"\n[STARTED] 🚀 Server running on port {current_port}")
            LAST_PORT = current_port

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            server.bind((HOST, current_port))
        except:
            time.sleep(1)
            continue

        server.listen(5)
        server.settimeout(1)

        try:
            conn, addr = server.accept()
            print(f"[CONNECTED] 🔗 {addr}")

            data = conn.recv(1024).decode()

            if data == "HELLO_SERVER":
                conn.send("WELCOME_CLIENT".encode())
                print("[OK] ✅ Legit client connected")

            else:
                FAILED_ATTEMPTS += 1
                print(f"[ALERT] ⚠️ Suspicious activity ({FAILED_ATTEMPTS})")
                send_attack_log()

            conn.close()

            # 🔥 LOWERED threshold for demo
            if FAILED_ATTEMPTS >= 1:
                with lock:
                    print("[DEFENSE] 🛡️ Attack detected! Immediate port shift!")
                    PORT = random.randint(5000, 6000)
                    update_port_api(PORT)
                    FAILED_ATTEMPTS = 0
                    send_defense_log()

        except socket.timeout:
            pass

        finally:
            server.close()


if __name__ == "__main__":
    update_port_api(PORT)
    threading.Thread(target=shift_port_periodically, daemon=True).start()
    start_server()