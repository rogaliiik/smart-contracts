import os
import dotenv
from web3 import Web3
import json


NODE_PROVIDER_LOCAL = 'https://speedy-nodes-nyc.moralis.io/f88b37d06c188b84b2db686c/eth/rinkeby'

my_provider = Web3.HTTPProvider(NODE_PROVIDER_LOCAL)
w3 = Web3(my_provider)

METAMASK_KEY = "a6cd7ec077d04875ae6979f7fbc62dd3e1592019081110718886a5a15b68a298"

contract_addr = "0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359"
from_addr = '0xC7470fEb5Cba97862803418A570453558DFdA89d'
ABI = json.load(open('ABI.json'))
nonce = w3.eth.get_transaction_count(from_addr)

contract = w3.eth.contract(contract_addr, abi=ABI)

tx = {'to': contract.address,
      'from': from_addr,
      'chainId': 4,
      'value': Web3.toHex(0),
      'maxFeePerGas': w3.toWei('2', 'gwei'),
      'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
      'nonce': nonce,
      'gas': 70000,
      }

signed = w3.eth.account.sign_transaction(tx, METAMASK_KEY)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)

print(tx_hash)
print(w3.toHex(w3.keccak(signed.rawTransaction)))
