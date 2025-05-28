import segno
from flask import Flask, render_template, request, send_file, make_response, session
import os
from io import BytesIO

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/gerar', methods=['POST'])
def gerar():
    url = request.form['url']
    session['last_url'] = url
    return render_template('mostrando_qr_code.html')

@app.route('/qr_code.png')
def qr_code():
    url = session.get('last_url', None)
    if not url:
        return '', 404
    qr = segno.make(url)
    img_io = BytesIO()
    qr.save(img_io, kind='png', scale=10, border=5)
    img_io.seek(0)
    response = make_response(img_io.read())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'inline; filename=qr_code.png')
    return response

if __name__ == '__main__':
    app.run(debug=True)