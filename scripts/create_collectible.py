#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config

token_uri = "ipfs://QmberWNJ1Y169SKx2NPkM6Pk7hffUEXDFyGe9Zq789zYrV/"

def main():
    dev = accounts.add(config["wallets"]["from_key"])

    print(network.show_active())

    # Get the token ID.
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    token_id = simple_collectible.tokenCounter()

    # Execute the transaction.
    transaction = simple_collectible.createCollectible(token_uri, {"from": dev, "gas_price": 60000000000}) #60 gwei
    transaction.wait(1)

    print(
        "Awesome! You can view your NFT at {}".format(
            "https://opensea.io/assets/{}/{}".format(simple_collectible.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
