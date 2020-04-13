from src.prep_data import PrepData
from src.predict_data import PredictData
from src.load_data import LoadData
from flask import Flask, jsonify, request

app = Flask(__name__)

loader = LoadData()
prep = PrepData()
model = loader.load_model('./models/cal_model.pkl')
predictor = PredictData(model)

@app.route("/", methods=['POST'])
def predict_score():
    json = request.get_json()
    df = loader.userdata_to_df(json)

    prediction = predictor.predict(df)
    return jsonify({'divorce': prediction[0][1]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)