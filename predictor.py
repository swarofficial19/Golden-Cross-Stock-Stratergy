import pandas as pd

# 1. DATA INGESTION (Knowledge Base)
import os  # Add this at the very top of your file (Line 1)

def load_data(file_name):
    # This finds the folder where your predictor.py is actually located
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_name)
    
    try:
        return pd.read_csv(full_path)
    except FileNotFoundError:
        print(f"Error: Could not find {file_name} at {full_path}")
        return None

# 2. FEATURE EXTRACTION (Heuristics)
def apply_heuristics(df):
    # On a real dataset, we use 50 and 200. 
    # For your 10-row dataset, we use 3 and 5 to demonstrate the logic.
    df['Short_MA'] = df['Close'].rolling(window=3).mean()
    df['Long_MA'] = df['Close'].rolling(window=5).mean()
    return df

# 3. INFERENCE ENGINE (Decision Logic)
def make_prediction(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    
    print(f"Current Short MA: {latest['Short_MA']:.2f}")
    print(f"Current Long MA: {latest['Long_MA']:.2f}")

    # Golden Cross Logic: Short MA crosses ABOVE Long MA
    if previous['Short_MA'] <= previous['Long_MA'] and latest['Short_MA'] > latest['Long_MA']:
        return "🎯 PREDICTION: GOLDEN CROSS (Bullish Trend Detected!)"
    
    # Death Cross Logic: Short MA crosses BELOW Long MA
    elif previous['Short_MA'] >= previous['Long_MA'] and latest['Short_MA'] < latest['Long_MA']:
        return "⚠️ PREDICTION: DEATH CROSS (Bearish Trend Detected!)"
    
    else:
        return "⚖️ PREDICTION: NEUTRAL (No trend change detected)"

# --- Execution ---
data = load_data('stock_data.csv')
if data is not None:
    data_with_features = apply_heuristics(data)
    # We need at least 5 rows to calculate the Long_MA(5)
    if len(data_with_features) >= 5:
        result = make_prediction(data_with_features)
        print(result)
    else:
        print("Not enough data in Knowledge Base to run inference.")