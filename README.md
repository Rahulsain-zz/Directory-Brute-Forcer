# Directory-Brute-Forcer
# 🔍 Directory Brute Forcer (Python)

> Discover hidden paths and directories on web servers using Python & wordlists.

---

## 🚀 Features

- ✅ Multi-threaded for faster scans
- ✅ Shows status codes (200, 403, 301, etc.)
- ✅ Automatically saves found paths to file
- ✅ Built with Python’s `requests` and `threading`

---

## 🖥️ Usage


python dir_brute.py

You'll be prompted to enter:

   Target base URL (e.g. https://example.com)

   Wordlist path (e.g. wordlist.txt)

  🧠 How It Works

  Reads each path from the wordlist

  Appends it to the base URL

  Sends a GET request

  Reports if it returns a meaningful status code (200/301/403/etc.)

  📦 Requirements

Install dependencies:

pip install -r requirements.txt

📁 Output

Found URLs are saved to:

found_paths.txt

⚠️ Legal Note

This tool is for educational & authorized use only. Never test unauthorized websites. You're responsible for your actions.
