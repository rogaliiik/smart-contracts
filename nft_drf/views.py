import os
from web3 import Web3
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import TokenSerializer
from .models import Token, _createHashId
from rest_framework.response import Response
import json


class TokenAPICreate(APIView):
    """Create a new token"""

    def post(self, request):
        unique_hash = _createHashId().decode('utf-8')
        media_url = request.data['media_url']
        owner = request.data['owner']

        contract_address = os.environ['CONTRACT_MINT_ADDRESS']
        provider = os.environ['NODE_PROVIDER_LOCAL']
        with open('ABI.json', 'r') as file:
            contract_abi = json.load(file)

        w3 = Web3(Web3.HTTPProvider(provider))
        myContract = w3.eth.contract(address=contract_address, abi=contract_abi)

        nonce = w3.eth.get_transaction_count(owner)

        txn = myContract.functions.mint(
            owner=owner, uniqueHash=unique_hash, mediaURL=media_url
        ).buildTransaction({
            'chainId': 4,
            'gas': 2000000,
            'maxFeePerGas': 2000000000,
            'maxPriorityFeePerGas': 1000000000,
            'nonce': nonce,
        })
        print(txn)
        PRIVATE_KEY = os.environ['METAMASK_KEY']
        signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print("TXN RECEIPT: ", tx_receipt)

        new_token = Token.objects.create(
            unique_hash=unique_hash,
            media_url=media_url,
            owner=owner,
            tx_hash=Web3.toHex(tx_hash)
        )
        print("Ready")
        return Response({'token': TokenSerializer(new_token).data})


class TokenAPIList(ListAPIView):
    """Show list of all tokens"""
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenAPITotalSupply(APIView):
    """Get total amount of tokens"""

    def get(self, request):
        contract_address = os.environ['CONTRACT_MINT_ADDRESS']
        provider = os.environ['NODE_PROVIDER_LOCAL']
        w3 = Web3(Web3.HTTPProvider(provider))

        with open('ABI.json', 'r') as file:
            contract_abi = json.load(file)
        myContract = w3.eth.contract(address=contract_address, abi=contract_abi)

        name = myContract.functions.name().call()
        symbol = myContract.functions.symbol().call()
        totalSupply = myContract.functions.totalSupply().call()
        return Response({'name': name, 'symbol': symbol, 'result': totalSupply})
