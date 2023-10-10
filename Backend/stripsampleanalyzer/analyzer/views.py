from .serializers import AnalyzerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .tasks import create_task
class AnalyzerView(APIView):
    serializer_class = AnalyzerSerializer

    def post(self, request, format=None):
        serializer = AnalyzerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                create_task.delay(email=request.data.get("email"),image=request.data.get("image").read())
            except:
                return Response( {"msg": "Request unsuccessful. Internal Server Error."}, status=status.HTTP_400_BAD_REQUEST)
            return    Response({"msg": "Request successful!"}, status=status.HTTP_201_CREATED, )
        return Response(
            {"msg": "Request unsuccessful. Invalid data"}, status=status.HTTP_400_BAD_REQUEST)