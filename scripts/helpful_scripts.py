from brownie import accounts, network, config

FORKED_LOCAL_ENVIRONMENTS = ("mainnet-fork-dev", "mainnet-fork")
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ("development", "ganache-local", 'ganache', 'hardhat', 'mainnet-fork')


def get_account(index=None, id=None):
    if index:
        return accounts[0]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None
