from flask import Flask

app = Flask(__name__, template_folder="templates")

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')