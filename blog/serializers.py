from .models import Article,Comments,Like
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username','image']


class CommentSerializer(ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Comments

class LikeSerializer(ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Like

class ArticleSerializer(ModelSerializer):

    class Meta:

        fields = '__all__'
        extra_kwargs = {'author':{'read_only':True}}
        model = Article

        