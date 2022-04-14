from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .serializers import TokenSerializer
from .models import Token, _createHashId
from rest_framework.response import Response
from .deploy import deploy
from .mint import mint


class TokenAPICreate(APIView):
    """Create a new token"""
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        unique_hash = _createHashId().decode('utf8'),
        media_url = request.data['media_url'],
        owner = request.data['owner']

        contract_addr = deploy()
        tx_hash = mint(contract_addr, media_url)

        new_token = Token.objects.create(
            unique_hash=unique_hash,
            media_url=media_url,
            owner=owner,
            tx_hash=tx_hash
        )
        return Response({'post': TokenSerializer(new_token).data})


class TokenAPIList(ListAPIView):
    """Show list of all tokens"""
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenAPITotalSupply(APIView):
    """"""
    def get(self, request):
        totalSupply = tx_hash.totalSupply
        return Response({'result': totalSupply})
