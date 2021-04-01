from flask import Flask
app = Flask(__name__)

@app.route('/')
def title():
    return "Hello World"

@app.route('/dojo')
def success():
  return "Dojo"

@app.route('/repeat/<name>/<int:number>')
def myNames(name,number):
    return name * number


if __name__ == "__main__":
    app.run(debug=True)
