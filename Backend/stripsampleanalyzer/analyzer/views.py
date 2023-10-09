from .serializers import AnalyzerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

class AnalyzerView(APIView):
    serializer_class = AnalyzerSerializer

    def post(self, request, format=None):
        serializer = AnalyzerSerializer(data=request.data)
        if serializer.is_valid():
            return    Response({"msg": "Request successful!"}, status=status.HTTP_201_CREATED, )
        return Response(
            {"msg": "Request unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)