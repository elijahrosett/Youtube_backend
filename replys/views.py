from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from .serializers import ReplySerializer
from .models import Reply

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all(request):
    reply = Reply.objects.all()
    serializer = ReplySerializer(reply , many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_replys(request):
    print(
        'Comment ', f"{request.comment.id}")

    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        reply = Reply.objects.filter(comment_id=request.comment.id)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def replys_by_comment(request, pk):
    if request.method == "GET":
        replys = Reply.objects.filter(comment_id=pk)
        serializer = ReplySerializer(replys, many=True)
        return Response(serializer.data)
