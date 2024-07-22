import pandas as pd


file_path = 'neighbourhoodFinder/chrome/FSAs.csv'

# Function to load the dataset
def load_dataset(file_path):
    return pd.read_csv(file_path)

# Function to find neighborhood by postal code
def find_neighborhood(postal_code, dataset):
    result = dataset.loc[dataset['PostalCode'] == postal_code, 'Neighborhood']
    if not result.empty:
        return result.values[0]
    else:
        return "Postal code not found in the dataset."



print (load_dataset(file_path))

# Main script
if __name__ == "__main__":
    dataset = load_dataset(file_path)
    
    # Example postal code to search for
    postal_code_to_search = 'V6T'
    
    # Find and print the neighborhood
    neighborhood = find_neighborhood(postal_code_to_search, dataset)
    print(f'Neighborhood for {postal_code_to_search}: {neighborhood}')


# # Function to load the dataset
# def load_dataset(file_path):
#     return pd.read_csv(file_path)
# 
# # Function to find neighborhood by postal code
# def find_neighborhood(postal_code, dataset):
#     result = dataset.loc[dataset['PostalCode'] == postal_code, 'Neighborhood']
#     if not result.empty:
#         return result.values[0]
#     else:
#         return "Postal code not found in the dataset."
# 
# # Main script
# if __name__ == "__main__":
#     # Load the dataset
#     file_path = 'postal_codes.csv'
#     dataset = load_dataset(file_path)
#     
#     # Example postal code to search for
#     postal_code_to_search = '10001'
#     
#     # Find and print the neighborhood
#     neighborhood = find_neighborhood(postal_code_to_search, dataset)
#     print(f'The neighborhood for postal code {postal_code_to_search} is: {neighborhood}')