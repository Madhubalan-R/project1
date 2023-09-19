from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_phishing_link(link):
    pattern = r'(http|https)://([a-zA-Z0-9]+[.])*([a-zA-Z0-9]+\.)+(com|org|net|gov|edu|mil|info|biz)'
    if re.match(pattern, link):
        return False
    else:
        return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_link', methods=['POST'])
def check_link():
    user_link = request.form['link']
    if check_phishing_link(user_link):
        return "Alert: The entered link may be a phishing attempt!"
    else:
        return "The entered link appears to be legitimate."

if __name__ == '__main__':
    app.run()
