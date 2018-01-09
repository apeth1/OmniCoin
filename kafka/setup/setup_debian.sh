#!/usr/bin/env bash
# ***************************
# KAFKA INSTALLATION SCRIPT for Debian/UNIX
# CONFLUENT.IO DISTRIBUTION
# https://docs.confluent.io/current/installation/installing_cp.html#zip-and-tar-archives
# ***************************

echo "Now Installing Confluent Kafka Stack v2.11. . ."
sleep 1

# Install the Confluent public key, which is used to sign the packages in the APT repository.
wget -qO - https://packages.confluent.io/deb/4.0/archive.key | sudo apt-key add -

# Add the repository to your /etc/apt/sources.list:
sudo add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/4.0 stable main"

# Run apt-get update and install Confluent Platform.
sudo apt-get update && sudo apt-get install confluent-platform-oss-2.11