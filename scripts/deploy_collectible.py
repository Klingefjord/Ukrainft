#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config

def main():
    dev = accounts.add(config["wallets"]["from_key"])

    # Deploy collectible
    SimpleCollectible.deploy({"from": dev, "gas_price": 60000000000}) #60 gwei
