from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)




@app.route('/api/add/<int:a>/<int:b>', methods=['GET'])
def add_api(a, b):
    return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True)
