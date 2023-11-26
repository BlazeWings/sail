# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    dl = int(request.form['dl'])
    pz = float(request.form['pz'])
    rg = int(request.form['rg'])
    sl = int(request.form['sl'])
    lr = 0
    dj = 0
    for i in range(0, 13):
        lr = dl * (1 + pz * i) * sl - sl * dj - rg
        while lr > 0:
            dj = dj + 1
            lr = dl * (1 + pz * i) * sl - sl * dj - rg
    return f"q {i} 交易价格 {dj}"

if __name__ == '__main__':
    app.run(debug=True)
