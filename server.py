from flask import Flask , jsonify , request , render_template
import joblib

app = Flask(__name__)

model = joblib.load('predict.plk')

@app.route('/predict',methods=["POST"])
def predict():
    data = request.json
    room_size = int(data['room_size'])
    bedrooms = int(data['bedrooms'])
    predicted_price = model.predict([[room_size,bedrooms]])
    return jsonify({"predicted_price":predicted_price[0]})
@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
