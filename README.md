# Portfolio Trade Order Compliance & Execution Checker

## Overview
A Python application that validates proposed portfolio trades and generates a decision with a reason for each trade.

## Features
- Manual trade entry
- Bulk CSV trade processing
- Restricted security validation
- Buy affordability checks
- Sell holdings validation
- Maximum position concentration check
- Automatic decision and reason generation
- Export results to CSV

## Technologies
- Python 3
- CSV module (built-in)

## Project Files
- `main.py` – Main application
- `trades.csv` – Input trade data
- `trade_results.csv` – Generated results

## How to Run

1. Keep `main.py` and `trades.csv` in the same folder.
2. Run the application:

   ```bash
   python main.py
