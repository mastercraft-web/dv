#!/usr/bin/env python
# – coding: utf-8
import os
from flask import Flask, render_template, request, send_file, redirect, url_for
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    quality = request.form['quality']
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]/best',
            'outtmpl': 'static/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_file = info['title'] + '.mp4'
        
        # Mostrar el video en la página HTML
        return render_template('video.html', video_file=video_file)
    except Exception as e:
        return str(e)

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
