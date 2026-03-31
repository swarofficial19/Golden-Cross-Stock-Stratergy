import pandas as pd

# Knowledge Base
import os  

def load_data(file_name):
    # This finds the folder where your predictor.py is actually located
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_name)
    
    try:
        return pd.read_csv(full_path)
    except FileNotFoundError:
        print(f"Error: Could not find {file_name} at {full_path}")
        return None

# FEATURE EXTRACTION 
def apply_heuristics(df):
    
    df['Short_MA'] = df['Close'].rolling(window=3).mean()
    df['Long_MA'] = df['Close'].rolling(window=5).mean()
    return df

# INFERENCE ENGINE 
def make_prediction(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    
    print(f"Current Short MA: {latest['Short_MA']:.2f}")
    print(f"Current Long MA: {latest['Long_MA']:.2f}")

    # Golden Cross logic
    if previous['Short_MA'] <= previous['Long_MA'] and latest['Short_MA'] > latest['Long_MA']:
        return " PREDICTION: GOLDEN CROSS (Bullish Trend Detected!)"
    
    # Death Cross logic
    elif previous['Short_MA'] >= previous['Long_MA'] and latest['Short_MA'] < latest['Long_MA']:
        return " PREDICTION: DEATH CROSS (Bearish Trend Detected!)"
    
    else:
        return " PREDICTION: NEUTRAL (No trend change detected)"

#Execution
full_dataset = load_data('stock_data.csv')

if full_dataset is not None:
    
    print("\n--WELCOME TO STOCK ANALYSER--")
    print("Available STOCKS: TCS, INFY, SBI")
    user_choice = input("Enter the STOCKS to analyze: ").strip().upper()

    # KNOWLEDGE BASE FILTERING
    
    filtered_data = full_dataset[full_dataset['Ticker'] == user_choice].copy()

    if not filtered_data.empty:
        # FEATURE EXTRACTION & INFERENCE
        data_with_features = apply_heuristics(filtered_data)
        
        
        if len(data_with_features) >= 5:
            print(f"\n--- AI Analysis for {user_choice} ---")
            result = make_prediction(data_with_features)
            print(result)
        else:
            print(f"Error: Not enough data points for {user_choice}.")
    else:
        print(f"Error: '{user_choice}' not found in the Knowledge Base.")