import requests
import json
import pandas as pd

# Define the Hugging Face API URL
API_URL = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=10"

def fetch_top_models():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def generate_report(models):
    report_data = []
    for model in models:
        report_data.append({
            'Model Name': model['modelId'],
            'Downloads': model['downloads']
        })
    
    df = pd.DataFrame(report_data)
    df.to_csv('top_10_models_report.csv', index=False)
    print("Report generated successfully: top_10_models_report.csv")

if __name__ == "__main__":
    models = fetch_top_models()
    generate_report(models)
