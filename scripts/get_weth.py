from .helpful_scripts import get_account
from brownie import config, network, accounts, interface


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    account = get_account()
    weth = interface.IWeth(config['networks'][network.show_active()]['weth_token'])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    print("Receieve 0.1 WETH!")
    tx.wait(1)
    return tx