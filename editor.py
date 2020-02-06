from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('editor.html')


if __name__ == '__main__':
    app.run(debug=True)