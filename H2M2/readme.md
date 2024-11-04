Garden Fairy
Garden Fairy is an AI-powered plant care assistant that provides expert gardening guidance. Through advanced machine learning, it analyzes plant images and generates professional care recommendations.
Features
Plant Whisperer provides tailored advice on:

Light requirements
Watering schedules
Humidity needs
Temperature preferences
Pruning techniques
Propagation methods

Dependencies

Python 3.12+
Flask
OpenAI API key
Hugging Face account and API token
Key packages: transformers, langchain, pandas, chromadb

Quick Setup

Create and activate a Python virtual environment
Install required packages: pip install -r requirements.txt
Create .env file with your API keys:
CopyOPENAI_API_KEY=your_key
HUGGINGFACEHUB_API_TOKEN=your_token


Running the Application

Start the server: python app.py
Youtube Video Link: https://youtu.be/GEKVFv-oUX4
Open web browser and navigate to http://127.0.0.1:8000/milestone2
Upload a plant image
Select the type of care advice needed
Receive personalized plant care recommendations

Notes

Ensure stable internet connection for API access
First-time setup will download required ML models
Image uploads are temporarily stored in static/imgs folder
