# OmniCoin
Gather live cryptocurrency pricing and financial data in near real time for analysis. Data is automatically loaded and appended
into an SQLite Database. Data is collected from CoinMarketCap.com

# How to Use
1. git clone <url>
2. Execute command 'python omni_coin.py'
3. Program will run until stopped by the user.
4. View api.log for API request status codes and information or history.log for SQLite Database operations.
5. Download an SQLite browser to view price_history.db

# Warnings
1. Keep the time.sleep(10) at 10 seconds! Any lower and your IP address will be banned from CoinMarketCap.com


