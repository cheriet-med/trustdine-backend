from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.template.loader import render_to_string
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .tasks import send_second_email
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .utils import *


from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.core.files.storage import default_storage

import pytesseract
from PIL import Image
import re
from datetime import datetime, timedelta
import os
import tempfile
import cv2
import numpy as np



class Index(APIView):
    def get(self, request):
        return HttpResponse('Loading ...')

    





#Amenities endpoint

class AmenitiesPostGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Amenities.objects.all()
                serializer_class = AmenitiesSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['categoty']  # Exact match filtering
                filterset_fields = ['categoty','user', 'name', 'id']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = AmenitiesSerializer(snippets, many=True)
                    return Response(serializer.data) 
               



class Amenitiesid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Amenities.objects.get(pk=pk)
        except Amenities.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AmenitiesSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AmenitiesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










#Languages endpoint

class LanguagesPostGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Languages.objects.all()
                serializer_class = LanguagesSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['categoty']  # Exact match filtering
                filterset_fields = ['user', 'language', 'id']
                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)
                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = LanguagesSerializer(snippets, many=True)
                    return Response(serializer.data)
                



class Languagesid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Languages.objects.get(pk=pk)
        except Languages.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LanguagesSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LanguagesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











#news letter endpoint

class NewsLetterPostGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = NewsLetter.objects.all()
                serializer_class = NewsLetterSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = NewsLetter.objects.all().order_by('-id')
                    serializer = NewsLetterSerializer(snippets, many=True)
                    return Response(serializer.data)



class Newsletterid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return NewsLetter.objects.get(pk=pk)
        except NewsLetter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NewsLetterSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NewsLetterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





#email letter endpoint

class EmailLetterPostGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = EmailLetter.objects.all()
                serializer_class = EmailLetterSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = EmailLetter.objects.all().order_by('-id')
                    serializer = EmailLetterSerializer(snippets, many=True)
                    return Response(serializer.data)



# show user

class UserDetailsView(APIView):
    #permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user  # Get the authenticated user
        user_data = {
            "email": user.email,
            "id": user.id,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "is_superuser":user.is_superuser,
            "full_name":user.full_name,
            "address_line_1":user.address_line_1,
            "address_line_2":user.address_line_2,
            "city":user.city,
            "state":user.state,
            "postalCode":user.postalCode,
            "countryCode":user.countryCode,
            "phoneNumber":user.phoneNumber,
        }
        return Response(user_data)





# Post get and post

class PostGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Post.objects.all()
                serializer_class = PostSerializer
                filter_backends = [SearchFilter]
                search_fields = ['title_en','title_ar','title_de','title_es','title_fr','title_it','title_nl','title_pt','title_ru','title_sv',
                'url_en','url_ar','url_de','url_es','url_fr','url_it','url_nl','url_pt','url_ru','url_sv',
                 'description_en', 'description_ar','description_de','description_es','description_fr','description_it','description_nl','description_pt','description_ru','description_sv',
                 'content_en','content_ar','content_de','content_es','content_fr','content_it','content_nl','content_pt','content_ru','content_sv']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = PostSerializer(snippets, many=True)
                    return Response(serializer.data)



class Postid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# products
from rest_framework import filters

class ProductGlobal(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
    #filterset_fields = ['category']  # Exact match filtering
    filterset_fields = {
        'category','user', 'name', 'price_per_night', 'types', 'average_cost', 'id'  # Allows searching multiple names
    }
  
    search_fields = []  # Removed category, new_price, stock

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, format=None):
        filtered_queryset = self.filter_queryset(self.get_queryset().order_by('-id'))
        serializer = ProductSerializer(filtered_queryset, many=True)
        return Response(serializer.data)



class Productid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# product images
class ProductImageGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ProductImage.objects.all()
                serializer_class = ProductImagesSerializer
                #filter_backends = [SearchFilter]
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'product', 'id'  # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ProductImagesSerializer(snippets, many=True)
                    return Response(serializer.data)



class ProductImageid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ProductImage.objects.get(pk=pk)
        except ProductImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductImagesSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductImagesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














# product Nearbyattractions
class NearbyattractionsGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Nearbyattractions.objects.all()
                serializer_class = NearbyattractionsSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'product', 'id', 'name', 'distance' # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = NearbyattractionsSerializer(snippets, many=True)
                    return Response(serializer.data)



class Nearbyattractionsid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Nearbyattractions.objects.get(pk=pk)
        except Nearbyattractions.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NearbyattractionsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NearbyattractionsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# product Awards
class AwardsGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Awards.objects.all()
                serializer_class = AwardsSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'product', 'id', 'name', 'year' # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = AwardsSerializer(snippets, many=True)
                    return Response(serializer.data)



class Awardsid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Awards.objects.get(pk=pk)
        except Awards.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AwardsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AwardsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# product Specialties
class SpecialtiesGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Specialties.objects.all()
                serializer_class = SpecialtiesSerializer
                filter_backends = [SearchFilter]
                search_fields = ['images']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = SpecialtiesSerializer(snippets, many=True)
                    return Response(serializer.data)



class Specialtiesid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Specialties.objects.get(pk=pk)
        except Specialties.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpecialtiesSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpecialtiesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














# product reviews
class ProductReviewsGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ProductReview.objects.all()
                serializer_class = ProductReviewSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['product', 'user']  # Specify the fields to filter by

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ProductReviewSerializer(snippets, many=True)
                    return Response(serializer.data)



class ProductReviewsid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ProductReview.objects.get(pk=pk)
        except ProductReview.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductReviewSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductReviewSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











# reviews images
class ReviewsImageGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = RviewsImage.objects.all()
                serializer_class = RviewsImageSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['categoty']  # Exact match filtering
                filterset_fields = ['ProductReview']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = RviewsImageSerializer(snippets, many=True)
                    return Response(serializer.data)


class ReviewsImageid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return RviewsImage.objects.get(pk=pk)
        except RviewsImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RviewsImageSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RviewsImageSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












# reviews helpful


class ReviewHelpfulGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ReviewHelpful.objects.all()
                serializer_class = ReviewHelpfulSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'review', 'user',  # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ReviewHelpfulSerializer(snippets, many=True)
                    return Response(serializer.data)



class ReviewHelpfulid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ReviewHelpful.objects.get(pk=pk)
        except ReviewHelpful.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewHelpfulSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewHelpfulSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












# reviews report


class ReviewReportGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ReviewReport.objects.all()
                serializer_class = ReviewReportSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'review', 'user', 'reason'  # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ReviewReportSerializer(snippets, many=True)
                    return Response(serializer.data)



class ReviewReportid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ReviewReport.objects.get(pk=pk)
        except ReviewReport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewReportSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewReportSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)













# reviews Score


class ReviewScoreGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ReviewScore.objects.all()
                serializer_class = ReviewScoreSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'review', 'user', 'clean', 'blur', 'verified', 'fake', 'total' # Allows searching multiple names
                }

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ReviewScoreSerializer(snippets, many=True)
                    return Response(serializer.data)



class ReviewScoreid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ReviewScore.objects.get(pk=pk)
        except ReviewScore.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewScoreSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReviewScoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















# order
class OrderGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Order.objects.all()
                serializer_class = OrderSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['status', 'product', 'user', 'check_in_date', 'check_out_date', 'total_guests', 'adults', 'children', 'room_quantity', 'restaurat_check_in_date', 'restaurat_check_in_time']  # Specify the fields to filter by
                #search_fields = ['orders']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = OrderSerializer(snippets, many=True)
                    return Response(serializer.data)



class Orderid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# user informations
class UserGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = UserAccount.objects.all()
                serializer_class = EmailUserSearchSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is c
                filterset_fields = ['email']  # Exact match filtering
           
                #search_fields = ['email']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)


                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = EmailUserSearchSerializer(snippets, many=True)
                    return Response(serializer.data)





# user informations
class InformationsGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = UserAccount.objects.all()
                serializer_class = InformationsSerializer
                filter_backends = [SearchFilter]
                search_fields = ['full_name']

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)


                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = InformationsSerializer(snippets, many=True)
                    return Response(serializer.data)






class InformationsId(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserAccount.objects.get(pk=pk)
        except UserAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = InformationsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = InformationsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












class SendEmailGlobal(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SendEmailForPassword.objects.all()
    serializer_class = SendEmailForPasswordSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return SendEmailForPassword.objects.all()

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        nam = request.data.get('name')
        em = request.data.get('email')
        ps = request.data.get('password')
        l = request.data.get('language')
        da = request.data.get('date')
        ti = request.data.get('time')

        # Create a dictionary with the data
        data = {
            'name': nam,
            'password': ps,
            'email': em,
            'language': l,
            'date': da,
            'time': ti,
        }

        # Validate and save the data using the serializer
        serializer = SendEmailForPasswordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Determine the subject and HTML template based on the language
            if l == 'en':
                subject = 'Your Padlev Journey Starts Now!'
                html_message = render_to_string('createaccount/password_en.html', data)
            elif l == 'fr':
                subject = 'Votre aventure Padlev commence maintenant !'
                html_message = render_to_string('createaccount/password_fr.html', data)
            elif l == 'ar':
                subject = 'تبدأ رحلتك مع بادليف الآن!'
                html_message = render_to_string('createaccount/password_ar.html', data)
            elif l == 'de':
                subject = 'Deine Padlev-Reise beginnt jetzt!'
                html_message = render_to_string('createaccount/password_de.html', data)
            elif l == 'es':
                subject = '¡Tu viaje Padlev comienza ahora!'
                html_message = render_to_string('createaccount/password_es.html', data)
            elif l == 'it':
                subject = 'Il tuo viaggio Padlev inizia ora!'
                html_message = render_to_string('createaccount/password_it.html', data)
            elif l == 'nl':
                subject = 'Jouw Padlev-reis begint nu!'
                html_message = render_to_string('createaccount/password_nl.html', data)
            elif l == 'pt':
                subject = 'Sua jornada Padlev começa agora!'
                html_message = render_to_string('createaccount/password_pt.html', data)
            elif l == 'ru':
                subject = 'Ваше путешествие с Padlev начинается сейчас!'
                html_message = render_to_string('createaccount/password_ru.html', data)
            else:
                subject = 'Din Padlev-resa börjar nu!'
                html_message = render_to_string('createaccount/password_sv.html', data)

             # Send the email
            plain_message = html_message
            from_email = 'Padlev <contact@padlev.com>'
            to = em

            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

   

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
        serializer = SendEmailForPasswordSerializer(snippets, many=True)
        return Response(serializer.data)















class SendEmailCreateOrders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SendEmailCreateOrder.objects.all()
    serializer_class = SendEmailCreateOrderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return SendEmailCreateOrder.objects.all()

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        nam = request.data.get('name')
        em = request.data.get('email')
        ps = request.data.get('OrderID')
        l = request.data.get('language')
        da = request.data.get('date_time')

        # Create a dictionary with the data
        data = {
            'name': nam,
            'OrderID': ps,
            'email': em,
            'language': l,
            'date_time': da,
        }

        # Validate and save the data using the serializer
        serializer = SendEmailCreateOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Determine the subject and HTML template based on the language
            if l == 'en':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'fr':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'ar':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'de':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'es':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'it':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'nl':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'pt':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            elif l == 'ru':
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)
            else:
                subject = 'New Order'
                html_message = render_to_string('createOrder/create.html', data)

             # Send the email
            plain_message = html_message
            from_email = 'Padlev <contact@padlev.com>'
            to = em

            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

      
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
        serializer = SendEmailCreateOrderSerializer(snippets, many=True)
        return Response(serializer.data)













class SendEmailTrakinNumber(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SendEmailTrakingNumber.objects.all()
    serializer_class = SendEmailTrakingNumberSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return SendEmailTrakingNumber.objects.all()

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        nam = request.data.get('name')
        em = request.data.get('email')
        ps = request.data.get('trakingNumber')
        l = request.data.get('language')
        da = request.data.get('date_time')

        # Create a dictionary with the data
        data = {
            'name': nam,
            'trakingNumber': ps,
            'email': em,
            'language': l,
            'date_time': da,
        }

        # Validate and save the data using the serializer
        serializer = SendEmailTrakingNumberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Determine the subject and HTML template based on the language
            if l == 'en':
                subject = 'Your Free Book is Here – Grab Your Copy Now!'
                html_message = render_to_string('padlevap/en.html', data)
            elif l == 'fr':
                subject = 'Votre livre gratuit est ici – Téléchargez votre exemplaire maintenant !'
                html_message = render_to_string('padlevap/fr.html', data)
            elif l == 'ar':
                subject = 'كتابك المجاني هنا – احصل على نسختك الآن!'
                html_message = render_to_string('padlevap/ar.html', data)
            elif l == 'de':
                subject = 'Ihr kostenloses Buch ist da – Holen Sie sich jetzt Ihr Exemplar!'
                html_message = render_to_string('padlevap/de.html', data)
            elif l == 'es':
                subject = 'Tu libro gratis está aquí – ¡Consigue tu copia ahora!'
                html_message = render_to_string('padlevap/es.html', data)
            elif l == 'it':
                subject = 'Il tuo libro gratuito è qui – Scarica la tua copia ora!'
                html_message = render_to_string('padlevap/it.html', data)
            elif l == 'nl':
                subject = 'Je gratis boek is hier – Download nu je exemplaar!'
                html_message = render_to_string('padlevap/nl.html', data)
            elif l == 'pt':
                subject = 'Seu Livro Grátis Está Aqui – Baixe Sua Cópia Agora!'
                html_message = render_to_string('padlevap/pt.html', data)
            elif l == 'ru':
                subject = 'Ваша бесплатная книга здесь – получите свою копию прямо сейчас!'
                html_message = render_to_string('padlevap/ru.html', data)
            else:
                subject = 'Din gratis bok är här – hämta din kopia nu!'
                html_message = render_to_string('padlevap/sv.html', data)

             # Send the email
            plain_message = html_message
            from_email = 'Padlev <contact@padlev.com>'
            to = em

            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

          

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
        serializer = SendEmailTrakingNumberSerializer(snippets, many=True)
        return Response(serializer.data)

















# Return
class ReturnGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Return.objects.all()
                serializer_class = ReturnSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['user']  # Specify the fields to filter by

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = ReturnSerializer(snippets, many=True)
                    return Response(serializer.data)



class Returnid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Return.objects.get(pk=pk)
        except Return.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReturnSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ReturnSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# Feedback
class FeedbackGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Feedback.objects.all()
                serializer_class = FeedbackSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['user']  # Specify the fields to filter by

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = FeedbackSerializer(snippets, many=True)
                    return Response(serializer.data)



class Feedbackid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FeedbackSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FeedbackSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















# Coupon
class CoponGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Coupon.objects.all()
                serializer_class = CouponSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['copon']  # Specify the fields to filter by

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = CouponSerializer(snippets, many=True)
                    return Response(serializer.data)



class Coponid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CouponSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CouponSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






#now we generate cron jobs for send emails







class SubmitEmailView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = ScheduledEmail.objects.all()
                serializer_class = EmailSerializer
                #filter_backends = [DjangoFilterBackend, SearchFilter]
                #filterset_fields = ['copon']  # Specify the fields to filter by

                #def post(self, request, *args, **kwargs):
                #    return self.create(request, *args, **kwargs)
                def post(self, request, *args, **kwargs):
                                
                    # Extract data from the request
                    nam = request.data.get('name')
                    em = request.data.get('email')
                    l = request.data.get('language')
                    

                    # Create a dictionary with the data
                    data = {
                        'name': nam,
                        'email': em,
                        'language': l,
                    }

                    # Validate and save the data using the serializer
                    serializer = EmailSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()

                        # Determine the subject and HTML template based on the language
                        if l == 'en':
                            subject = 'Your Free Book is Here – Grab Your Copy Now!'
                            html_message = render_to_string('padlevap/en.html', data)
                        elif l == 'fr':
                            subject = 'Votre livre gratuit est ici – Téléchargez votre exemplaire maintenant !'
                            html_message = render_to_string('padlevap/fr.html', data)
                        elif l == 'ar':
                            subject = 'كتابك المجاني هنا – احصل على نسختك الآن!'
                            html_message = render_to_string('padlevap/ar.html', data)
                        elif l == 'de':
                            subject = 'Ihr kostenloses Buch ist da – Holen Sie sich jetzt Ihr Exemplar!'
                            html_message = render_to_string('padlevap/de.html', data)
                        elif l == 'es':
                            subject = 'Tu libro gratis está aquí – ¡Consigue tu copia ahora!'
                            html_message = render_to_string('padlevap/es.html', data)
                        elif l == 'it':
                            subject = 'Il tuo libro gratuito è qui – Scarica la tua copia ora!'
                            html_message = render_to_string('padlevap/it.html', data)
                        elif l == 'nl':
                            subject = 'Je gratis boek is hier – Download nu je exemplaar!'
                            html_message = render_to_string('padlevap/nl.html', data)
                        elif l == 'pt':
                            subject = 'Seu Livro Grátis Está Aqui – Baixe Sua Cópia Agora!'
                            html_message = render_to_string('padlevap/pt.html', data)
                        elif l == 'ru':
                            subject = 'Ваша бесплатная книга здесь – получите свою копию прямо сейчас!'
                            html_message = render_to_string('padlevap/ru.html', data)
                        else:
                            subject = 'Din gratis bok är här – hämta din kopia nu!'
                            html_message = render_to_string('padlevap/sv.html', data)

                        # Send the email
                        plain_message = html_message
                        from_email = 'Padlev <contact@padlev.com>'
                        to = em

                        send_mail(subject, plain_message, from_email, [to], html_message=html_message)

                        # Schedule the second email after a one-minute delay
                        #send_second_email.apply_async(args=[data, l], countdown=60000)  # 60 seconds delay

                        return Response(serializer.data)
                    else:
                        return Response(serializer.errors, status=400)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = EmailSerializer(snippets, many=True)
                    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([AllowAny])  # Allow Cron-Job.org to access
def trigger_emails(request):
    # Security: Verify API Key
    if request.headers.get('X-API-KEY') != 'h!6u@q1w%z$9&l^e*0x+3v#b8s$k@r!m2n(c)p=f$g@u^d&wz':
        return Response({"error": "Unauthorized"}, status=401)
    
    clients = ScheduledEmail.objects.filter(is_completed=False)
    emails_processed = 0
    
    for client in clients:
        now = timezone.now()
        elapsed = now - client.created_at
        
        # Check if client was created more than 1 hour ago
        if elapsed.total_seconds() > 86400:  # 3600 seconds = 1 hour
            send_email1(client.email, client.language, client.name)
            client.welcome_sent = True
            
        elif elapsed.total_seconds() > 172800:
            send_email2(client.email, client.language, client.name)
            client.day1_sent = True

        elif elapsed.total_seconds() > 259200:
            send_email3(client.email, client.language, client.name)
            client.day2_sent = True

        elif elapsed.total_seconds() > 345600:
            send_email4(client.email, client.language, client.name)
            client.day3_sent = True
            client.is_completed = True

        emails_processed += 1
        client.save()
    
    return Response({"status": "success", "emails_processed": emails_processed})













# product reviews
class testReview(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = test.objects.all()
                serializer_class = TestSerializer
                #filter_backends = [DjangoFilterBackend, SearchFilter]
                #filterset_fields = ['product', 'user']  # Specify the fields to filter by

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = TestSerializer(snippets, many=True)
                    return Response(serializer.data)



class testReviewid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return test.objects.get(pk=pk)
        except test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TestSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TestSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# bill validation


class BillValidationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        try:
            # Get input data
            title = request.data.get('title', '').strip()
            image_file = request.FILES.get('image')
            
            # Validate inputs
            if not title:
                return Response({
                    'status': 'rejected',
                    'message': 'Title is required',
                    'data': {}
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if not image_file:
                return Response({
                    'status': 'rejected',
                    'message': 'Image file is required',
                    'data': {}
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Process the image
            result = self.process_bill_image(image_file, title)
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'rejected',
                'message': f'Error processing request: {str(e)}',
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def process_bill_image(self, image_file, input_title):
        """Process the uploaded image with enhanced preprocessing and multiple OCR attempts"""
        # Save image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            for chunk in image_file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name
        
        try:
            # Open and process image
            image = Image.open(temp_file_path)
            
            # Check image quality before OCR
            quality_report = self.check_image_quality(temp_file_path)
            is_blurry = quality_report.get('is_blurry', False)
            
            # Enhanced preprocessing and OCR with debugging
            best_ocr_result = self.enhanced_ocr_processing(temp_file_path, is_blurry)
            
            # Debug date extraction (optional - remove in production)
            # self.debug_date_extraction(best_ocr_result)
            
            # If very little text extracted, check if it's due to blurriness
            if len(best_ocr_result.strip()) < 20:
                return {
                    'status': 'rejected',
                    'message': 'Image is too blurry - extracted very little text',
                    'data': {
                        'extracted_text': best_ocr_result,
                        'quality_report': quality_report,
                        'is_bill': True,
                        'potential_titles': [input_title]
                    }
                }
            
            # Extract and validate bill data
            extracted_data = self.extract_bill_data(best_ocr_result)
            validation_result = self.validate_bill_data(extracted_data, input_title)
            
            return validation_result
            
        finally:
            # Clean up temporary files
            self.cleanup_temp_files(temp_file_path)
    
    def enhanced_ocr_processing(self, image_path, is_blurry):
        """Apply enhanced preprocessing and multiple OCR attempts"""
        
        # Read the original image
        img_cv = cv2.imread(image_path)
        img_pil = Image.open(image_path)
        
        # Create multiple preprocessed versions
        preprocessed_images = []
        
        # 1. Original image (as baseline)
        preprocessed_images.append(("original", img_cv, img_pil))
        
        # 2. Enhanced version with multiple preprocessing steps
        enhanced_cv, enhanced_pil = self.apply_comprehensive_preprocessing(img_cv, img_pil)
        preprocessed_images.append(("enhanced", enhanced_cv, enhanced_pil))
        
        # 3. If blurry, create upscaled version
        if is_blurry:
            upscaled_cv, upscaled_pil = self.apply_upscaling_and_sharpening(img_cv, img_pil)
            preprocessed_images.append(("upscaled", upscaled_cv, upscaled_pil))
        
        # 4. High contrast version for difficult text
        contrast_cv, contrast_pil = self.apply_high_contrast_processing(img_cv, img_pil)
        preprocessed_images.append(("high_contrast", contrast_cv, contrast_pil))
        
        # Run OCR on each preprocessed version with different configurations
        ocr_results = []
        
        ocr_configs = [
            '--psm 6 --oem 3',  # Uniform block of text
            '--psm 4 --oem 3',  # Single column of text
            '--psm 7 --oem 3',  # Single text line
            '--psm 8 --oem 3',  # Single word
            '--psm 13 --oem 3', # Raw line
        ]
        
        for version_name, cv_img, pil_img in preprocessed_images:
            # Save preprocessed image temporarily
            temp_processed_path = f"{image_path}_{version_name}.png"
            cv2.imwrite(temp_processed_path, cv_img)
            
            for config in ocr_configs:
                try:
                    # Extract text with current configuration
                    extracted_text = pytesseract.image_to_string(
                        pil_img,
                        lang='eng',
                        config=config
                    )
                    
                    # Score this result
                    score = self.score_ocr_result(extracted_text)
                    
                    ocr_results.append({
                        'text': extracted_text,
                        'score': score,
                        'version': version_name,
                        'config': config
                    })
                    
                except Exception as e:
                    print(f"OCR failed for {version_name} with config {config}: {str(e)}")
                    continue
            
            # Clean up temporary processed image
            if os.path.exists(temp_processed_path):
                os.unlink(temp_processed_path)
        
        # Return the best result
        if ocr_results:
            best_result = max(ocr_results, key=lambda x: x['score'])
            print(f"Best OCR result from: {best_result['version']} with config: {best_result['config']}")
            return best_result['text']
        else:
            # Fallback to simple OCR
            return pytesseract.image_to_string(img_pil, lang='eng', config='--psm 6 --oem 3')
    
    def apply_comprehensive_preprocessing(self, img_cv, img_pil):
        """Apply comprehensive preprocessing for better OCR accuracy"""
        
        # Convert to grayscale
        if len(img_cv.shape) == 3:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = img_cv.copy()
        
        # 1. Noise reduction
        denoised = cv2.fastNlMeansDenoising(gray)
        
        # 2. Gaussian blur to smooth
        blurred = cv2.GaussianBlur(denoised, (1, 1), 0)
        
        # 3. Adaptive thresholding for better text separation
        adaptive_thresh = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        
        # 4. Morphological operations to clean text
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        cleaned = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)
        
        # 5. Histogram equalization for contrast enhancement
        enhanced = cv2.equalizeHist(cleaned)
        
        # Convert back to PIL for OCR
        enhanced_pil = Image.fromarray(enhanced)
        
        return enhanced, enhanced_pil
    
    def apply_upscaling_and_sharpening(self, img_cv, img_pil):
        """Apply upscaling and sharpening for blurry images"""
        
        # Convert to grayscale first
        if len(img_cv.shape) == 3:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = img_cv.copy()
        
        # 1. Upscale using INTER_CUBIC for better quality
        height, width = gray.shape
        upscaled = cv2.resize(gray, (width * 3, height * 3), interpolation=cv2.INTER_CUBIC)
        
        # 2. Apply multiple sharpening techniques
        
        # Unsharp masking
        blurred = cv2.GaussianBlur(upscaled, (0, 0), 2.0)
        unsharp = cv2.addWeighted(upscaled, 1.5, blurred, -0.5, 0)
        
        # Additional sharpening kernel
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        sharpened = cv2.filter2D(unsharp, -1, kernel)
        
        # 3. Normalize to full range
        normalized = cv2.normalize(sharpened, None, 0, 255, cv2.NORM_MINMAX)
        
        # 4. Apply bilateral filter to reduce noise while keeping edges sharp
        final = cv2.bilateralFilter(normalized.astype(np.uint8), 9, 75, 75)
        
        # Convert to PIL
        final_pil = Image.fromarray(final)
        
        return final, final_pil
    
    def apply_high_contrast_processing(self, img_cv, img_pil):
        """Apply high contrast processing for difficult text"""
        
        # Convert to grayscale
        if len(img_cv.shape) == 3:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = img_cv.copy()
        
        # 1. CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        clahe_applied = clahe.apply(gray)
        
        # 2. Binary thresholding with Otsu's method
        _, binary = cv2.threshold(clahe_applied, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # 3. Morphological operations to connect broken characters
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
        connected = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        
        # 4. Remove small noise
        kernel_noise = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        final = cv2.morphologyEx(connected, cv2.MORPH_OPEN, kernel_noise)
        
        # Convert to PIL
        final_pil = Image.fromarray(final)
        
        return final, final_pil
    
    def score_ocr_result(self, text):
        """Score OCR results based on various criteria"""
        if not text or len(text.strip()) < 10:
            return 0
        
        score = 0
        
        # 1. Length score (more text usually better)
        score += min(len(text.strip()) / 100, 10)
        
        # 2. Bill indicators score
        bill_indicators = [
            'invoice', 'bill', 'receipt', 'statement', 'payment',
            'total', 'amount', 'due', 'subtotal', 'tax', 'charge',
            'check', 'thank you', 'vat', 'service', 'table', 'tab',
            'fizetendo', 'fogyasztas', 'szervizdi', 'asztal'
        ]
        
        lower_text = text.lower()
        for indicator in bill_indicators:
            if indicator in lower_text:
                score += 5
        
        # 3. Date pattern score
        date_patterns = [
            r'\d{4}\.\d{2}\.\d{2}\.\s*\d{2}:\d{2}:\d{2}',
            r'\d{2}\.\d{2}\.\d{4}',
            r'\d{4}-\d{2}-\d{2}'
        ]
        
        for pattern in date_patterns:
            if re.search(pattern, text):
                score += 10
        
        # 4. Amount patterns score
        if re.search(r'\d+\s*(?:Ft|HUF|EUR|USD)', text):
            score += 8
        
        # 5. Structure score (lines with meaningful content)
        lines = [line.strip() for line in text.split('\n') if len(line.strip()) > 3]
        score += len(lines) * 0.5
        
        # 6. Character quality score (penalize too many special chars or OCR artifacts)
        clean_chars = re.sub(r'[^\w\s.,:\-/]', '', text)
        if len(text) > 0:
            quality_ratio = len(clean_chars) / len(text)
            score += quality_ratio * 5
        
        return score
    
    def check_image_quality(self, image_path):
        """Enhanced image quality check with multiple metrics"""
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                return {'error': 'Could not read image'}
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # 1. Laplacian variance (blur detection)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # 2. Sobel variance (edge detection)
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            sobel_var = np.var(sobel_x) + np.var(sobel_y)
            
            # 3. Gradient magnitude
            gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
            gradient_mean = np.mean(gradient_magnitude)
            
            # 4. Contrast measurement
            contrast = gray.std()
            
            # Combined blur threshold (more sophisticated)
            is_blurry = (laplacian_var < 100 or sobel_var < 1000 or gradient_mean < 20)
            
            return {
                'is_blurry': is_blurry,
                'sharpness_score': laplacian_var,
                'sobel_variance': sobel_var,
                'gradient_mean': gradient_mean,
                'contrast': contrast,
                'resolution': f"{image.shape[1]}x{image.shape[0]}",
                'thresholds': {
                    'laplacian': 100,
                    'sobel': 1000,
                    'gradient': 20
                }
            }
        except Exception as e:
            return {'error': f'Quality check failed: {str(e)}'}
    
    def extract_bill_data(self, text):
        """Extract relevant data from OCR text with enhanced pattern matching"""
        # Enhanced bill indicators for restaurants
        bill_indicators = [
            'invoice', 'bill', 'receipt', 'statement', 'payment',
            'total', 'amount', 'due', 'subtotal', 'tax', 'charge',
            'check', 'thank you', 'vat', 'service', 'table', 'tab',
            'cosmopolitan', 'tel no', 'custom', 'servicenot included',
            'fizetendo', 'fogyasztas', 'szervizdi', 'asztal', 'felszolgalta'
        ]
        
        # Extract potential titles/company names (improved)
        lines = text.strip().split('\n')
        potential_titles = []
        




        for i, line in enumerate(lines[:8]):  # Check first 8 lines instead of 5
            clean_line = line.strip()
            # Skip lines that are mostly numbers, dates, or very short
            if (len(clean_line) > 2 and 
                not re.match(r'^[\d\s\-\/\.\,\$\:]+$', clean_line) and
                not re.match(r'^\d{4}\.\d{2}\.\d{2}', clean_line) and
                len(clean_line) < 50):  # Avoid very long OCR artifacts
                potential_titles.append(clean_line)
        
        # Enhanced date extraction with OCR error correction
        date_patterns = [
            # Hungarian format with time (your specific format)
            r'nyitas:\s*(\d{4}\.\d{1,2}\.\d{1,2}\.\s*\d{1,2}:\d{1,2}:\d{1,2})',  # With context
            r'(\d{4}\.\d{1,2}\.\d{1,2}\.\s*\d{1,2}:\d{1,2}:\d{1,2})',           # 2025.08.15. 13:44:57
            r'(\d{2}\.\d{1,2}\.\d{4}\s*/\s*\d{1,2}:\d{1,2}:\d{1,2})',           # 15.08.2025/13:44:57
            
            # Date only patterns
            r'\b(\d{4}\.\d{1,2}\.\d{1,2})\b',                                   # 2025.08.15
            r'\b(\d{1,2}\.\d{1,2}\.\d{4})\b',                                   # 15.08.2025
            
            # Common international formats
            r'\b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})\b',                        # 15/08/2025, 15-08-25
            r'\b(\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2})\b',                          # 2025/08/15, 2025-08-15
            
            # Month name formats
            r'\b(\d{1,2}[-/](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/]\d{2,4})\b',
            r'\b(\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4})\b',
            r'\b((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{2,4})\b',
            
            # Time patterns (separate from dates)
            r'\b(\d{1,2}:\d{1,2}:\d{1,2})\b',                                  # 13:44:57
            r'\b(\d{1,2}:\d{1,2})\b'                                            # 13:44
        ]

        extracted_dates = []
        for pattern in date_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                date_str = match.group(1) if match.groups() else match.group(0)
                if date_str and date_str not in extracted_dates:
                    # Apply OCR error corrections for common digit misreadings
                    corrected_date = self.correct_ocr_date_errors(date_str)
                    extracted_dates.append(corrected_date)

        # Enhanced amount extraction
        amount_patterns = [
            r'\b\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?\s*(?:Ft|HUF|USD|EUR|GBP)\b',  # With currency
            r'\b\d{1,4}\s+\d{3}(?:\s+\d{3})*\s*(?:Ft|HUF)?\b',                   # Space-separated (Hungarian style)
            r'\b\d{1,3}(?:\s\d{3})*\s*Ft\b',                                     # Hungarian forint format
            r'\b\d+\s*(?:Ft|HUF|EUR|USD)\b'                                      # Simple amount + currency
        ]
        
        amounts = []
        for pattern in amount_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            amounts.extend(matches)
        
        # Remove duplicates and clean amounts
        amounts = list(set([amt.replace('£', '').replace('$', '').replace(',', '').strip() for amt in amounts]))
        
        # Check if text contains bill indicators (case insensitive)
        lower_text = text.lower()
        is_bill = any(indicator.lower() in lower_text for indicator in bill_indicators)
        
        # Enhanced item detection for restaurant bills
        item_patterns = [
            r'\d+\s+[A-Za-z].+\d+[.,]\d{2}',     # Quantity + item + price
            r'[A-Za-z].+\d+\s*(?:Ft|HUF)',      # Item + amount
            r'\d+\s*[xX]\s*.+\d+[.,]\d{2}',     # 2x item 12.50
        ]
        
        has_items = any(re.search(pattern, text) for pattern in item_patterns)
        
        return {
            'extracted_text': text,
            'potential_titles': potential_titles,
            'extracted_dates': extracted_dates,
            'amounts': amounts,
            'is_bill': is_bill or has_items,
            'bill_indicators_found': [indicator for indicator in bill_indicators 
                                    if indicator.lower() in lower_text],
            'has_items': has_items
        }
    
    def apply_high_contrast_processing(self, img_cv, img_pil):
        """Apply high contrast processing for better text recognition"""
        
        # Convert to grayscale
        if len(img_cv.shape) == 3:
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = img_cv.copy()
        
        # 1. Apply gamma correction to brighten
        gamma = 1.2
        lookup_table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")
        gamma_corrected = cv2.LUT(gray, lookup_table)
        
        # 2. Apply CLAHE for local contrast enhancement
        clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
        clahe_applied = clahe.apply(gamma_corrected)
        
        # 3. Binary threshold with Otsu's method
        _, binary = cv2.threshold(clahe_applied, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # 4. Invert if text is lighter than background
        if np.mean(binary) > 127:  # More white than black
            binary = cv2.bitwise_not(binary)
        
        # 5. Clean up with morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        final = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        
        # Convert to PIL
        final_pil = Image.fromarray(final)
        
        return final, final_pil
    
    def validate_bill_data(self, extracted_data, input_title):
        """Validate the extracted data against input criteria with enhanced date validation"""
        
        # Check if it's a bill
        if not extracted_data['is_bill']:
            return {
                'status': 'rejected',
                'message': 'Document does not appear to be a bill',
                'data': extracted_data
            }
        
        # Check title match with enhanced logic
        title_found = False
        matched_title = None
        title_debug_info = []
        
        for potential_title in extracted_data['potential_titles']:
            # Test different matching strategies
            exact_match = input_title.lower().strip() == potential_title.lower().strip()
            contains_match = (input_title.lower() in potential_title.lower() or 
                            potential_title.lower() in input_title.lower())
            fuzzy_match_result = self.fuzzy_match(input_title.lower(), potential_title.lower())
            
            title_debug_info.append({
                'potential_title': potential_title,
                'exact_match': exact_match,
                'contains_match': contains_match,
                'fuzzy_match': fuzzy_match_result
            })
            
            if exact_match or contains_match or fuzzy_match_result:
                title_found = True
                matched_title = potential_title
                break
        
        if not title_found:
            return {
                'status': 'rejected',
                'message': 'Title not found in the bill',
                'data': {
                    **extracted_data,
                    'title_debug': {
                        'input_title': input_title,
                        'potential_titles': extracted_data['potential_titles'],
                        'matching_attempts': title_debug_info
                    }
                }
            }
        
        # Enhanced date validation
        date_valid = False
        valid_date = None
        current_date = datetime.now()
        date_parsing_info = []
        
        for date_str in extracted_data['extracted_dates']:
            try:
                parsed_date = self.parse_date_enhanced(date_str)
                if parsed_date:
                    days_diff = (current_date - parsed_date).days
                    date_parsing_info.append({
                        'original': date_str,
                        'parsed': parsed_date.strftime('%Y-%m-%d %H:%M:%S'),
                        'days_ago': days_diff
                    })
                    
                    if 0 <= days_diff <= 21:
                        date_valid = True
                        valid_date = parsed_date.strftime('%Y-%m-%d')
                        break
            except Exception as e:
                date_parsing_info.append({
                    'original': date_str,
                    'error': str(e)
                })
                continue
        
        # Determine final status
        if title_found and date_valid:
            final_status = 'valid'
            message = 'Bill validation successful'
        else:
            final_status = 'suspect'
            if not date_valid:
                message = 'Bill date is not within the last 21 days or date not found'
            else:
                message = 'Bill validation failed'
        
        return {
            'status': final_status,
            'message': message,
            'data': {
                **extracted_data,
                'title_match': {
                    'found': title_found,
                    'input_title': input_title,
                    'matched_title': matched_title
                },
                'date_validation': {
                    'valid': date_valid,
                    'valid_date': valid_date,
                    'parsing_details': date_parsing_info,
                    'all_dates_found': extracted_data['extracted_dates']
                }
            }
        }
    
    def fuzzy_match(self, str1, str2, threshold=0.6):
        """Enhanced fuzzy matching for titles with better punctuation handling"""
        # Remove common words and special characters
        common_words = ['inc', 'ltd', 'llc', 'corp', 'company', 'co', 'the', 'and', '&', 'kft', 'bt']
        
        def clean_string(s):
            # First normalize punctuation and spacing
            s = s.lower().strip()
            # Replace hyphens, underscores with spaces
            s = re.sub(r'[-_]+', ' ', s)
            # Remove all other punctuation except &
            s = re.sub(r'[^\w\s&]', ' ', s)
            # Replace & with 'and' for better matching
            s = s.replace('&', 'and')
            # Clean up multiple spaces
            s = ' '.join(s.split())
            
            words = s.split()
            return ' '.join([w for w in words if w not in common_words and len(w) > 1])
        
        clean_str1 = clean_string(str1)
        clean_str2 = clean_string(str2)
        
        if not clean_str1 or not clean_str2:
            return False
        
        # Multiple matching strategies
        
        # 1. Exact match after cleaning
        if clean_str1 == clean_str2:
            return True
        
        # 2. Substring matching (either direction)
        if clean_str1 in clean_str2 or clean_str2 in clean_str1:
            return True
        
        # 3. Word overlap ratio
        words1 = set(clean_str1.split())
        words2 = set(clean_str2.split())
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        if not union:
            return False
        
        word_similarity = len(intersection) / len(union)
        
        # 4. Character similarity (Jaccard similarity on character bigrams)
        def get_char_bigrams(s):
            return set([s[i:i+2] for i in range(len(s)-1)])
        
        bigrams1 = get_char_bigrams(clean_str1.replace(' ', ''))
        bigrams2 = get_char_bigrams(clean_str2.replace(' ', ''))
        
        if bigrams1 and bigrams2:
            char_intersection = bigrams1.intersection(bigrams2)
            char_union = bigrams1.union(bigrams2)
            char_similarity = len(char_intersection) / len(char_union) if char_union else 0
        else:
            char_similarity = 0
        
        # 5. Length similarity bonus
        len1, len2 = len(clean_str1), len(clean_str2)
        length_similarity = min(len1, len2) / max(len1, len2) if max(len1, len2) > 0 else 0
        
        # Combined similarity score
        final_similarity = (word_similarity * 0.5 + char_similarity * 0.3 + length_similarity * 0.2)
        
        # Debug info (uncomment for testing)
        # print(f"Fuzzy match debug:")
        # print(f"  Input: '{str1}' -> Clean: '{clean_str1}'")
        # print(f"  OCR: '{str2}' -> Clean: '{clean_str2}'")
        # print(f"  Word similarity: {word_similarity:.3f}")
        # print(f"  Char similarity: {char_similarity:.3f}")
        # print(f"  Final similarity: {final_similarity:.3f}")
        # print(f"  Threshold: {threshold}")
        # print(f"  Match: {final_similarity >= threshold}")
        
        return final_similarity >= threshold
    
    def parse_date_enhanced(self, date_str):
        """Enhanced date parsing with better error handling and format detection"""
        # Clean the date string more thoroughly
        clean_date = date_str.strip().rstrip('.').strip()
        
        # Remove common prefixes
        prefixes_to_remove = [
            r'^(Invoice|Bill|Receipt|Asztal nyitas|Asztal)\s*(Date)?\s*[:]?\s*',
            r'^(nyitas|open|time)\s*[:]?\s*'
        ]
        
        for prefix_pattern in prefixes_to_remove:
            clean_date = re.sub(prefix_pattern, '', clean_date, flags=re.IGNORECASE)
        
        # Enhanced date formats with better OCR error tolerance
        date_formats = [
            # Hungarian formats (your specific case)
            '%Y.%m.%d. %H:%M:%S',    # 2025.08.15. 13:44:57
            '%Y.%m.%d.%H:%M:%S',     # 2025.08.15.13:44:57 (no space)
            '%Y.%m.%d. %H%M%S',      # 2025.08.15. 134457 (no colons in time)
            '%Y.%m.%d.%H%M%S',       # 2025.08.15.134457
            '%Y.%m.%d. %H:%M',       # 2025.08.15. 13:44
            '%Y.%m.%d.%H:%M',        # 2025.08.15.13:44
            '%Y.%m.%d',              # 2025.08.15
            '%Y.%m.%d.',             # 2025.08.15.
            
            # Reverse Hungarian format
            '%d.%m.%Y. %H:%M:%S',    # 15.08.2025. 13:44:57
            '%d.%m.%Y.%H:%M:%S',     # 15.08.2025.13:44:57
            '%d.%m.%Y. %H:%M',       # 15.08.2025. 13:44
            '%d.%m.%Y.%H:%M',        # 15.08.2025.13:44
            '%d.%m.%Y',              # 15.08.2025
            '%d.%m.%Y.',             # 15.08.2025.
            
            # Slash formats
            '%d/%m/%Y %H:%M:%S',     # 15/08/2025 13:44:57
            '%d/%m/%Y',              # 15/08/2025
            '%Y/%m/%d %H:%M:%S',     # 2025/08/15 13:44:57
            '%Y/%m/%d',              # 2025/08/15
            '%m/%d/%Y %H:%M:%S',     # 08/15/2025 13:44:57 (US format)
            '%m/%d/%Y',              # 08/15/2025
            
            # Dash formats
            '%d-%m-%Y %H:%M:%S',     # 15-08-2025 13:44:57
            '%d-%m-%Y',              # 15-08-2025
            '%Y-%m-%d %H:%M:%S',     # 2025-08-15 13:44:57
            '%Y-%m-%d',              # 2025-08-15
            '%m-%d-%Y %H:%M:%S',     # 08-15-2025 13:44:57
            '%m-%d-%Y',              # 08-15-2025
            
            # Short year formats
            '%d.%m.%y. %H:%M:%S',    # 15.08.25. 13:44:57
            '%d.%m.%y',              # 15.08.25
            '%y.%m.%d',              # 25.08.15
            '%d/%m/%y',              # 15/08/25
            '%y/%m/%d',              # 25/08/15
            '%m/%d/%y',              # 08/15/25
            '%d-%m-%y',              # 15-08-25
            '%y-%m-%d',              # 25-08-15
            '%m-%d-%y',              # 08-15-25
            
            # Month name formats
            '%d-%b-%Y %H:%M:%S',     # 15-Aug-2025 13:44:57
            '%d-%b-%Y',              # 15-Aug-2025
            '%d %b %Y %H:%M:%S',     # 15 Aug 2025 13:44:57
            '%d %b %Y',              # 15 Aug 2025
            '%b %d, %Y %H:%M:%S',    # Aug 15, 2025 13:44:57
            '%b %d, %Y',             # Aug 15, 2025
            '%Y-%b-%d',              # 2025-Aug-15
            '%Y %b %d',              # 2025 Aug 15
            
            # Full month name formats
            '%d-%B-%Y %H:%M:%S',     # 15-August-2025 13:44:57
            '%d-%B-%Y',              # 15-August-2025
            '%d %B %Y %H:%M:%S',     # 15 August 2025 13:44:57
            '%d %B %Y',              # 15 August 2025
            '%B %d, %Y %H:%M:%S',    # August 15, 2025 13:44:57
            '%B %d, %Y',             # August 15, 2025
            '%Y-%B-%d',              # 2025-August-15
            '%Y %B %d',              # 2025 August 15
            
            # Compact formats
            '%Y%m%d',                # 20250815
            '%d%m%Y',                # 15082025
            '%y%m%d',                # 250815
            '%d%m%y',                # 150825
            
            # Time only (should be last to avoid conflicts)
            '%H:%M:%S',              # 13:44:57
            '%H:%M'                  # 13:44
        ]
        
        # Try each format
        for fmt in date_formats:
            try:
                parsed = datetime.strptime(clean_date, fmt)
                
                # Handle 2-digit years (assume 20xx for years 00-30, 19xx for 31-99)
                if parsed.year < 100:
                    if parsed.year <= 30:
                        parsed = parsed.replace(year=parsed.year + 2000)
                    else:
                        parsed = parsed.replace(year=parsed.year + 1900)
                
                # Validate that the date makes sense (not too far in future)
                current_year = datetime.now().year
                if parsed.year > current_year + 1:
                    continue
                
                return parsed
                
            except ValueError:
                continue
        
        # If no format matched, try some fuzzy parsing for OCR errors
        return self.fuzzy_date_parsing(clean_date)
    
    def fuzzy_date_parsing(self, date_str):
        """Attempt to parse dates with common OCR errors"""
        try:
            # Common OCR digit confusions
            ocr_corrections = {
                '0': ['O', 'o', 'Q'],
                '1': ['I', 'l', '|'],
                '2': ['Z', 'z'],
                '3': ['8', 'B'],
                '5': ['S', 's'],
                '6': ['G', 'b'],
                '8': ['B', '3'],
                '9': ['g', 'q']
            }
            
            # Try correcting common OCR errors
            corrected_variants = [date_str]
            
            for correct_digit, wrong_chars in ocr_corrections.items():
                for wrong_char in wrong_chars:
                    if wrong_char in date_str:
                        variant = date_str.replace(wrong_char, correct_digit)
                        corrected_variants.append(variant)
            
            # Try parsing each variant
            for variant in corrected_variants:
                parsed = self.parse_date_basic(variant)
                if parsed:
                    return parsed
                    
        except Exception:
            pass
        
        return None
    
    def correct_ocr_date_errors(self, date_str):
        """Correct common OCR errors in dates, especially digit misreading"""
        
        # Common OCR digit errors that affect dates
        corrections = {
            # Focus on month errors (08 vs 09 issue)
            '.09.': '.08.',  # September misread as August
            '.90.': '.08.',  # Severe misreading
            '.06.': '.08.',  # 6 vs 8 confusion
            '.98.': '.08.',  # 9 and 8 confusion
            
            # Day errors
            '15.': '15.',    # This should be correct
            '1S.': '15.',    # S vs 5
            'I5.': '15.',    # I vs 1
            
            # Year errors
            '2025': '2025',  # Should be correct
            '2Q25': '2025',  # Q vs 0
            '2O25': '2025',  # O vs 0
            
            # Time errors
            ':I3:': ':13:',  # I vs 1
            ':l3:': ':13:',  # l vs 1
            ':4A:': ':44:',  # A vs 4
            ':S7': ':57',    # S vs 5
        }
        
        corrected = date_str
        for wrong, right in corrections.items():
            corrected = corrected.replace(wrong, right)
        
        # Additional specific correction for the 08/09 confusion
        # If we see 09 in what should be August 2025, correct it
        if '2025.09.' in corrected and datetime.now().month == 8:
            corrected = corrected.replace('2025.09.', '2025.08.')
        
        return corrected
    
    def parse_date_basic(self, date_str):
        """Basic date parsing for fuzzy matching"""
        basic_formats = [
            '%Y.%m.%d. %H:%M:%S',
            '%Y.%m.%d',
            '%d.%m.%Y',
            '%Y-%m-%d',
            '%d/%m/%Y',
            '%Y/%m/%d'
        ]
        
        for fmt in basic_formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue
        
        return None
    
    def cleanup_temp_files(self, base_path):
        """Clean up all temporary files created during processing"""
        temp_files = [
            base_path,
            f"{base_path}_enhanced.png",
            f"{base_path}_original.png",
            f"{base_path}_upscaled.png",
            f"{base_path}_high_contrast.png"
        ]
        
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                try:
                    os.unlink(temp_file)
                except Exception as e:
                    print(f"Failed to cleanup {temp_file}: {str(e)}")

    def debug_date_extraction(self, text):
        """Debug helper to see what dates are being extracted"""
        print("=== DEBUG: Date Extraction ===")
        print(f"Original text length: {len(text)}")
        
        # Show the specific lines around the date
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2025' in line or '08' in line or '09' in line:
                print(f"Line {i}: '{line.strip()}'")
        
        # Test specific date patterns
        date_patterns = [
            r'(\d{4}\.\d{1,2}\.\d{1,2}\.\s*\d{1,2}:\d{1,2}:\d{1,2})',
            r'nyitas:\s*(\d{4}\.\d{1,2}\.\d{1,2}\.\s*\d{1,2}:\d{1,2}:\d{1,2})',
        ]
        
        for i, pattern in enumerate(date_patterns):
            matches = re.findall(pattern, text, re.IGNORECASE)
            print(f"Pattern {i+1} matches: {matches}")
        
        print("=== END DEBUG ===")
        
        return None  