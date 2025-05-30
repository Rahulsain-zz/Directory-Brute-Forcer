import requests
import threading
import queue
import time

# ===== CONFIG =====
THREADS = 10
q = queue.Queue()
found_paths = []

def load_wordlist(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Wordlist Error: {e}")
        return []

def check_url(base_url, path):
    url = f"{base_url}/{path}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in [200, 301, 302, 403]:
            print(f"[+] Found: {url} (Status: {response.status_code})")
            found_paths.append(f"{url} - {response.status_code}")
    except requests.RequestException:
        pass

def worker(base_url):
    while not q.empty():
        path = q.get()
        check_url(base_url, path)
        q.task_done()

def main():
    base_url = input("Enter base URL (e.g., https://example.com): ").strip().rstrip('/')
    wordlist_path = input("Enter wordlist path: ").strip()

    paths = load_wordlist(wordlist_path)
    if not paths:
        return

    for path in paths:
        q.put(path)

    print(f"\n🚀 Starting directory brute force with {THREADS} threads...")
    start = time.time()

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker, args=(base_url,))
        t.start()
        threads.append(t)

    q.join()

    end = time.time()
    print(f"\n⏱️ Scan complete in {round(end - start, 2)} seconds.")

    if found_paths:
        with open("found_paths.txt", "w") as f:
            for path in found_paths:
                f.write(path + "\n")
        print("[+] Results saved to found_paths.txt")
    else:
        print("[-] No directories found.")

if __name__ == "__main__":
    main()
