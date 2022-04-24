from dataclasses import field, fields
from rest_framework import serializers
from .models import Article


# # #  #form serializers
# # # class ArticleSerializers(serializers.Serializer):

# # #     # title =serializers.CharField(max_length=100)
# # #     # author =serializers.CharField(max_length=100)
# # #     # email =serializers.EmailField(max_length=100)
# # #     # date = serializers.DateField()
    
    
# # #     # def create(self, validated_data):
# # #     #     return Article.objects.create(validated_data)
# # #     #     #return super().create(validated_data)        
        
    
# # #     # def update(self, instance, validated_data):
# # #     #     instance.title = validated_data.get('title', instance.title)
# # #     #     instance.author = validated_data.get('author', instance.author)
# # #     #     instance.email = validated_data.get('email', instance.email)
# # #     #     instance.date = validated_data.get('date', instance.date)
# # #     #     instance.save()
        
# # #     #     return instance
# # #     #     #return super().update(instance, validated_data)
    

# # #     #modal Serializers
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id', 'title', 'author', 'email']
        #better way
        fields = '__all__'

