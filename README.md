FinTech AI: Stock AnalyZer


🤖 Project Overview

This project is a Rule-Based Expert System designed to provide financial decision support. It identifies market trend reversals (Bullish and Bearish) by applying Heuristic-based Inference to historical stock price data.

The system is built as part of the Fundamentals of AIML course at VIT Bhopal University. It demonstrates how raw data can be transformed into actionable "Predictions" through feature engineering and state-based logic.

🧠 AIML Concepts Applied

Knowledge Base: A structured CSV repository (stock_data.csv) containing multi-entity time-series data for TCS, INFY, and SBI.

Data Preprocessing (Feature Extraction): The system reduces market "noise" by calculating Moving Average Heuristics (Short-term vs. Long-term).

Inference Engine: A logic unit that performs Pattern Matching on sequential data points to detect "Crossover" events.

Classification: The AI classifies the current market state into three distinct labels: GOLDEN CROSS (Buy), DEATH CROSS (Sell), or NEUTRAL (Hold).

🛠️ Technical Requirements

To run this project, you need:

Python 3.x

Pandas Library (for data manipulation)

Install the required library using:

Bash
pip install pandas
🚀 Setup & Usage
Clone the Repository:

Bash
git clone <your-repository-link>
Ensure Data Presence:
Verify that stock_data.csv is in the same directory as predictor.py.

Run the Predictor:

Bash
python predictor.py
Interact:
When prompted, enter one of the available tickers: TCS, INFY, or SBI.

📂 File Structure
predictor.py: The main Python script containing the Inference Engine and Filtering Logic.

stock_data.csv: The Knowledge Base containing historical price data.

README.md: Project documentation and setup guide.

💡 Key Features

Dynamic Absolute Pathing: Uses the os module to ensure the Knowledge Base is always accessible regardless of the terminal environment.

Context-Specific Filtering: Allows users to select specific financial entities for targeted analysis.

Validation Check: Includes a safety gate to ensure the Knowledge Base has sufficient data before attempting inference.



Description: Documented AIML concepts, technical requirements, and usage instructions to meet BYOP evaluation criteria.

🧪 Execution & Testing Details

The system was rigorously tested against three distinct "Knowledge Base" scenarios to verify the accuracy of the Inference Engine.

1. Test Case: Bullish Reversal (Golden Cross)
Data Input: A 10-day dataset where the 3-day Short MA starts below the 5-day Long MA but spikes on the final day.

Expected Output: 🎯 PREDICTION: GOLDEN CROSS (Bullish Trend Detected!)

Actual Result: Pass

2. Test Case: Bearish Reversal (Death Cross)
Data Input: A dataset where a high-valued stock (TCS) suffers a sharp 30% drop on the final day.

Expected Output: ⚠️ PREDICTION: DEATH CROSS (Bearish Trend Detected!)

Actual Result: Pass

3. Test Case: Stable Market (Neutral)
Data Input: A dataset for SBI showing a steady 1% daily growth without any sudden spikes or drops.

Expected Output: ⚖️ PREDICTION: NEUTRAL (No trend change detected)

Actual Result: Pass

🛠️ Step-by-Step Execution Guide

Follow these steps to replicate the results:

Environment Setup: Ensure Python 3.10+ and pandas are installed.

Ticker Selection: Run python predictor.py. The console will display a menu of available tickers from the Knowledge Base.

Entity Filtering: Type TCS, INFY, or SBI (case-insensitive).

Inference: The system will immediately calculate the heuristics for that specific entity and output the prediction based on the most recent data point.
