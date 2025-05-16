import streamlit as st
import folium
from streamlit_folium import folium_static
from data_processing import preprocess_data
from recommendation_engine import RestaurantRecommender

def setup_sidebar():
    """Setup the sidebar with user input controls"""
    st.sidebar.header("Restaurant Preferences")
    
    # Load data and initialize recommender
    df = preprocess_data()
    recommender = RestaurantRecommender(df)
    
    # Get unique values for filters
    cuisines = sorted(df['Primary Cuisine'].unique())
    locations = sorted(df['Location'].unique())
    price_buckets = ['Low', 'Medium', 'High']
    
    # User inputs
    selected_cuisine = st.sidebar.selectbox(
        "Preferred Cuisine",
        ['Any'] + cuisines
    )
    
    selected_location = st.sidebar.selectbox(
        "Preferred Location",
        ['Any'] + locations
    )
    
    selected_price = st.sidebar.selectbox(
        "Price Range",
        ['Any'] + price_buckets
    )
    
    top_n = st.sidebar.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5
    )
    
    return {
        'cuisine': None if selected_cuisine == 'Any' else selected_cuisine,
        'location': None if selected_location == 'Any' else selected_location,
        'price_bucket': None if selected_price == 'Any' else selected_price,
        'top_n': top_n,
        'recommender': recommender
    }

def display_recommendations(recommendations, recommender):
    """Display recommendations in the main area"""
    st.header("Recommended Restaurants")
    
    if recommendations.empty:
        st.warning("No restaurants match your criteria. Try broadening your search.")
        return
    
    # Create a map centered on the first recommendation
    map_center = [recommendations.iloc[0]['Latitude'], recommendations.iloc[0]['Longitude']]
    m = folium.Map(location=map_center, zoom_start=13)
    
    for _, row in recommendations.iterrows():
        # Add marker to map
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=row['Restaurant Name'],
            tooltip=f"{row['Restaurant Name']} - Rating: {row['Aggregate rating']}"
        ).add_to(m)
        
        # Create an expandable card for each recommendation
        with st.expander(f"🍽️ {row['Restaurant Name']} - ⭐ {row['Aggregate rating']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader(row['Restaurant Name'])
                st.caption(f"📍 {row['Location']}")
                st.write(f"**Cuisine:** {row['Primary Cuisine'].title()}")
                st.write(f"**Price Range:** {row['Price Bucket']} (${row['Average Cost for two']} for two)")
                st.write(f"**Rating:** {row['Aggregate rating']} from {row['Votes']} votes")
                st.write(f"**Why we recommend this:** {recommender.generate_explanation(row)}")
                
            with col2:
                st.metric("Average Cost for Two", f"${row['Average Cost for two']}")
    
    # Display the map
    st.header("Restaurant Locations")
    folium_static(m)

def main_ui():
    """Main user interface function"""
    st.set_page_config(page_title="Restaurant Recommender", page_icon="🍽️", layout="wide")
    st.title("🍽️ Knowledge-Based Restaurant Recommender")
    
    # Setup sidebar and get user preferences
    inputs = setup_sidebar()
    
    # Get recommendations
    recommendations = inputs['recommender'].recommend(
        cuisine=inputs['cuisine'],
        location=inputs['location'],
        price_bucket=inputs['price_bucket'],
        top_n=inputs['top_n']
    )
    
    # Display recommendations
    display_recommendations(recommendations, inputs['recommender'])

if __name__ == "__main__":
    main_ui()


    #streamlit run main.py