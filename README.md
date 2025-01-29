# real-time-stock-pipeline

## Overview
This project implements a real-time data pipeline to stream, process, store, and visualize stock price data using Apache Kafka, Apache Spark, PostgreSQL (or BigQuery), and Streamlit.

## Tech Stack
- **Kafka**: Streaming real-time stock price data
- **Apache Spark**: Processing and transforming the data
- **PostgreSQL / BigQuery**: Storing processed data
- **Python**: For data ingestion and transformation
- **Streamlit**: For real-time dashboard visualization

## Project Structure
```
real-time-stock-pipeline/
│── data_ingestion/            # Kafka producer to fetch stock data
│   ├── kafka_producer.py
│── data_processing/           # Spark processing logic
│   ├── spark_processing.py
│── database/                  # PostgreSQL database setup
│   ├── schema.sql
│── dashboard/                 # Streamlit dashboard for visualization
│   ├── app.py
│── docker-compose.yml         # For running Kafka, Zookeeper, and PostgreSQL
│── README.md
│── requirements.txt
│── .env                       # Environment variables (API keys, DB config)
```

## Setup & Installation

### Prerequisites
Ensure you have the following installed:
- Docker & Docker Compose
- Python 3.8+
- Apache Kafka
- Apache Spark
- PostgreSQL or Google BigQuery

### Step 1: Clone the Repository
```bash
git clone https://github.com/joshbaid/real-time-stock-pipeline.git
cd real-time-stock-pipeline
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Kafka & PostgreSQL
```bash
docker-compose up -d
```

### Step 5: Start Data Ingestion (Kafka Producer)
```bash
python data_ingestion/kafka_producer.py
```

### Step 6: Start Spark Processing
```bash
python data_processing/spark_processing.py
```

### Step 7: Start Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```

## Features
- **Real-time Stock Streaming**: Fetches stock data using an API and streams via Kafka.
- **Real-time Processing**: Uses Apache Spark to clean and transform data.
- **Storage**: Saves processed data in PostgreSQL or BigQuery.
- **Visualization**: Displays real-time stock prices using Streamlit.

## Future Enhancements
- Implement real-time alerting for stock price anomalies.
- Add machine learning models for stock price prediction.