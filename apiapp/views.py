from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializers

#viewsets
class ArticleViewset(viewsets.ViewSet):
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk = None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk = pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    
    
    def update(self, request, pk = None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


#Generic views
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'
    
    #using basic authentication
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    #using token authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)


class GenericAPIdetails(generics.DestroyAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

#class based views
class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#function based views
@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
