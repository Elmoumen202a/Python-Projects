# ⛔ Website Blocker

## 📋 Project Overview
The **Website Blocker** is a simple Python program that helps you stay focused by blocking access to distracting websites during specific hours. It modifies your system's `hosts` file to redirect unwanted websites to `localhost`, making them inaccessible.

## 🛠️ How It Works
- The program reads a list of websites from a file (`websites.txt`).
- During specified hours, it blocks these websites by redirecting them to `127.0.0.1` (localhost).
- Outside of these hours, the websites are unblocked and fully accessible again.

## 📁 Files
- `main.py`: The core Python script that handles blocking and unblocking.
- `websites.txt`: A list of websites to block (one per line).
- `tests.py`: Basic unit tests for the program (optional).

## 🖥️ Requirements
- **Python >=  3.12.3**
- **Administrator/root privileges** (required to modify the `hosts` file).

## 🚀 How to Run
1. Add the websites you want to block to the `websites.txt` file.
2. Open a terminal/command prompt with administrator privileges.
3. Run the following command:
    ```bash
    python main.py
    ```
4. The program will check every 5 minutes whether it's time to block or unblock the websites.

## 🕒 Example Block Hours
- Websites are blocked from **9 AM** to **5 PM** (adjust these times in `main.py` as needed).
  
## 📜 Notes
- Make sure to run the program with administrator privileges, as modifying the system's `hosts` file requires elevated permissions.
- This tool is meant to help with productivity. Use it responsibly to avoid blocking essential sites unintentionally.

## ⚠️ Disclaimer
This project is intended for personal use only. Be cautious while modifying the system's `hosts` file. Incorrect modifications might disrupt your network settings.

---

### Stay focused and block distractions! ⛔

# Happy coding 🖥️🚀