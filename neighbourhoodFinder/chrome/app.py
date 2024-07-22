from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('FSAs.csv')

def find_neighborhood(postal_code, dataset):
    FSA = dataset.loc[dataset['PostalCode'] == postal_code, 'Neighborhood']
    if not FSA.empty:
        return FSA.values[0]
    else:
        return "Postal code not found in the dataset."

@app.route('/neighborhood', methods=['GET'])

def get_neighborhood():
    postal_code = request.args.get('postal_code')
    if not postal_code:
        return jsonify({'error': 'Postal code is required'}), 400
    
    neighborhood = find_neighborhood(postal_code, dataset)
    return (jsonify({'neighborhood': neighborhood}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  