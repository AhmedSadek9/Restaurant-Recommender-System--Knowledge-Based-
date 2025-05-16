import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class RestaurantRecommender:
    def __init__(self, data):
        self.data = data
        self.scaler = MinMaxScaler()
        
    def filter_restaurants(self, cuisine=None, location=None, price_bucket=None):
        """Filter restaurants based on user preferences"""
        filtered = self.data.copy()
        
        if cuisine:
            filtered = filtered[filtered['Cuisines'].str.contains(cuisine.lower())]
        
        if location:
            filtered = filtered[filtered['Location'].str.lower() == location.lower()]
        
        if price_bucket:
            filtered = filtered[filtered['Price Bucket'] == price_bucket]
            
        return filtered
    
    def calculate_scores(self, df):
        """Calculate recommendation scores"""
        # Normalize ratings and votes
        df['Rating_norm'] = self.scaler.fit_transform(df[['Aggregate rating']])
        df['Votes_norm'] = self.scaler.fit_transform(df[['Votes']])
        
        # Calculate weighted score (70% rating, 30% votes)
        df['Score'] = 0.7 * df['Rating_norm'] + 0.3 * df['Votes_norm']
        return df
    
    def recommend(self, cuisine=None, location=None, price_bucket=None, top_n=5):
        """Generate recommendations based on filters"""
        filtered = self.filter_restaurants(cuisine, location, price_bucket)
        
        if filtered.empty:
            return pd.DataFrame()
        
        scored = self.calculate_scores(filtered)
        recommendations = scored.sort_values('Score', ascending=False).head(top_n)
        
        return recommendations
    
    def generate_explanation(self, restaurant):
        """Generate explanation for recommendation"""
        explanation = f"Matched on {restaurant['Primary Cuisine'].title()} cuisine"
        
        if pd.notna(restaurant['Price Bucket']):
            explanation += f", {restaurant['Price Bucket']} budget"
        
        explanation += f" with {restaurant['Aggregate rating']} rating"
        
        if restaurant['Votes'] > 1000:
            explanation += " (popular choice)"
            
        return explanation

if __name__ == "__main__":
    from data_processing import preprocess_data
    df = preprocess_data()
    recommender = RestaurantRecommender(df)
    recs = recommender.recommend(cuisine='indian', price_bucket='Medium')
    print(recs[['Restaurant Name', 'Primary Cuisine', 'Price Bucket', 'Aggregate rating', 'Score']])