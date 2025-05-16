import pandas as pd
from recommendation_engine import RestaurantRecommender
from data_processing import preprocess_data

def evaluate_recommendations(test_cases):
    """Evaluate the recommendation system with test cases"""
    df = preprocess_data()
    recommender = RestaurantRecommender(df)
    
    results = []
    
    for case in test_cases:
        recs = recommender.recommend(
            cuisine=case.get('cuisine'),
            location=case.get('location'),
            price_bucket=case.get('price_bucket'),
            top_n=case.get('top_n', 5)
        )
        
        results.append({
            'test_case': case,
            'num_recommendations': len(recs),
            'average_rating': recs['Aggregate rating'].mean() if not recs.empty else 0,
            'min_rating': recs['Aggregate rating'].min() if not recs.empty else 0,
            'max_rating': recs['Aggregate rating'].max() if not recs.empty else 0
        })
    
    return pd.DataFrame(results)

def generate_test_cases():
    """Generate test cases for evaluation"""
    return [
        {'cuisine': 'indian', 'price_bucket': 'Medium', 'top_n': 3},
        {'cuisine': 'italian', 'location': 'Downtown', 'top_n': 5},
        {'price_bucket': 'High', 'top_n': 2},
        {'cuisine': 'japanese', 'location': 'Uptown', 'price_bucket': 'High', 'top_n': 4},
        {'cuisine': 'nonexistent', 'top_n': 3}  # Should return empty
    ]

def user_satisfaction_survey():
    """Simulate user satisfaction survey"""
    # In a real implementation, this would collect actual user feedback
    return {
        'satisfaction_score': 4.2,  # Average on Likert scale 1-5
        'relevance_score': 4.0,     # Average rating of recommendation relevance
        'usability_score': 4.5      # Average rating of interface usability
    }

def generate_evaluation_report():
    """Generate comprehensive evaluation report"""
    test_cases = generate_test_cases()
    evaluation_results = evaluate_recommendations(test_cases)
    user_feedback = user_satisfaction_survey()
    
    report = {
        'test_case_results': evaluation_results,
        'user_feedback': user_feedback,
        'summary': {
            'success_rate': len(evaluation_results[evaluation_results['num_recommendations'] > 0]) / len(evaluation_results),
            'average_rating_across_tests': evaluation_results['average_rating'].mean(),
            'user_satisfaction': user_feedback['satisfaction_score']
        }
    }
    
    return report

if __name__ == "__main__":
    report = generate_evaluation_report()
    print("Evaluation Report:")
    print("\nTest Case Results:")
    print(report['test_case_results'])
    print("\nUser Feedback:")
    print(report['user_feedback'])
    print("\nSummary:")
    print(report['summary'])