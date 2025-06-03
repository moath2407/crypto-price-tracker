# Cryptocurrency Price Tracker

This project contains two versions of a Python script that fetches real-time cryptocurrency prices using the CoinMarketCap API. The script allows users to track the price of a selected coin by symbol (e.g., BTC, ETH), and optionally receive notifications at a specified interval.

## Overview

The tracker utilizes CoinMarketCap's `/v1/cryptocurrency/listings/latest` endpoint to retrieve up-to-date pricing information. Users can specify whether they want one-time output or continuous notifications.

## Versions

### 1. Google Colab Version

- Utilizes `IPython.display.Javascript` to trigger browser-based alerts directly in the Google Colab environment.
- Useful for quick demos or educational purposes where browser-based notifications are acceptable.
- Not compatible with standard Python environments outside Colab.

### 2. Standard Python Version

- Fully compatible with any standard Python interpreter (e.g., VS Code, terminal, Jupyter Notebook).
- Replaces browser alerts with terminal-based print notifications on a timed interval.
- Designed to be simple, portable, and easily customizable.

### Prerequisites

- Python 3.x
- `requests` library

#### Dependencies (automatically available in Colab):
- `requests`
- `json`
- `IPython.display`

----------------------------------------------------------------------------------------

# How It Works

CoinMarketCap API Key
   Both versions require a CoinMarketCap API key. You can obtain one for free from:
    https://coinmarketcap.com/api

Replace the placeholder in the script with your actual API key:
'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE'

1. Prompts the user for a cryptocurrency symbol (e.g., BTC).
2. Optionally asks if you'd like real-time notifications (Google Colab alert boxes).
3. Fetches the latest price using CoinMarketCap’s API.
4. Displays the price and time of the last update.


# Example Usage

Enter your coin symbol (BTC, ETH, etc.) BTC
Would you like to implement a notification system (Yes/No)? Yes
How many seconds? 5

 Expected Outcome
As of 2025-06-03T18:05:00.000Z, the price of BTC is $105754.63



-----------------------------------------------------------------------------------------
# How to Use

Run the script and follow the prompts:

	Enter the symbol of the cryptocurrency (e.g., BTC, ETH).
	Choose whether you want to enable notifications.
	If notifications are enabled, specify the interval (in seconds) for repeated updates.

# Files Included

crypto_price_tracker_colab.py – Google Colab version with browser-based notifications.

crypto_price_tracker_standard.py – Standard Python version with terminal notifications.

README.md – Project documentation.


# Notes
	Make sure to adhere to CoinMarketCap’s rate limits based on your API tier.

	The notification system is basic and intended for demonstration or personal use.