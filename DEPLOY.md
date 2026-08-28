# 🚀 Panduan Deploy PhotoTag ke Online (HTTPS)

## 📋 Ringkasan Arsitektur

```
┌─────────────────┐         HTTPS          ┌─────────────────┐
│  GitHub Pages   │  ◄─────────────────►   │  Render.com     │
│  (Frontend)     │    API Request         │  (Backend)      │
│  index.html     │                        │  Flask + Python │
│  Gratis         │  ◄─────────────────►   │  Gratis         │
└─────────────────┘    Image URL           └─────────────────┘
     https://username.github.io/phototag       https://phototag-xxx.onrender.com
```

---

## Bagian 1: Deploy Backend ke Render (GRATIS)

### Step 1: Push ke GitHub

Buat repository baru di GitHub, lalu push semua file:

```bash
cd C:\Users\userp\MyApp\phototag

# Inisialisasi git
git init
git add .
git commit -m "Initial commit - PhotoTag app"

# Ganti URL di bawah dengan repo GitHub Anda
git remote add origin https://github.com/USERNAME/phototag.git
git branch -M main
git push -u origin main
```

### Step 2: Daftar & Deploy ke Render

1. Buka [https://render.com](https://render.com) → Sign Up (gratis) pakai GitHub
2. Klik **"New +"** → Pilih **"Web Service"**
3. Connect ke repository GitHub `phototag` Anda
4. Isi form:
   - **Name**: `phototag-backend` (atau nama lain)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backend:app`
   - **Plan**: Free
5. Klik **"Create Web Service"**
6. Tunggu 2-3 menit sampai status **"Live"**
7. Catat URL-nya, contoh: `https://phototag-backend.onrender.com`

### Step 3: Update Frontend

Buka `index.html`, cari baris:

```javascript
const PROD_BACKEND_URL = 'https://phototag-backend.onrender.com';
```

Ganti dengan URL Render Anda yang sebenarnya, lalu commit & push:

```bash
git add index.html
git commit -m "Update backend URL"
git push
```

---

## Bagian 2: Deploy Frontend ke GitHub Pages (GRATIS)

### Step 1: Aktifkan GitHub Pages

1. Buka repository GitHub Anda
2. Klik **Settings** → tab **Pages** (di sidebar kiri)
3. Di bagian **"Build and deployment"**:
   - **Source**: Pilih **"Deploy from a branch"**
   - **Branch**: Pilih **"main"** → folder **"/ (root)"**
   - Klik **Save**
4. Tunggu 1-2 menit
5. URL akan muncul, contoh: `https://username.github.io/phototag/`

### Step 2: Akses Aplikasi

Buka URL GitHub Pages di browser:
```
https://username.github.io/phototag/
```

---

## ✅ Cek List Verifikasi

| Cek | Status |
|-----|--------|
| Backend Render status "Live" | ☐ |
| URL backend bisa diakses (buka di browser) | ☐ |
| `PROD_BACKEND_URL` di `index.html` sudah diganti | ☐ |
| GitHub Pages sudah aktif | ☐ |
| Buka frontend di HP → kamera & lokasi jalan | ☐ |
| Foto tersimpan di folder uploads Render | ☐ |
| Kirim WhatsApp → link foto bisa dibuka | ☐ |

---

## 🔧 Troubleshooting

### "Backend tidak terhubung" di frontend
- Cek URL `PROD_BACKEND_URL` di `index.html` sudah benar
- Cek backend Render sudah "Live" (bukan "Deploying")
- Coba buka URL backend langsung di browser, harus muncul JSON

### Kamera tidak muncul di HP
- GitHub Pages pakai **HTTPS** ✅ — seharusnya bisa
- Pastikan browser diizinkan akses kamera
- Coba pakai Chrome/Safari (Firefox kadang strict)

### Foto tidak tersimpan
- Render free tier: file di folder `uploads/` akan **hilang** saat server restart
- Solusi: upgrade ke paid tier atau gunakan cloud storage (AWS S3/Cloudinary)
- Untuk demo/testing, ini tidak masalah

### CORS Error di console
- Pastikan `CORS(app, resources={...})` sudah ada di `backend.py`
- Render URL sudah benar di `PROD_BACKEND_URL`

---

## 💡 Tips

- **Custom Domain**: Bisa tambahkan custom domain di GitHub Pages & Render
- **Auto-deploy**: Setiap push ke GitHub, Render akan auto-deploy ulang
- **Environment Variable**: Di Render Dashboard → Environment, bisa set `BASE_URL` jika perlu

---

Selamat! Aplikasi Anda sekarang online dan bisa diakses dari mana saja! 🎉
