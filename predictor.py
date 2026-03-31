import pandas as pd
import os

def load_data(file_name):
    # Determine the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_name} not found at {file_path}")
        return None


def apply_heuristics(dataframe):
    dataframe['Short_MA'] = dataframe['Close'].rolling(3).mean()
    dataframe['Long_MA'] = dataframe['Close'].rolling(5).mean()
    return dataframe


def make_prediction(dataframe):
    current = dataframe.iloc[-1]
    prev = dataframe.iloc[-2]

    print(f"Current Short MA: {current['Short_MA']:.2f}")
    print(f"Current Long MA: {current['Long_MA']:.2f}")

    if prev['Short_MA'] <= prev['Long_MA'] and current['Short_MA'] > current['Long_MA']:
        return " PREDICTION: GOLDEN CROSS (Bullish Trend Detected! )"
    elif prev['Short_MA'] >= prev['Long_MA'] and current['Short_MA'] < current['Long_MA']:
        return " PREDICTION: DEATH CROSS (Bearish Trend Detected! )"
    else:
        return " PREDICTION: NEUTRAL (No change in trend detected! )"


if __name__ == '__main__':
    data = load_data('stock_data.csv')

    if data is not None:
        print("\n--WELCOME TO STOCK ANALYSER--")
        print("Available STOCKS: TCS, INFY, SBI")
        choice = input("Enter the STOCKS to analyze: ").strip().upper()

        stock_data = data[data['Ticker'] == choice].copy()

        if not stock_data.empty:
            stock_data = apply_heuristics(stock_data)

            if len(stock_data) >= 5:
                print(f"\n--- AI Analysis for {choice} ---")
                prediction = make_prediction(stock_data)
                print(prediction)
            else:
                print(f"Error: Not enough data points for {choice}.")
        else:
            print(f"Error: '{choice}' not found in the Knowledge Base.")