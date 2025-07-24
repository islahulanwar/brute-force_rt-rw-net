# 🔐 Brute Force Voucher RT/RW Net - GUI (Microsoft Edge)

Program Python ini digunakan untuk melakukan brute force login ke halaman login RT/RW Net, dengan antarmuka GUI berbasis Tkinter dan browser otomatis menggunakan Microsoft Edge atau browser yang lain (Selenium WebDriver).

> ⚠️ **FOR EDUCATIONAL PURPOSES ONLY** ⚠️  
>  This project is intended for educational and ethical testing purposes only.
>  Do NOT use this on networks or systems you do not own or have explicit permission to test.
>  Use responsibly. The author takes no responsibility for misuse.

---

## 🎯 Fitur

- Generate kode voucher otomatis: `k5` + 2 huruf + 2 angka (contoh: `k5sj65`) atau bisa disesuaikan dengan pola voucher RT/RW Net yang ada
- Login otomatis ke halaman hotspot menggunakan Microsoft Edge (headless)
- Deteksi redirect URL untuk memverifikasi login sukses
- Simpan voucher valid ke file `valid_voucher.txt`
- GUI interaktif:
  - ✅ Mulai brute force
  - 🛑 Hentikan brute force
  - 📄 Tampilkan daftar voucher valid

---

## 🧠 Cara Kerja

Program akan:

1. Meng-generate kombinasi kode voucher secara acak dengan format `k5[a-z][a-z][0-9][0-9]`.
2. Mencoba login ke halaman seperti berikut:

   ```
   http://goa.tech/login?dst=http://www.msftconnecttest.com/redirect&popup=true&username=<voucher>&password=<voucher>
   ```

3. Jika login berhasil, akan ter-redirect ke halaman `/status`.
4. Jika login gagal, URL akan tetap di halaman `/login`.
5. Voucher yang valid disimpan otomatis ke file `valid_voucher.txt`.

---

## 🧩 Struktur Generate Kode Voucher (Sesuaikan dengan Kebutuhan)

```python
def generate_voucher():
    huruf = string.ascii_lowercase
    angka = string.digits
    return "k5" + ''.join(random.choices(huruf, k=2)) + ''.join(random.choices(angka, k=2))
```

Contoh hasil:
```
k5ab12
k5ks45
k5ty91
```

---

## 💻 Kebutuhan Sistem

- Python 3.7 atau lebih baru
- Microsoft Edge atau browser yang digunakan 
- Edge WebDriver (msedgedriver.exe) atau sesuaikan dengan WebDriver browser yang digunakan
- Selenium Python library

---

## 📦 Instalasi

1. **Clone repositori**:

   ```bash
   git clone https://github.com/islahulanwar/brute-force_rt-rw-net.git
   ```

2. **Install dependensi Python**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Microsoft Edge WebDriver**  
   Sesuaikan dengan versi browsermu:
   - Edge ➡️ https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Chrome ➡️ https://developer.chrome.com/docs/chromedriver/downloads
   - FireFox ➡️ https://developer.mozilla.org/en-US/docs/Web/WebDriver

---

## 🚀 Menjalankan Program

```bash
WebDriver.exe
brute_force_voucher.py
```

GUI akan muncul, kemudian kamu bisa:

- Klik **"Mulai Brute Force"** untuk memulai
- Klik **"STOP"** untuk menghentikan
- Klik **"Lihat Voucher Valid"** untuk membuka log valid

---

## 📁 Output

Voucher yang valid akan dicatat di:

```
valid_voucher.txt
```

Contoh isi:

```
k5sj65 | 2025-07-24 11:45:32
```

---

## 📂 Struktur Folder

```
.
├── WebDriver.exe
├── brute_force_voucher.py
├── valid_voucher.txt
├── requirements.txt
└── README.md
```

---

## 🧾 File requirements.txt

```text
selenium
```

---

## ⚠️ Disclaimer

> Program ini hanya untuk tujuan edukasi!  
> Dilarang menggunakan alat ini untuk mengakses jaringan tanpa izin.  
> Penggunaan di luar tanggung jawab penulis dan dapat melanggar hukum yang berlaku.

---
