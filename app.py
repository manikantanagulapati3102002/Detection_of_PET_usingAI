from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None  # default: no prediction shown
    if request.method == 'POST':
        file = request.files['image']

        # Send image to FastAPI for prediction
        response = requests.post("http://127.0.0.1:8000/predict", files={'file': file})
        
        if response.status_code == 200:
            prediction = response.json()  # {'class': 'cat', 'confidence': 0.87}
        else:
            prediction = {'class': 'error', 'confidence': 0}

    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
