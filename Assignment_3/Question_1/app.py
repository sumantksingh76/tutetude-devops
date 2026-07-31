from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the Flask API"

@app.route('/api')
def data():
    file = open("data.json", 'r')

    data = file.read()
    return data
    

if __name__ == '__main__':
    app.run(debug=True)