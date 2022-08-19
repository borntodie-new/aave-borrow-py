from scripts.aave_borrow import (
    get_asset_price,
    get_account,
    get_lending_pool,
    approve_erc20,
)

from brownie import config, network


def test_get_asset_price():
    price_feed_address = config['networks'][network.show_active()]['dai_eth_price_feed']
    # Arrange / Action
    asset_price = get_asset_price(price_feed_address)
    # Assert
    assert asset_price > 0


def test_get_lengding_pool():
    # Arrange / Action
    lending_pool = get_lending_pool()
    # Assert
    assert lending_pool is not None


def test_approve_erc20():
    # Arrange
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 10000000000000000
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # Action
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    tx.wait(1)
    # Assert
    assert tx is not None
