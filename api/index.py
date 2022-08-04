from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    return {"success": True, 'test': 'ok'}

@app.route('/')
def get_server_ip():
    res = requests.get("https://api4.ipify.org/?format=json")
    return {"success": True, 'ip': res.json()['ip']}

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
