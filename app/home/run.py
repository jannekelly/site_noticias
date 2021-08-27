from flask import Flask,jsonify
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
   nome = "Alisson"
   posts = ["Flask Basico","Flask Intermediario","Flask Avancado"]
   return render_template("index.html",nome=nome,posts=posts)
if __name__ == '__main__':
    app.run(debug=True)
