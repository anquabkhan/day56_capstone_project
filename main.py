from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/hello')
def say_hello():
    return "Hello, world"


@app.route('/orignal')
def blog():
    return render_template("blog.html")


@app.route('/')
def title():
    response = requests.get("https://api.npoint.io/de18eeb516a00f96e786")
    data = response.json()
    # print(data['Title'])
    # return data['Title']
    return render_template("blog.html", title=data[0]['Title'], body=data[0]['body'], data=data)


@app.route('/expand/<int:num>')
def expand(num):
    response = requests.get("https://api.npoint.io/de18eeb516a00f96e786")
    data = response.json()
    return render_template('blog2.html', d=data, n=num)


if __name__ == '__main__':
    app.run(debug=True)
