from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Users(APIView):
    """
    Users or create a new user.
    """
    data_list = []

    def get(self, request):
        return Response({"status": "ok", "data": self.data_list}, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data.get("name"):
            items = {"no": len(self.data_list) + 1, "name": request.data.get('name')}
            self.data_list.append(items)
            return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"status": "no"}, status=status.HTTP_400_BAD_REQUEST)
