from flask import Flask, render_template

app = Flask(__name__)

#creating index route

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)