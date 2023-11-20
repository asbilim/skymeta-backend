from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Article,Comments,Like
from .serializers import ArticleSerializer,CommentSerializer,LikeSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.decorators import action
class ArticleViewset(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser,FormParser]

    @swagger_auto_schema(operation_description="CREATE an article , you need to be an admin")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        return super().create(request, *args, **kwargs)
    


    @swagger_auto_schema(operation_description="GET all articles or CREATE a new article")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="RETRIEVE, UPDATE or DELETE a specific article")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Assuming the serializer handles the saving logic
            return Response({"status": "success", "content": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer  # Replace with your actual Like serializer

    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        like, created = Like.objects.get_or_create(article=article)
        if created:
            return Response({"status": "success", "message": "Like added"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "message": "Like already exists"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def remove_like(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        Like.objects.filter(article=article).delete()
        return Response({"status": "success", "message": "Like removed"}, status=status.HTTP_200_OK)

