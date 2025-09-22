# Stock Market Prediction using LSTM with Causal Attention – an experiment

## Introduction

`attention-stock-predictor` is a PyTorch-based transformer model designed for experimenting with stock market predictions using multi-stock OHLCV data. Although it does **not reliably predict next-day returns**, it showcases advanced techniques like probability distribution modeling, Wasserstein loss, and allocation-based evaluation—highlighting technical depth in applying modern deep learning to financial time series.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Data Pipeline](#data-pipeline)
- [Model Architecture](#model-architecture)
- [Evaluation](#evaluation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SATheinen/stock-lstm-causal-attention.git
cd stock-lstm-causal-attention
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 API Key Setup

To download or update stock data, this project uses the [Alpha Vantage API](https://www.alphavantage.co/). You need to provide your own API key.

1. Register at [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Create a file named `api_key.txt` in the project root
3. Paste your API key into this file

```txt
api_key = "************"
```

**Important:** Do not share this file or include it in version control.

## Usage

1. Create a free [Alpha Vantage API key](https://www.alphavantage.co/).
2. Save it in a file named `api_key.txt` in the root directory:

```python
api_key = "YOUR_API_KEY_HERE"
```

3. Run the data collection script:

```bash
python data/get_data.py
```

4. Open and run the model training notebook:

```bash
jupyter notebook model/lstm.ipynb
```

## Features

- Transformer model for multi-stock prediction
- Sequence-to-distribution prediction using triangular probability targets
- Wasserstein loss for training
- Backtesting via allocation-based evaluation
- Custom optimizer with arbitrary momentum scheduling
- Metrics: annualized return, drawdown, Sharpe ratio

## Project Structure

```
.
├── api_key.txt                # User-provided API key for Alpha Vantage
├── data/
│   ├── data_dump/             # Saved OHLCV datasets
│   ├── get_data.py            # Script to fetch stock data
│   ├── stock_names.txt        # List of stocks to fetch
│   └── ...                    # Additional folders (repo versions etc.)
├── model/
│   └── lstm.ipynb             # Main notebook with model training
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Configuration

- API Key: `api_key.txt`
- List of Stocks: `data/stock_names.txt`
- Dataset Path: `data/data_dump/`
- All hyperparameters and training controls are in the notebook.

## Data Pipeline

- Stock data (OHLCV) is downloaded via Alpha Vantage.
- Daily percentage changes are computed.
- Hard classification targets are mapped to triangular distributions.
- A sequence of metrics across all stocks is fed to the model.
- Training occurs in two phases:
  1. On training set for several rounds
  2. Testing on unseen points

## Model Architecture

- Transformer-style encoder
- Inputs: `seq_len` time steps of engineered features
- Outputs: Probability distribution over target outcomes
- Loss: Wasserstein distance between predicted and target distributions
- Custom optimizer: `ArbitraryMomentumSGD`

## Evaluation

- Convert output distributions to stock allocations
- Compute:
  - Daily returns
  - Annualized return
  - Maximum drawdown
  - Sharpe ratio
- Evaluation handled by external post-processing script

## Examples

Visuals and training results can be found in the notebook:
`model/lstm.ipynb`

## Troubleshooting

- **API Errors**: Ensure you are not hitting the Alpha Vantage rate limit.
- **Empty Data**: Check if your stock list is valid in `stock_names.txt`.
- **Slow Training**: MPS acceleration is attempted but falls back to CPU.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.