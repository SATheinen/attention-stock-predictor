
# Stock Market Prediction using LSTM with Causal Attention

This repository contains a deep learning model for predicting stock prices using LSTM with SpatioTemporal Causal Attention, implemented in PyTorch.

---

## 🔧 Project Structure

```
.
├── api_key.txt          # Your personal Alpha Vantage API key (not shared)
├── data/                # Folder containing CSVs with historical stock data
├── model/
│   └── lstm.ipynb       # Core model implementation
├── requirements.txt     # Python package requirements
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SATheinen/stock-lstm-causal-attention.git
cd stock-lstm-causal-attention
```

### 2. Install Dependencies

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

**Important:** Do not share this file or include it in version control (it's ignored via `.gitignore`).

---

## 📊 Dataset

The historical stock data is stored in the `data/` directory as CSV files. You can either use the existing data or update it using the script in the notebook which fetches from Alpha Vantage using your API key.

---

## 🧠 Model Overview

- Implements a custom `SpatioTemporalCausalAttention` module
- Uses multi-head attention on temporal sequences of asset prices
- Trained using historical daily stock data
- Optimized using PyTorch, with flexible architecture for multivariate input

---

## 🙋‍♂️ Contributing

Pull requests and discussions are welcome.

