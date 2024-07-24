from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('FSAs.csv')

def find_neighbourhood(postal_code, dataset):
    postal_code = postal_code[:3].upper()
    FSA = dataset.loc[dataset['FSA'] == postal_code, 'Neighbourhood']
    if not FSA.empty:
        return FSA.values[0]
    else:
        return

@app.route('/neighbourhood', methods=['GET'])

def get_neighbourhood():
    postal_code = request.args.get('postal_code')
    if not postal_code:
        return jsonify({'error': 'Postal code is required'}), 400
    
    neighbourhood = find_neighbourhood(postal_code, dataset)
    return (jsonify({'neighbourhood': neighbourhood}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
  