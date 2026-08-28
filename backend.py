#!/usr/bin/env python3
"""
PhotoTag Backend - Flask Server
================================
Cara menjalankan lokal:
    pip install -r requirements.txt
    python backend.py

Deploy ke Render:
    1. Push ke GitHub
    2. Connect repo ke Render
    3. Render auto-detect Procfile & requirements.txt
"""

import os
import base64
import uuid
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

# CORS: izinkan semua origin (untuk GitHub Pages)
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Konfigurasi
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB

# Auto-detect BASE_URL
if os.environ.get('RENDER'):
    # Running di Render
    BASE_URL = os.environ.get('RENDER_EXTERNAL_URL', 'https://your-app.onrender.com')
elif os.environ.get('RAILWAY'):
    BASE_URL = os.environ.get('RAILWAY_STATIC_URL', 'https://your-app.railway.app')
else:
    # Local development
    BASE_URL = "http://localhost:5000"


@app.route('/')
def index():
    return jsonify({
        "status": "PhotoTag Backend Running",
        "base_url": BASE_URL,
        "endpoints": {
            "POST /upload": "Upload foto base64, return URL gambar",
            "GET /images/<filename>": "Akses gambar yang diupload",
            "GET /gallery": "List semua gambar"
        }
    })


@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload foto base64 ke server."""
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "Field 'image' diperlukan"}), 400

        image_data = data['image']
        metadata = data.get('metadata', {})

        # Parse base64
        if ',' in image_data:
            header, base64_str = image_data.split(',', 1)
        else:
            base64_str = image_data

        # Decode
        image_bytes = base64.b64decode(base64_str)

        # Generate nama file unik
        filename = "phototag_{}_{}.jpg".format(uuid.uuid4().hex[:8], int(datetime.now().timestamp()))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Simpan file
        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        # Simpan metadata
        meta_filename = filename.replace('.jpg', '.json')
        import json
        with open(os.path.join(app.config['UPLOAD_FOLDER'], meta_filename), 'w') as f:
            json.dump(metadata, f, indent=2)

        image_url = "{}/images/{}".format(BASE_URL, filename)

        return jsonify({
            "success": True,
            "filename": filename,
            "url": image_url,
            "metadata": metadata
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/images/<filename>')
def serve_image(filename):
    """Serving gambar yang sudah diupload."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/gallery')
def gallery():
    """List semua gambar yang tersedia."""
    files = []
    for f in sorted(os.listdir(UPLOAD_FOLDER)):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            filepath = os.path.join(UPLOAD_FOLDER, f)
            stat = os.stat(filepath)
            files.append({
                "filename": f,
                "url": "{}/images/{}".format(BASE_URL, f),
                "size_kb": round(stat.st_size / 1024, 2),
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat()
            })
    return jsonify({"count": len(files), "images": files[::-1]})


if __name__ == '__main__':
    # Local development
    port = int(os.environ.get('PORT', 5000))
    print("=" * 50)
    print("PhotoTag Backend Server")
    print("=" * 50)
    print("Upload folder: {}".format(UPLOAD_FOLDER))
    print("Base URL: {}".format(BASE_URL))
    print("=" * 50)
    print("\nMenjalankan server di http://localhost:{}".format(port))
    print("Tekan Ctrl+C untuk berhenti\n")

    app.run(host='0.0.0.0', port=port, debug=True)
