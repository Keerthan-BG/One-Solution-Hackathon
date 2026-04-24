# 🔐 Moving Target Defense (MTD) Web Security System

## 📌 Project Overview
This project implements a **Moving Target Defense (MTD)** approach for web applications, where the system dynamically changes the **port number at runtime** to reduce the risk of cyber attacks such as port scanning, exploitation, and targeted intrusion.

Instead of using a fixed server configuration, the application continuously shifts its attack surface, making it difficult for attackers to locate or maintain a stable connection.

---

## 🚀 Key Idea
Traditional systems use fixed ports (like 80, 443), which are easy to scan and attack.

In this system:
- The **server port changes dynamically**
- The client is always redirected to the updated port
- Attackers cannot reliably track the system location

---

## ⚙️ How It Works
1. Server starts on an initial port
2. After a fixed interval or trigger:
   - A new random port is generated
   - Server migrates to the new port
3. Client is automatically informed of the updated port
4. Old connections become invalid

---

## 🧠 Core Concept
- Dynamic Attack Surface
- Port Randomization
- Secure Session Redirection
- Continuous Adaptation (Defense Mechanism)

---

## 💡 Problem Solved
- Prevents port scanning attacks
- Reduces risk of brute-force targeting
- Avoids static endpoint exploitation
- Improves system unpredictability

---

## 🛠️ Technologies Used
- Python / Node.js (based on your implementation)
- Flask / Express (if used)
- HTML, CSS, JavaScript
- Socket / HTTP communication

---

## 📂 Project Structure
Moving Target Defense/
│
├── server.py / app.js
├── client/
├── static/
├── templates/
└── README.md


---

## 🔄 Future Improvements
- Secure encrypted port transition
- AI-based adaptive port shifting
- Multi-node distributed defense system
- Integration with intrusion detection system (IDS)

---

## 👨‍💻 Author
Keerthan BG  
Hackathon Project – Moving Target Defense

---

## 📌 Conclusion
This project demonstrates how **dynamic system behavior** can significantly improve cybersecurity by making traditional attack methods ineffective.

---
