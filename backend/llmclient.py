

import os
from google.cloud import aiplatform
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Google Cloud AI Platform (Gemini/PaLM) client
aiplatform.init(project="gen-lang-client-0012873231", location="asia-south1")  # Make sure to use your project ID and location

def call_gemini(prompt: str) -> str:
    # Initialize the Model for Predictions (Note: Use the correct endpoint ID)
    endpoint = "projects/gen-lang-client-0012873231/locations/asia-south1/endpoints/your-endpoint-id"  # Use the correct endpoint

    # Create the client for prediction
    prediction_client = aiplatform.gapic.PredictionServiceClient()

    # Prepare the input for the model (specify input parameters, like `prompt`)
    instance = aiplatform.gapic.Instance(data=[prompt])
    
    # Make the prediction request
    response = prediction_client.predict(endpoint=endpoint, instances=[instance])

    # Return the prediction result (generated text)
    return response.predictions[0]

