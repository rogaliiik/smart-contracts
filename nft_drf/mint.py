from web3 import Web3, middleware
from web3.gas_strategies.time_based import *
from web3.middleware import geth_poa_middleware
import json
import dotenv
import os


def mint(contract_addr, media_url):
    dotenv.load_dotenv('.env')

    # media_url = 'blue_dog.jpeg'
    # contract_addr = '0x1fa10868d42dd97ab10b6b3a68a8ca4adc879e9b'

    w3 = Web3(provider=Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/f88b37d06c188b84b2db686c/eth/rinkeby"))
    from_addr = os.getenv('ADDR')

    ABI = json.load(open('./abi.json'))
    PRIVATE_KEY = os.getenv('METAMASK_KEY')

    contract = w3.eth.contract(Web3.toChecksumAddress(contract_addr), abi=ABI)

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
    w3.middleware_onion.add(middleware.simple_cache_middleware)

    strategy = construct_time_based_gas_price_strategy(10)
    w3.eth.setGasPriceStrategy(strategy)

    def handle_transaction(fn_name, args):
        addr = Web3.toChecksumAddress(from_addr)

        def calculate_nonce():
            return Web3.toHex(w3.eth.getTransactionCount(addr))

        data = contract.encodeABI(fn_name, args=args)
        gas = getattr(contract.functions, fn_name)(*args).estimateGas({'from': addr})
        gasprice = w3.eth.generateGasPrice()

        tr = {'to': contract.address,
              'chainId': 4,
              'from': from_addr,
              'value': Web3.toHex(0),
              'gasPrice': Web3.toHex(gasprice),
              'nonce': calculate_nonce(),
              'data': data,
              'gas': gas,
              }

        signed = w3.eth.account.sign_transaction(tr, PRIVATE_KEY)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        tx_receipt = w3.eth.waitForTransactionReceipt(tx)
        print("TXN RECEIPT: ", tx_receipt)
        return tx

    handle_transaction("mint", [media_url])


if __name__ == '__main__':
    pass
