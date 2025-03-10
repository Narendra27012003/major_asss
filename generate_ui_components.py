import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_ui_components(analysis_data):
    """Generate Angular UI components using LLM."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/v1/ui/generate"  # Update with the correct endpoint

    # Prepare the payload for the API request
    payload = {
        "model": "llama-3.3-70b-versatile",
        "input": {
            "analysis": analysis_data
        }
    }

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    # Send the request to the Groq API
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()  # Assuming the response contains the generated code
    else:
        print(f"Error generating UI components: {response.text}")
        return None

def main():
    # Example analysis data from Milestone 1
    analysis_data = {
        "ui_components": ["Button", "Modal", "Form"],
        "api_endpoints": [
            "GET /api/dashboard",
            "POST /api/lms/leave/apply"
        ]
    }

    # Generate UI components
    generated_components = generate_ui_components(analysis_data)
    
    if generated_components:
        # Logic to create component files goes here
        print("UI components generated successfully.")
    else:
        print("Failed to generate UI components.")

if __name__ == "__main__":
    main()
