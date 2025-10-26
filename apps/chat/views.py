from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from .serializers import MessageSerializer
from .models import Message


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    # Get all messages by chat room id
    def get(self, request):
        try:
            room_id = request.query_params.get('room_id')
            if not room_id:
                raise ValidationError("room_id query parameter is required")

            messages = Message.objects.filter(room__id=room_id).order_by('created_at')
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"Internal server error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
