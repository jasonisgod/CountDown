from flask import Flask, request, render_template, send_file
from datetime import datetime

HOST = '0.0.0.0'
PORT = 1205
PATH = './test.jpg'
DTS = "2022-06-09 00:00:00"
DT = datetime.strptime(DTS, '%Y-%m-%d %H:%M:%S')

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def index():
    dt = datetime.now()
    dts = dt.strftime("%Y-%m-%d %H:%M:%S")
    if dt < DT:
        diff = int((DT - dt).total_seconds())
        hh, mm, ss = str(diff//3600%60), str(diff//60%60), str(diff%60)
        hh_mm_ss = f'{hh:0>2s}:{mm:0>2s}:{ss:0>2s}'
        return hh_mm_ss
    return send_file(PATH)

if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT)

