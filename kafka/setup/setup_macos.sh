#!/usr/bin/env bash
# ***************************
# KAFKA INSTALLATION SCRIPT for macOS
# CONFLUENT.IO DISTRIBUTION
# ***************************

#Install within your OmniCoin virtual environment:
echo "Installing Kafka by Confluent.io . . ."
sleep 1
brew install librdkafka

echo "Installing X-Code"
xcode-select --install

echo "Installing Kafka into your virtual environment"
pip install confluent-kafka