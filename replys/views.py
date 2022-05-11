from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from .serializers import ReplySerializer
from .models import Reply

@api_view(['GET', 'POST'])
def replys_list(request):

    if request.method == 'GET':
        type_param = request.query_params.get('type')
        replys = Reply.objects.all()
        if type_param:
            replys = replys.filter(comment__type=type_param)
            serializer = ReplySerializer(replys, many=True)
            return Response(serializer.data)
        custom_response_dictionary = {}
        comments = Comment.objects.all()
        for comment in comments:
            replys = Reply.objects.filter(comment_id=comment.id)

            reply_serializer = ReplySerializer(replys, many=True)

            custom_response_dictionary[comment.type] = {
                "": reply_serializer.data
            }
        return Response(custom_response_dictionary)


    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

