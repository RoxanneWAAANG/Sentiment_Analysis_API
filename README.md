# Sentiment Analysis Model Deployment
### AIPI.510 Team Assignment9
#### Team Name: RRKing
#### Team Member: Ruoxin(Roxanne) Wang & Ruonan(Reina) Shi

#### Demo URL: http://13.59.129.76:8501

This project is a Sentiment Analysis web application that allows users to enter text and receive a sentiment prediction (positive or negative). The application is powered by a machine learning model trained using Python and scikit-learn, and the front-end is implemented in Streamlit.

## Project Overview
This project aims to deploy an ML model that predicts the sentiment of a given text. Users can interact with the model through a simple web interface deployed on **AWS EC2 cloud platform**.

### Features
- **Sentiment Analysis Model**: Uses Naive Bayes to predict sentiment.
- **Streamlit Front-End**: A quick and easy Python-based interface for prototyping.

## Getting Started
These instructions will help you set up and deploy the application on your local machine or a cloud server.

### Prerequisites
- **Python 3.8+**
- **Streamlit** (for Streamlit front-end)
- **AWS EC2 Instance** (if deploying to the cloud)
- **Conda or virtualenv** for Python package management

### Installation
#### Backend (FastAPI)
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. **Set Up Python Environment**
   ```sh
   conda create -n sentiment-api python=3.12
   conda activate sentiment-api
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Server**
   ```sh
   uvicorn your_api_script:app --host 0.0.0.0 --port 8000
   ```

#### Front-End (Streamlit)
1. **Install Streamlit**
   ```sh
   pip install streamlit
   ```

2. **Run the Streamlit App**
   ```sh
   streamlit run sentiment_app.py --server.address 0.0.0.0
   ```

### Deployment
- **AWS EC2 Instance**: Use an EC2 instance to deploy the backend API.
  - Ensure that the security group allows inbound traffic on ports `8000` and `8501` (for FastAPI and Streamlit, respectively).
  - Use the **External URL** provided by Streamlit to access the application from another computer.

## Usage
- **React Front-End**: Visit `http://13.59.129.76:8000` to access the React interface.
- **Streamlit Front-End**: Visit `http://13.59.129.76:8501` to access the Streamlit interface.
- **API Endpoint**: The API is available at `http://13.59.129.76:8000/predict`. You can make POST requests with JSON data to receive sentiment predictions.

### Example Request (using cURL)
```sh
curl -X POST "http://13.59.129.76:8000/predict" -H "Content-Type: application/json" -d '{"text": "This is a great day!"}'
```

### Example Response
```json
{
  "sentiment": "Positive"
}
```

## Project Structure
```
- sentiment-analysis-app/
  - main.py  # FastAPI code with ML model
  - sentiment_app.py # Streamlit app code
  - README.md       # Project documentation (this file)
```


