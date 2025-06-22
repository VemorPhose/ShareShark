# ShareShark: Hybrid Stock Price Prediction

## Overview

ShareShark is a Python-based machine learning project that integrates a standard RNN model with sentiment analysis from sources like Twitter and news articles. The goal is to measure the performance improvement of this hybrid model over a purely RNN-based approach for stock price prediction on a limited set of stocks.

## Features

- RNN-based stock price prediction
- Sentiment analysis integration from social and news data
- Performance comparison between hybrid and pure RNN models

## Setup

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.9.7
- TensorFlow
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Usage

1. Prepare your data sources (stock prices, Twitter posts, news articles).
2. Run the training scripts to build and evaluate the models.
3. Compare the results and visualize performance.

## License

MIT License

---

*This project is for research and educational purposes only.*
