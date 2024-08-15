import segno 
# qr = segno.make('https://miguelfermo.netlify.app')

from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify, send_file, render_template
import os
import time
  
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/') 
def index():
    return render_template('index.html') 

@app.route('/gerar', methods=['POST'])
def gerar():
    url = request.form['url']
    qr = segno.make(url)
    qr.save('qr_code.png', scale=100, border=5) 
    return render_template('mostrando_qr_code.html')

@app.route('/qr_code.png')
def qr_code():
    return send_file('qr_code.png')

if __name__ == '__main__':
    app.run(debug=True)