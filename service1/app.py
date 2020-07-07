from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    combine=requests.get("http://service4:5003")
    print(combine)
    return render_template('home.html', title='Home', combine=combine)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')