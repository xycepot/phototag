# 📸 PhotoTag - GPS Photo Tagging App

Aplikasi web modern untuk memotret foto dengan watermark lokasi (GPS) otomatis.

---

## 🚀 Quick Start (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Jalankan backend
python backend.py

# 3. Buka frontend
# - Buka index.html di browser (double-click)
# - Atau: python -m http.server 8080
```

---

## 📁 Struktur Folder

```
phototag/
├── backend.py          # Flask server
├── requirements.txt    # Python dependencies
├── Procfile            # Render deployment config
├── runtime.txt         # Python version for Render
├── index.html          # Frontend app
├── .gitignore          # Git ignore rules
├── README.md           # Dokumentasi ini
├── DEPLOY.md           # Panduan deploy online
└── uploads/            # Folder foto (auto-create)
```

---

## 🔌 API Endpoints

| Endpoint | Method | Deskripsi |
|----------|--------|-----------|
| `/` | GET | Status server |
| `/upload` | POST | Upload foto base64 |
| `/images/<filename>` | GET | Akses gambar |
| `/gallery` | GET | List semua gambar |

---

## 🌐 Deploy Online

Lihat **[DEPLOY.md](DEPLOY.md)** untuk panduan lengkap deploy ke:
- **Frontend** → GitHub Pages (Gratis + HTTPS)
- **Backend** → Render.com (Gratis)

Ringkasnya:
1. Push repo ke GitHub
2. Deploy backend ke Render
3. Update `PROD_BACKEND_URL` di `index.html`
4. Aktifkan GitHub Pages
5. Selesai! 🎉

---

## ✨ Fitur

- 📷 Kamera depan & belakang
- 📍 GPS auto-tagging (Lat, Long, Alamat, Waktu)
- 🗺️ Reverse geocoding via OpenStreetMap
- ☁️ Upload ke backend
- 💬 Kirim WhatsApp (3 cara otomatis)
- ⬇️ Download lokal
- 📐 Grid overlay
- 📱 Responsive mobile

---

## 🛠️ Tech Stack

| Layer | Teknologi |
|-------|-----------|
| Frontend | HTML5, Tailwind CSS, Vanilla JS |
| Backend | Python 3, Flask, Gunicorn |
| Hosting | GitHub Pages + Render |
| Geolocation | OpenStreetMap Nominatim |

---

## 🔒 Catatan

- Kamera & GPS hanya jalan di **HTTPS** atau **localhost**
- Render free tier: file upload akan hilang saat server sleep
- Untuk production, gunakan cloud storage (S3/Cloudinary)
