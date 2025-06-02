from flask import Flask

# αρχικοποιηση flask app
app = Flask(__name__)#, static_folder="static")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
