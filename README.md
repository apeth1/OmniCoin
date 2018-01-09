# OmniCoin | With Kafka and Spark + HDFS
Gather live cryptocurrency pricing and financial data in near real time for analysis. 

Publish data to a Kafka topic for ingestion by a consumer and/or the Hadoop File System.

Data is automatically loaded and appended into an SQLite Database for storage. 

Data is collected from CoinMarketCap.com

# Anaconda 3.6 - How To Run
Install Anaconda > 3.6

Create a virtual environment in the OmniCoin
Home Directory:
> conda create --name OmniCoin python=3 pandas numpy

To activate this environment, use:
> source activate OmniCoin

To deactivate an active environment, use:
> source deactivate

Program will run until stopped by the user.

View api.log for API request status codes and information or history.log for SQLite Database operations.

Download an SQLite browser to view price_history.db

# Kafka Setup

# Respect the API
Keep the time.sleep(20) at > 10 seconds. Any lower and your IP address will be banned from CoinMarketCap.com.
