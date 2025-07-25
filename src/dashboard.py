from flask import Flask, render_template, request
from src.data_ingestion import DataIngestion
from src.analysis_engine import AnalysisEngine
from src.explainability import Explainability

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        ingestion = DataIngestion(file)
        data = ingestion.load_data()
        engine = AnalysisEngine(data)
        forecast = engine.forecast_sales()
        return render_template('results.html', forecast=forecast.to_dict())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)