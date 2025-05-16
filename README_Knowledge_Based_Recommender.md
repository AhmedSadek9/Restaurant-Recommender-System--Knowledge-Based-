
# 🍽️ Knowledge-Based Restaurant Recommender System

An interactive Streamlit web application that recommends restaurants based on explicit user preferences—such as cuisine type, budget, and location—using the Zomato dataset. Unlike collaborative filtering, this system does not rely on historical user behavior, making it cold-start-free and ideal for first-time users.

## 📌 Objective

To build a **knowledge-based restaurant recommender system** that delivers personalized and explainable dining recommendations by matching user-defined criteria against a structured dataset of restaurant metadata.

## 🚀 Key Features

### ✅ Core Features

- 🔍 **Smart Preference Filtering**  
  Match user inputs for:
  - 🍱 Cuisine type (e.g., Indian, Chinese)
  - 💰 Budget (low, medium, high)
  - 📍 Location (exact or approximate match)

- 📊 **Custom Ranking System**  
  Score restaurants using:
  - ⭐ Average User Rating (weighted)
  - 🗳️ Number of Votes (credibility)
  - 🔥 Optional: Popularity or proximity (geo-based)

- 🧠 **Explainable Recommendations**  
  Each recommendation includes a concise explanation of why it was suggested (e.g., "Matched on Chinese cuisine in Mumbai under ₹800 with a 4.5 rating").

- 🖥️ **Streamlit Web Interface**  
  Clean, intuitive sidebar for input + interactive result cards showing name, rating, cost, and cuisine.

### 🌟 Additional Features

- 🗺️ **Interactive Map View**  
  Visualize recommended restaurants using Folium or Streamlit’s `st.map`.

- 🔁 **Dynamic Re-Ranking**  
  Allow users to fine-tune the ranking algorithm with sliders (e.g., rating weight vs. popularity weight).

- 📍 **Proximity-Based Sorting**  
  Users can optionally enter a location and sort restaurants by distance.

- 💬 **Live Feedback Collection**  
  Embedded user feedback mechanism (Likert scale or comment box) to assess satisfaction.

- 📦 **Real-Time Filtering**  
  Add checkboxes or toggles to instantly refine results (e.g., vegetarian-only, delivery available).

- 🏷️ **Tag-Based Filtering**  
  Support additional filters like ambiance (e.g., family-friendly, romantic), service type, or available facilities.

- 📸 **Media Integration** *(optional)*  
  Show images or menus using Zomato links or image APIs.

- 📅 **Reservation & Timing Info** *(optional)*  
  Include restaurant hours and reservation support if available.

## 🛠️ Tech Stack

| Component     | Technology     |
|---------------|----------------|
| Language      | Python          |
| Frontend      | Streamlit       |
| Backend Logic | pandas, numpy   |
| Data Source   | [Zomato Kaggle Dataset](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data) |
| Mapping       | Folium / Streamlit Map |
| Hosting       | Streamlit Cloud / Render |

## 📂 Project Structure

```
restaurant-recommender/
│
├── data_preprocessing.py       # Load, clean, and preprocess the dataset
├── recommender.py              # Core recommendation logic (filtering + scoring)
├── app.py                      # Streamlit front-end application
├── evaluation.md               # Evaluation feedback and improvement proposals
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## ⚙️ Functional Overview

### 🧹 Data Ingestion & Preprocessing
- Remove duplicates and nulls
- Normalize text (lowercase, synonyms)
- Convert ratings, price, and votes to numeric
- Feature engineering: extract primary cuisine, classify price bucket

### 🤖 Recommendation Engine
- Apply user filters
- Rank based on weighted scoring:
  ```
  Score = w1 * Rating + w2 * Votes + w3 * Popularity
  ```
- Normalize and return Top-N results

### 🧑‍💻 User Interface
- Sidebar inputs: cuisine, location, budget
- Results area with:
  - Restaurant name
  - Cuisine, cost, rating
  - Explanation text
  - Map link or location
  - Feedback option (optional)

### 📊 Evaluation
- User satisfaction surveys (1–5 scale or thumbs-up/down)
- Compare filtering strategies via A/B testing
- Metrics:
  - Relevance of results
  - Interface usability
  - Time-to-result

## ✅ Deliverables

| Component                | Description |
|--------------------------|-------------|
| Data Scripts             | Dataset ingestion & cleaning scripts |
| Recommendation Engine    | `filter_and_rank()` with scoring logic |
| Streamlit App            | GUI for input + results |
| Evaluation Report        | Markdown/PDF with results and feedback |
| Deployment               | Public link on Streamlit Cloud or Render |

## 📈 Future Enhancements

- 🔔 **Notification System** for favorite cuisines
- 📍 **Location Detection** via geolocation API
- 🗃️ **User Profiles** for storing preferences
- 💡 **Hybrid Model**: Combine knowledge-based and collaborative filtering
- 🧠 **ML Integration**: Predict user preferences using classification models

## 🌐 Live Demo

*(Optional — Add your Streamlit Cloud deployment link here)*

## 👤 Author

**Your Name**  
📧 *your.email@example.com*  
🔗 [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)
