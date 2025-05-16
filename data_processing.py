import pandas as pd
import numpy as np

PRICE_BUCKETS = {
    'Low': (0, 400),
    'Medium': (401, 700),
    'High': (701, float('inf'))
}

def load_data(filepath):
    """Load the dataset from CSV file"""
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully")
        return df
    except FileNotFoundError:
        print("File not found. Using synthetic data instead.")
        return create_synthetic_data()

def create_synthetic_data():
    """Create synthetic data if real data is not available"""
    np.random.seed(42)
    num_restaurants = 500
    cuisines = ['Indian', 'Chinese', 'Italian', 'Mexican', 'Japanese', 'Thai', 'American', 'Mediterranean']
    locations = ['Downtown', 'Midtown', 'Uptown', 'Eastside', 'Westside']
    
    data = {
        'Restaurant Name': [f"Restaurant {i}" for i in range(num_restaurants)],
        'Cuisines': [', '.join(np.random.choice(cuisines, np.random.randint(1, 3), replace=False)) for _ in range(num_restaurants)],
        'Location': np.random.choice(locations, num_restaurants),
        'Average Cost for two': np.random.randint(200, 1500, num_restaurants),
        'Aggregate rating': np.round(np.random.uniform(2.5, 5, num_restaurants), 1),
        'Votes': np.random.randint(10, 5000, num_restaurants),
        'Latitude': np.random.uniform(12.8, 13.2, num_restaurants),
        'Longitude': np.random.uniform(77.5, 77.7, num_restaurants)
    }
    return pd.DataFrame(data)

def clean_data(df):
    """Clean and preprocess the data"""
    # Remove duplicates
    df = df.drop_duplicates(subset=['Restaurant Name', 'Location'])
    
    # Normalize cuisines
    df['Cuisines'] = df['Cuisines'].str.lower().str.strip()
    
    # Handle missing values
    df = df.dropna(subset=['Cuisines', 'Average Cost for two', 'Aggregate rating'])
    
    # Create price bucket
    df['Price Bucket'] = pd.cut(
        df['Average Cost for two'],
        bins=[0, 400, 700, float('inf')],
        labels=['Low', 'Medium', 'High']
    )
    
    # Extract primary cuisine
    df['Primary Cuisine'] = df['Cuisines'].str.split(',').str[0].str.strip()
    
    return df

def preprocess_data(filepath='zomato_data.csv'):
    """Main data processing function"""
    df = load_data(filepath)
    df = clean_data(df)
    return df

if __name__ == "__main__":
    df = preprocess_data()
    print(df.head())