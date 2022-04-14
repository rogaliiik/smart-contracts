import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import *
import json
import dotenv
import os


def deploy():
    dotenv.load_dotenv('.env')

    # addr = '0xC7470fEb5Cba97862803418A570453558DFdA89d'
    # PRIVATE_KEY = 'a6cd7ec077d04875ae6979f7fbc62dd3e1592019081110718886a5a15b68a298'
    # NODE_PROVIDER_LOCAL = 'https://speedy-nodes-nyc.moralis.io/f88b37d06c188b84b2db686c/eth/rinkeby'

    addr = os.getenv('ADDR')
    PRIVATE_KEY = os.getenv('METAMASK_KEY')
    NODE_PROVIDER_LOCAL = os.getenv('NODE_PROVIDER_LOCAL')

    abi = json.load(open('./ABI.json'))
    w3 = Web3(Web3.HTTPProvider(NODE_PROVIDER_LOCAL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    contract = w3.eth.contract(abi=abi)

    strategy = construct_time_based_gas_price_strategy(15)
    w3.eth.setGasPriceStrategy(strategy)
    gasprice = w3.eth.generateGasPrice()
    print("gasprice: ", gasprice)

    nonce = Web3.toHex(w3.eth.getTransactionCount(addr))

    tr = {'to': None,
          'chainId': 4,
          'from': addr,
          'value': Web3.toHex(0),
          'gasPrice': Web3.toHex(gasprice),
          'nonce': nonce,
          'gas': 500000,
          }

    signed = w3.eth.account.sign_transaction(tr, PRIVATE_KEY)
    tx = w3.eth.send_raw_transaction(signed.rawTransaction)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx)

    contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    print("Done.")

    return tx_receipt.contractAddress


if __name__ == '__main__':
    print(deploy())
