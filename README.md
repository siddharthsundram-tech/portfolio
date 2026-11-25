# Portfolio Trade Compliance System

## Overview
A Python-based application that validates Buy and Sell orders against predefined portfolio compliance rules before approving trades.

## Features
- Validates trade quantity, price, and action.
- Checks restricted securities.
- Verifies sufficient holdings for Sell orders.
- Checks available cash for Buy orders.
- Monitors maximum position concentration.
- Flags trades requiring manual approval.
- Displays trade decisions and rejection reasons.

## Technology
- Python 3
- Dictionaries and Lists
- Conditional Statements and Loops
- Command-Line Interface (CLI)

## Compliance Decisions
- **Approved:** All compliance checks passed.
- **Rejected:** Trade violates compliance rules.
- **Needs Manual Sign-off:** Position concentration exceeds the permitted limit.

## Portfolio Configuration

| Attribute | Value |
|---|---|
| Portfolio ID | P101 |
| Cash Balance | 500,000 |
| Restricted Securities | Airtel, Coco Cola |
| Maximum Position | 30% |

## How to Run

1. Install Python 3.
2. Save the code as `main.py`.
3. Open the terminal.
4. Execute:

   ```bash
   python main.py
