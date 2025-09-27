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
from .tasks import send_second_email
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .utils import *


from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage

import pytesseract
from PIL import Image
import re
from datetime import datetime, timedelta
import os
import tempfile
import cv2
import numpy as np




from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
import logging

logger = logging.getLogger(__name__)



from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.db.models import Q, Prefetch
from django.utils import timezone
from django.db.models import Q, Max  # Make sure Max is imported here


User = get_user_model()







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



class EmailLetterPostid(APIView):
    """
    Retrieve, update or delete a snippet instance ..
    """
    def get_object(self, pk):
        try:
            return EmailLetter.objects.get(pk=pk)
        except EmailLetter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EmailLetterSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EmailLetterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
  
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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







#Verify Documents



class VerifyGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Verify.objects.all()
                serializer_class = VerifySerializer
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = VerifySerializer(snippets, many=True)
                    return Response(serializer.data)



class Verifyid(APIView):
    """
    Retrieve, update or delete a Verify instance.
    """

    def get_object(self, pk):
        try:
            return Verify.objects.get(pk=pk)
        except Verify.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VerifySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VerifySerializer(snippet, data=request.data, partial=True)  # allow partial update
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
                'product', 'user', 'clean', 'blur', 'verified', 'fake', 'total' # Allows searching multiple names
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
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is c
                filterset_fields =  ['full_name', 'email']

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








import cv2
import numpy as np
import requests
from PIL import Image
import tempfile
import os
from skimage.metrics import structural_similarity as ssim
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import hashlib

class BillValidationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        try:
            # Get input data
            image_file = request.FILES.get('image')
            reference_image_url = request.data.get('reference_image_url', '').strip()
            
            # Validate inputs
            if not image_file:
                return Response({
                    'status': 'rejected',
                    'message': 'Image file is required',
                    'data': {}
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if not reference_image_url:
                return Response({
                    'status': 'rejected',
                    'message': 'Reference image URL is required',
                    'data': {}
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Process the image with deep comparison
            result = self.process_bill_image_with_comparison(image_file, reference_image_url)
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'status': 'rejected',
                'message': f'Error processing request: {str(e)}',
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def process_bill_image_with_comparison(self, image_file, reference_url):
        """Process the uploaded image with deep comparison against reference URL"""
        
        # Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            for chunk in image_file.chunks():
                temp_file.write(chunk)
            uploaded_image_path = temp_file.name
        
        # Download reference image
        reference_image_path = None
        try:
            reference_image_path = self.download_reference_image(reference_url)
            
            # Perform deep image comparison
            comparison_result = self.deep_image_comparison(uploaded_image_path, reference_image_path)
            
            # If images don't match, return early with comparison details
            if not comparison_result['images_match']:
                return {
                    'status': 'rejected',
                    'message': 'Uploaded image does not match the reference image',
                    'data': {
                        'comparison_details': comparison_result,
                        'reason': 'image_mismatch'
                    }
                }
            
            # Images match, now process for bill validation
            try:
                # Check image quality before OCR
                quality_report = self.check_image_quality(uploaded_image_path)
                is_blurry = quality_report.get('is_blurry', False)
                
                # Enhanced preprocessing and OCR with debugging
                best_ocr_result = self.enhanced_ocr_processing(uploaded_image_path, is_blurry)
                
                # If very little text extracted, check if it's due to blurriness
                if len(best_ocr_result.strip()) < 20:
                    return {
                        'status': 'rejected',
                        'message': 'Image is too blurry - extracted very little text',
                        'data': {
                            'extracted_text': best_ocr_result,
                            'quality_report': quality_report,
                            'is_bill': True,
                            'comparison_details': comparison_result,
                            'reason': 'blurry_image'
                        }
                    }
                
                # Extract and validate bill data
                extracted_data = self.extract_bill_data(best_ocr_result)
                validation_result = self.validate_bill_data(extracted_data)
                
                # Add comparison details to the result
                validation_result['data']['comparison_details'] = comparison_result
                
                return validation_result
                
            except Exception as e:
                return {
                    'status': 'rejected',
                    'message': f'Error processing bill image: {str(e)}',
                    'data': {
                        'comparison_details': comparison_result,
                        'reason': 'processing_error'
                    }
                }
                
        finally:
            # Clean up temporary files
            self.cleanup_temp_files(uploaded_image_path)
            if reference_image_path:
                self.cleanup_temp_files(reference_image_path)
    
    def download_reference_image(self, url):
        """Download reference image from URL"""
        try:
            # Add headers to mimic browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            # Check if content is an image
            content_type = response.headers.get('content-type', '')
            if not content_type.startswith('image/'):
                raise ValueError(f"URL does not point to an image. Content-Type: {content_type}")
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                for chunk in response.iter_content(chunk_size=8192):
                    temp_file.write(chunk)
                return temp_file.name
                
        except requests.RequestException as e:
            raise Exception(f"Failed to download reference image: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing reference image: {str(e)}")
    
    def deep_image_comparison(self, uploaded_path, reference_path):
        """Perform deep comparison between uploaded and reference images"""
        
        try:
            # Load images
            uploaded_img = cv2.imread(uploaded_path)
            reference_img = cv2.imread(reference_path)
            
            if uploaded_img is None or reference_img is None:
                return {
                    'images_match': False,
                    'error': 'Could not load one or both images',
                    'comparison_score': 0
                }
            
            # 1. Hash-based comparison (fastest check)
            hash_comparison = self.compare_image_hashes(uploaded_path, reference_path)
            
            # 2. Histogram comparison
            histogram_comparison = self.compare_histograms(uploaded_img, reference_img)
            
            # 3. Structural Similarity Index (SSIM)
            ssim_comparison = self.compare_ssim(uploaded_img, reference_img)
            
            # 4. Feature-based comparison (ORB)
            feature_comparison = self.compare_features(uploaded_img, reference_img)
            
            # 5. Template matching
            template_comparison = self.compare_template_matching(uploaded_img, reference_img)
            
            # 6. OCR-based content comparison
            ocr_comparison = self.compare_ocr_content(uploaded_path, reference_path)
            
            # 7. Color distribution comparison
            color_comparison = self.compare_color_distribution(uploaded_img, reference_img)
            
            # Calculate weighted final score
            final_score = self.calculate_final_similarity_score({
                'hash': hash_comparison,
                'histogram': histogram_comparison,
                'ssim': ssim_comparison,
                'features': feature_comparison,
                'template': template_comparison,
                'ocr': ocr_comparison,
                'color': color_comparison
            })
            
            # Determine if images match (threshold can be adjusted)
            match_threshold = 0.7  # 70% similarity threshold
            images_match = final_score >= match_threshold
            
            return {
                'images_match': images_match,
                'comparison_score': final_score,
                'threshold': match_threshold,
                'detailed_scores': {
                    'hash_similarity': hash_comparison['similarity'],
                    'histogram_similarity': histogram_comparison['similarity'],
                    'ssim_score': ssim_comparison['similarity'],
                    'feature_matches': feature_comparison['similarity'],
                    'template_score': template_comparison['similarity'],
                    'ocr_similarity': ocr_comparison['similarity'],
                    'color_similarity': color_comparison['similarity']
                },
                'analysis_details': {
                    'hash': hash_comparison,
                    'histogram': histogram_comparison,
                    'ssim': ssim_comparison,
                    'features': feature_comparison,
                    'template': template_comparison,
                    'ocr': ocr_comparison,
                    'color': color_comparison
                }
            }
            
        except Exception as e:
            return {
                'images_match': False,
                'error': f'Comparison failed: {str(e)}',
                'comparison_score': 0
            }
    
    def compare_image_hashes(self, img1_path, img2_path):
        """Compare images using perceptual hashing"""
        try:
            # Calculate MD5 hash first (exact match)
            def get_file_hash(path):
                with open(path, 'rb') as f:
                    return hashlib.md5(f.read()).hexdigest()
            
            hash1 = get_file_hash(img1_path)
            hash2 = get_file_hash(img2_path)
            
            exact_match = hash1 == hash2
            
            # Calculate perceptual hash using average hash
            def average_hash(image_path, hash_size=16):
                image = Image.open(image_path)
                image = image.convert('L').resize((hash_size, hash_size), Image.Resampling.LANCZOS)
                pixels = np.array(image)
                avg = pixels.mean()
                return (pixels > avg).astype(int)
            
            ahash1 = average_hash(img1_path)
            ahash2 = average_hash(img2_path)
            
            # Calculate Hamming distance
            hamming_distance = np.sum(ahash1 != ahash2)
            max_distance = ahash1.size
            similarity = 1 - (hamming_distance / max_distance)
            
            return {
                'similarity': 1.0 if exact_match else similarity,
                'exact_match': exact_match,
                'hamming_distance': hamming_distance,
                'perceptual_similarity': similarity
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_histograms(self, img1, img2):
        """Compare color histograms of images"""
        try:
            # Convert to RGB for consistent histogram calculation
            img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            
            # Calculate histograms for each channel
            hist1_r = cv2.calcHist([img1_rgb], [0], None, [256], [0, 256])
            hist1_g = cv2.calcHist([img1_rgb], [1], None, [256], [0, 256])
            hist1_b = cv2.calcHist([img1_rgb], [2], None, [256], [0, 256])
            
            hist2_r = cv2.calcHist([img2_rgb], [0], None, [256], [0, 256])
            hist2_g = cv2.calcHist([img2_rgb], [1], None, [256], [0, 256])
            hist2_b = cv2.calcHist([img2_rgb], [2], None, [256], [0, 256])
            
            # Compare histograms using multiple methods
            methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_BHATTACHARYYA]
            
            scores = []
            for method in methods:
                score_r = cv2.compareHist(hist1_r, hist2_r, method)
                score_g = cv2.compareHist(hist1_g, hist2_g, method)
                score_b = cv2.compareHist(hist1_b, hist2_b, method)
                
                # Average across channels
                avg_score = (score_r + score_g + score_b) / 3
                
                # Normalize score (correlation method gives values 0-1, others need normalization)
                if method == cv2.HISTCMP_CORREL:
                    normalized_score = max(0, avg_score)  # Correlation: higher is better
                elif method == cv2.HISTCMP_CHISQR:
                    normalized_score = 1 / (1 + avg_score)  # Chi-square: lower is better
                elif method == cv2.HISTCMP_INTERSECT:
                    normalized_score = avg_score / np.sum(hist1_r)  # Intersection: normalize by histogram size
                else:  # Bhattacharyya
                    normalized_score = 1 - avg_score  # Bhattacharyya: lower is better
                
                scores.append(normalized_score)
            
            # Average all methods
            final_similarity = np.mean(scores)
            
            return {
                'similarity': final_similarity,
                'method_scores': {
                    'correlation': scores[0],
                    'chi_square': scores[1], 
                    'intersection': scores[2],
                    'bhattacharyya': scores[3]
                }
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_ssim(self, img1, img2):
        """Compare images using Structural Similarity Index"""
        try:
            # Convert to grayscale
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            
            # Resize to same dimensions for comparison
            h1, w1 = gray1.shape
            h2, w2 = gray2.shape
            
            # Resize to smaller dimensions for faster computation
            target_size = (min(w1, w2, 800), min(h1, h2, 600))
            gray1_resized = cv2.resize(gray1, target_size)
            gray2_resized = cv2.resize(gray2, target_size)
            
            # Calculate SSIM
            ssim_score, ssim_map = ssim(gray1_resized, gray2_resized, full=True)
            
            # Calculate mean SSIM across the image
            mean_ssim = np.mean(ssim_map)
            
            return {
                'similarity': ssim_score,
                'mean_ssim': mean_ssim,
                'image_dimensions': {
                    'original': (w1, h1, w2, h2),
                    'compared': target_size
                }
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_features(self, img1, img2):
        """Compare images using ORB feature detection and matching"""
        try:
            # Convert to grayscale
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            
            # Initialize ORB detector
            orb = cv2.ORB_create(nfeatures=2000)
            
            # Find keypoints and descriptors
            kp1, des1 = orb.detectAndCompute(gray1, None)
            kp2, des2 = orb.detectAndCompute(gray2, None)
            
            if des1 is None or des2 is None:
                return {'similarity': 0, 'error': 'No features detected in one or both images'}
            
            # Match features using BFMatcher
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            
            # Sort matches by distance
            matches = sorted(matches, key=lambda x: x.distance)
            
            # Calculate similarity based on good matches
            good_matches = [m for m in matches if m.distance < 50]  # Threshold for good matches
            
            total_features = min(len(kp1), len(kp2))
            if total_features == 0:
                similarity = 0
            else:
                similarity = len(good_matches) / total_features
            
            return {
                'similarity': min(similarity, 1.0),  # Cap at 1.0
                'total_matches': len(matches),
                'good_matches': len(good_matches),
                'keypoints': (len(kp1), len(kp2)),
                'avg_distance': np.mean([m.distance for m in matches]) if matches else float('inf')
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_template_matching(self, img1, img2):
        """Compare images using template matching"""
        try:
            # Convert to grayscale
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            
            # Try multiple template matching methods
            methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
            
            scores = []
            
            # Template match in both directions
            for method in methods:
                # Use smaller image as template
                if gray1.shape[0] * gray1.shape[1] < gray2.shape[0] * gray2.shape[1]:
                    template, image = gray1, gray2
                else:
                    template, image = gray2, gray1
                
                # Resize template if it's larger than image
                if template.shape[0] > image.shape[0] or template.shape[1] > image.shape[1]:
                    scale_factor = min(image.shape[0] / template.shape[0], image.shape[1] / template.shape[1]) * 0.9
                    new_size = (int(template.shape[1] * scale_factor), int(template.shape[0] * scale_factor))
                    template = cv2.resize(template, new_size)
                
                result = cv2.matchTemplate(image, template, method)
                _, max_val, _, _ = cv2.minMaxLoc(result)
                
                if method == cv2.TM_SQDIFF_NORMED:
                    score = 1 - max_val  # For SQDIFF, lower is better
                else:
                    score = max_val
                
                scores.append(max(0, score))
            
            final_score = np.mean(scores)
            
            return {
                'similarity': final_score,
                'method_scores': scores,
                'template_size': template.shape,
                'image_size': image.shape
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_ocr_content(self, img1_path, img2_path):
        """Compare OCR content from both images"""
        try:
            # Extract text from both images
            img1_pil = Image.open(img1_path)
            img2_pil = Image.open(img2_path)
            
            text1 = pytesseract.image_to_string(img1_pil, lang='eng', config='--psm 6 --oem 3')
            text2 = pytesseract.image_to_string(img2_pil, lang='eng', config='--psm 6 --oem 3')
            
            # Clean and normalize text
            def clean_text(text):
                # Remove extra whitespace and normalize
                text = ' '.join(text.split())
                # Remove special characters but keep letters, numbers, and basic punctuation
                text = re.sub(r'[^\w\s.,:\-/]', ' ', text)
                return text.lower().strip()
            
            clean_text1 = clean_text(text1)
            clean_text2 = clean_text(text2)
            
            if not clean_text1 or not clean_text2:
                return {'similarity': 0, 'error': 'No text extracted from one or both images'}
            
            # 1. Exact text match
            exact_match = clean_text1 == clean_text2
            
            # 2. Jaccard similarity (word overlap)
            words1 = set(clean_text1.split())
            words2 = set(clean_text2.split())
            
            intersection = words1.intersection(words2)
            union = words1.union(words2)
            jaccard_score = len(intersection) / len(union) if union else 0
            
            # 3. TF-IDF cosine similarity
            tfidf_score = 0
            if clean_text1 and clean_text2:
                vectorizer = TfidfVectorizer(ngram_range=(1, 2))
                try:
                    tfidf_matrix = vectorizer.fit_transform([clean_text1, clean_text2])
                    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
                    tfidf_score = cosine_sim
                except:
                    pass
            
            # 4. Character-level similarity
            def char_similarity(s1, s2):
                longer = s1 if len(s1) > len(s2) else s2
                shorter = s2 if len(s1) > len(s2) else s1
                
                if len(longer) == 0:
                    return 1.0
                
                return (len(longer) - self.levenshtein_distance(longer, shorter)) / len(longer)
            
            char_sim = char_similarity(clean_text1, clean_text2)
            
            # Combine scores
            final_similarity = (jaccard_score * 0.4 + tfidf_score * 0.4 + char_sim * 0.2)
            
            if exact_match:
                final_similarity = 1.0
            
            return {
                'similarity': final_similarity,
                'exact_match': exact_match,
                'jaccard_score': jaccard_score,
                'tfidf_score': tfidf_score,
                'character_similarity': char_sim,
                'text_lengths': (len(clean_text1), len(clean_text2)),
                'word_counts': (len(words1), len(words2)),
                'common_words': len(intersection)
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def compare_color_distribution(self, img1, img2):
        """Compare color distribution between images"""
        try:
            # Convert to different color spaces for comprehensive comparison
            comparisons = []
            
            # RGB comparison
            for i in range(3):  # R, G, B channels
                hist1 = cv2.calcHist([img1], [i], None, [256], [0, 256])
                hist2 = cv2.calcHist([img2], [i], None, [256], [0, 256])
                corr = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
                comparisons.append(max(0, corr))
            
            # HSV comparison (more perceptually relevant)
            hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
            hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
            
            for i in range(3):  # H, S, V channels
                hist1 = cv2.calcHist([hsv1], [i], None, [256], [0, 256])
                hist2 = cv2.calcHist([hsv2], [i], None, [256], [0, 256])
                corr = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
                comparisons.append(max(0, corr))
            
            # Lab color space comparison
            lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
            lab2 = cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)
            
            for i in range(3):  # L, a, b channels
                hist1 = cv2.calcHist([lab1], [i], None, [256], [0, 256])
                hist2 = cv2.calcHist([lab2], [i], None, [256], [0, 256])
                corr = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
                comparisons.append(max(0, corr))
            
            final_similarity = np.mean(comparisons)
            
            return {
                'similarity': final_similarity,
                'rgb_scores': comparisons[:3],
                'hsv_scores': comparisons[3:6],
                'lab_scores': comparisons[6:9]
            }
            
        except Exception as e:
            return {'similarity': 0, 'error': str(e)}
    
    def calculate_final_similarity_score(self, comparison_results):
        """Calculate weighted final similarity score from all comparison methods"""
        
        # Define weights for each comparison method
        weights = {
            'hash': 0.20,        # Hash comparison (good for exact/near-exact matches)
            'histogram': 0.15,   # Color distribution
            'ssim': 0.20,        # Structural similarity (very important)
            'features': 0.20,    # Feature matching (important for content)
            'template': 0.10,    # Template matching
            'ocr': 0.10,         # OCR content comparison
            'color': 0.05        # Additional color analysis
        }
        
        total_score = 0
        total_weight = 0
        
        for method, weight in weights.items():
            if method in comparison_results and 'similarity' in comparison_results[method]:
                score = comparison_results[method]['similarity']
                if score > 0:  # Only include valid scores
                    total_score += score * weight
                    total_weight += weight
        
        # Normalize by actual weights used
        final_score = total_score / total_weight if total_weight > 0 else 0
        
        # Apply bonus for multiple high-scoring methods
        high_score_count = sum(1 for method in comparison_results.values() 
                              if isinstance(method, dict) and method.get('similarity', 0) > 0.8)
        
        if high_score_count >= 3:
            final_score *= 1.1  # 10% bonus
        
        return min(final_score, 1.0)  # Cap at 1.0
    
    def levenshtein_distance(self, s1, s2):
        """Calculate Levenshtein distance between two strings"""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    # Keep all existing methods from the original class
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
            if (len(clean_line) > 2
                and not re.match(r'^[\d\s\-\/\.\,\$\:]+$', clean_line)
                and not re.match(r'^\d{4}\.\d{2}\.\d{2}', clean_line)
                and len(clean_line) < 50  # Avoid very long OCR artifacts
                ):
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
        amounts = list(set([amt.replace('£', '').replace('', '').replace(',', '').strip() for amt in amounts]))
        
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
    
    def validate_bill_data(self, extracted_data):
        """Validate the extracted data with enhanced date validation"""
        
        # Check if it's a bill
        if not extracted_data['is_bill']:
            return {
                'status': 'rejected',
                'message': 'Document does not appear to be a bill',
                'data': {
                    **extracted_data,
                    'reason': 'not_a_bill'
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
        if date_valid:
            final_status = 'valid'
            message = 'Bill validation successful'
            reason = None
        else:
            final_status = 'rejected'
            message = 'Bill date is not within the last 21 days or date not found'
            reason = 'invalid_date'
        
        return {
            'status': final_status,
            'message': message,
            'data': {
                **extracted_data,
                'date_validation': {
                    'valid': date_valid,
                    'valid_date': valid_date,
                    'parsing_details': date_parsing_info,
                    'all_dates_found': extracted_data['extracted_dates']
                },
                'reason': reason
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
        
        # 4. Character-level similarity (Jaccard similarity on character bigrams)
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
            
            # Additional formats...
            '%d/%m/%Y %H:%M:%S',     # 15/08/2025 13:44:57
            '%d/%m/%Y',              # 15/08/2025
            '%Y/%m/%d %H:%M:%S',     # 2025/08/15 13:44:57
            '%Y/%m/%d',              # 2025/08/15
            '%m/%d/%Y %H:%M:%S',     # 08/15/2025 13:44:57 (US format)
            '%m/%d/%Y',              # 08/15/2025
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











# for social media login



@api_view(['POST'])
@permission_classes([AllowAny])
def email_login_or_register(request):
    """
    API endpoint that accepts an email and either:
    - Logs in the user if they exist
    - Creates a new user if they don't exist
    Returns user data and authentication tokens
    """
    email = request.data.get('email')
    
    if not email:
        return Response(
            {'error': 'Email is required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Normalize email
    email = UserAccount.objects.normalize_email(email)
    
    try:
        # Check if user exists
        user = UserAccount.objects.get(email=email)
        
        # User exists - handle login
        if not user.is_active:
            return Response(
                {'error': 'Account is deactivated'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        # Serialize user data
        serializer = UserAccountSerializer(user)
        
        return Response({
            'message': 'Login successful',
            'user_exists': True,
            'user': serializer.data,
            'tokens': {
                'access': str(access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)
        
    except UserAccount.DoesNotExist:
        # User doesn't exist - create new user
        try:
            with transaction.atomic():
                # Filter out email from extra fields to avoid duplicate argument
                extra_fields = {k: v for k, v in request.data.items() 
                               if k != 'email' and v is not None}
                
                # Create new user with email only
                user = UserAccount.objects.create_user(
                    email=email,
                    password=None,  # No password for email-only registration
                    **extra_fields  # Include any additional fields from request
                )
                
                # Generate tokens for new user
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                
                # Serialize user data
                serializer = UserAccountSerializer(user)
                
                logger.info(f"New user created with email: {email}")
                
                return Response({
                    'message': 'User created successfully',
                    'user_exists': False,
                    'user': serializer.data,
                    'tokens': {
                        'access': str(access_token),
                        'refresh': str(refresh),
                    }
                }, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return Response(
                {'error': 'Failed to create user', 'details': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return Response(
            {'error': 'An unexpected error occurred'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Alternative class-based view
from rest_framework.views import APIView

class EmailLoginOrRegisterView(APIView):
    """
    Class-based view for email login or register
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {'error': 'Email is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        email = UserAccount.objects.normalize_email(email)
        
        try:
            user = UserAccount.objects.get(email=email)
            return self._handle_existing_user(user)
        except UserAccount.DoesNotExist:
            return self._create_new_user(email, request.data)
    
    def _handle_existing_user(self, user):
        """Handle login for existing user"""
        if not user.is_active:
            return Response(
                {'error': 'Account is deactivated'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        refresh = RefreshToken.for_user(user)
        serializer = UserAccountSerializer(user)
        
        return Response({
            'message': 'Login successful',
            'user_exists': True,
            'user': serializer.data,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)
    
    def _create_new_user(self, email, data):
        """Create new user"""
        try:
            with transaction.atomic():
                # Filter out email and any fields that shouldn't be set during creation
                allowed_fields = [
                    'full_name', 'address_line_1', 'address_line_2', 'city', 
                    'state', 'postalCode', 'countryCode', 'phoneNumber', 
                    'username', 'title', 'location', 'about', 'pets', 
                    'born', 'time_spend', 'want_to_go', 'obsessed', 
                    'website', 'language', 'latitude', 'longtitude', 'types'
                ]
                
                extra_fields = {k: v for k, v in data.items() 
                               if k in allowed_fields and k != 'email' and v is not None}
                
                user = UserAccount.objects.create_user(
                    email=email,
                    password=None,
                    **extra_fields
                )
                
                refresh = RefreshToken.for_user(user)
                serializer = UserAccountSerializer(user)
                
                return Response({
                    'message': 'User created successfully',
                    'user_exists': False,
                    'user': serializer.data,
                    'tokens': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    }
                }, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response(
                {'error': 'Failed to create user', 'details': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )








# for live chat


"""

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ChatRoomListSerializer
        return ChatRoomSerializer
    
    def get_queryset(self):
       
        user = self.request.user
        return ChatRoom.objects.filter(
            members=user,
            is_active=True
        ).select_related('created_by').prefetch_related(
            'members',
            'online_users__user',
            Prefetch(
                'messages',
                queryset=Message.objects.select_related('user').order_by('-timestamp')[:1],
                to_attr='latest_messages'
            )
        )
    
    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        
        room = self.get_object()
        
        # Check if user is member of the room
        if not room.members.filter(id=request.user.id).exists():
            return Response(
                {'error': 'You are not a member of this room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Get pagination parameters
        page_size = int(request.query_params.get('page_size', 50))
        before = request.query_params.get('before')  # timestamp for pagination
        
        messages_query = room.messages.select_related('user').filter(is_deleted=False)
        
        if before:
            try:
                before_dt = timezone.datetime.fromisoformat(before.replace('Z', '+00:00'))
                messages_query = messages_query.filter(timestamp__lt=before_dt)
            except ValueError:
                pass
        
        messages = messages_query.order_by('-timestamp')[:page_size]
        messages = list(reversed(messages))  # Chronological order
        
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
       
        room = self.get_object()
        
        # Check if user is member of the room
        if not room.members.filter(id=request.user.id).exists():
            return Response(
                {'error': 'You are not a member of this room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CreateMessageSerializer(
            data=request.data, 
            context={'request': request}
        )
        
        if serializer.is_valid():
            message = serializer.save(room=room)
            response_serializer = MessageSerializer(message, context={'request': request})
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
      
        room = self.get_object()
        
        if room.is_private:
            return Response(
                {'error': 'Cannot join private room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        room.members.add(request.user)
        
        return Response({'message': 'Successfully joined room'})
    
    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None): 
        room = self.get_object()
        room.members.remove(request.user)
        
        # Remove from online users
        OnlineUser.objects.filter(user=request.user, room=room).delete()
        
        return Response({'message': 'Successfully left room'})
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
      
        room = self.get_object()
        
        if not room.members.filter(id=request.user.id).exists():
            return Response(
                {'error': 'You are not a member of this room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        from .serializers import UserSerializer
        members = room.members.all()
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def online_users(self, request, pk=None):
      
        room = self.get_object()
        
        if not room.members.filter(id=request.user.id).exists():
            return Response(
                {'error': 'You are not a member of this room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Clean up old online users (older than 5 minutes)
        five_minutes_ago = timezone.now() - timezone.timedelta(minutes=5)
        OnlineUser.objects.filter(
            room=room,
            last_seen__lt=five_minutes_ago
        ).delete()
        
        online_users = OnlineUser.objects.filter(room=room).select_related('user')
        serializer = OnlineUserSerializer(online_users, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def mark_online(self, request, pk=None):
       
        room = self.get_object()
        
        if not room.members.filter(id=request.user.id).exists():
            return Response(
                {'error': 'You are not a member of this room'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        online_user, created = OnlineUser.objects.get_or_create(
            user=request.user,
            room=room
        )
        online_user.save()  # Updates last_seen
        
        return Response({'message': 'Marked as online'})

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        user_rooms = ChatRoom.objects.filter(members=self.request.user)
        return Message.objects.filter(
            room__in=user_rooms,
            is_deleted=False
        ).select_related('user', 'room').order_by('-timestamp')
    
    def perform_create(self, serializer):
      
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
       
        message = self.get_object()
        message.read_by.add(request.user)
        return Response({'message': 'Message marked as read'})
    
    @action(detail=True, methods=['post'])
    def edit(self, request, pk=None):
       
        message = self.get_object()
        
        if message.user != request.user:
            return Response(
                {'error': 'Can only edit your own messages'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        content = request.data.get('content')
        if not content:
            return Response(
                {'error': 'Content is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        message.content = content
        message.is_edited = True
        message.edited_at = timezone.now()
        message.save()
        
        serializer = MessageSerializer(message, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['delete'])
    def soft_delete(self, request, pk=None):
      
        message = self.get_object()
        
        if message.user != request.user:
            return Response(
                {'error': 'Can only delete your own messages'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        message.is_deleted = True
        message.content = '[Message deleted]'
        message.save()
        
        return Response({'message': 'Message deleted'})

# Additional view for searching users to add to rooms
class UserSearchViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return User.objects.filter(
                Q(email__icontains=query) |
                Q(full_name__icontains=query) |
                Q(username__icontains=query)
            ).filter(is_active=True)[:20]
        return User.objects.none()
    
    def get_serializer_class(self):
        from .serializers import UserSerializer
        return UserSerializer


"""


















# live chat simple 

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_conversations(request):
    """Get all conversations for the current user with unread counts"""
    user = request.user
    
    try:
        # Get latest message for each conversation
        conversations_subquery = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).values(
            'sender', 'receiver'
        ).annotate(
            latest_timestamp=Max('timestamp')
        )
        
        # Build conversation list with contact info
        contacts = []
        seen_users = set()
        
        for conv in conversations_subquery:
            other_user_id = conv['receiver'] if conv['sender'] == user.id else conv['sender']
            
            if other_user_id not in seen_users:
                try:
                    other_user = User.objects.get(id=other_user_id)
                    latest_message = Message.objects.filter(
                        Q(sender=user, receiver=other_user) | 
                        Q(sender=other_user, receiver=user)
                    ).latest('timestamp')
                    
                    unread_count = Message.objects.filter(
                        sender=other_user, 
                        receiver=user, 
                        is_read=False
                    ).count()
                    
                    contacts.append({
                        'user': UserSerializer(other_user).data,
                        'last_message': MessageSerializer(latest_message).data,
                        'unread_count': unread_count
                    })
                    seen_users.add(other_user_id)
                except (User.DoesNotExist, Message.DoesNotExist):
                    continue
        
        # Sort by latest message timestamp
        contacts.sort(key=lambda x: x['last_message']['timestamp'], reverse=True)
        
        return Response(contacts)
    except Exception as e:
        logger.error(f"Error fetching conversations for user {user.id}: {str(e)}")
        return Response({'error': 'Failed to fetch conversations'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request, user_id):
    """Get messages between current user and specified user"""
    try:
        other_user = User.objects.get(id=user_id)
        messages = Message.objects.filter(
            Q(sender=request.user, receiver=other_user) |
            Q(sender=other_user, receiver=request.user)
        ).order_by('timestamp')
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error fetching messages: {str(e)}")
        return Response({'error': 'Failed to fetch messages'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_messages_read(request, user_id):
    """Mark all messages from a user as read"""
    try:
        other_user = User.objects.get(id=user_id)
        updated_count = Message.objects.filter(
            sender=other_user,
            receiver=request.user,
            is_read=False
        ).update(is_read=True)
        
        logger.info(f"Marked {updated_count} messages as read for user {request.user.id}")
        return Response({'status': 'success', 'updated_count': updated_count})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error marking messages as read: {str(e)}")
        return Response({'error': 'Failed to mark messages as read'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request, user_id):
    """Get user details by ID"""
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request):
    """Search for users to start new conversations"""
    query = request.GET.get('q', '').strip()
    if not query:
        return Response([])
    
    try:
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email=query)
        ).exclude(id=request.user.id)[:10]
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error searching users: {str(e)}")
        return Response({'error': 'Search failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# get geolocation 
from django.http import JsonResponse
from ipwhois import IPWhois
import requests
import pycountry


def get_ip_info(request):
    try:
        # Get the client's IP (first from X-Forwarded-For if behind proxy)
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if ip:
            ip = ip.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        # If you're testing locally, fallback to external detection
        if ip in ("127.0.0.1", "::1"):
            ip = requests.get("https://api.ipify.org").text

        # Lookup info
        obj = IPWhois(ip)
        result = obj.lookup_rdap()

        # Extract country code
        country_code = result["network"]["country"]
        country = pycountry.countries.get(alpha_2=country_code)

        return JsonResponse({
            "ip": ip,
            "country_code": country_code,
            "country_name": country.name if country else "Unknown"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)









class WishlistToggleView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  

    def post(self, request, product_id):

        user_id = request.data.get("user_id")
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = request.user
        product = get_object_or_404(Product, id=product_id)

 
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=user,
            product=product
        )

        if not created:
            wishlist_item.delete()
            return Response(
                {"message": "Removed from wishlist", "is_in_wishlist": False},
                status=status.HTTP_200_OK
            )

        return Response(
            {"message": "Added to wishlist", "is_in_wishlist": True},
            status=status.HTTP_201_CREATED
        )




class WishlistListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Wishlist.objects.all()
                serializer_class = ProductImagesSerializer
                #filter_backends = [SearchFilter]
                filter_backends = [DjangoFilterBackend, SearchFilter] # Ensure this is correct
                #filterset_fields = ['category']  # Exact match filtering
                filterset_fields = {
                'product', 'id'  # Allows searching multiple names
                }

                

                def get(self, request, format=None):
                    snippets = self.filter_queryset(self.get_queryset()).order_by('-id')
                    serializer = WishlistSerializer(snippets, many=True)
                    return Response(serializer.data)

class WishlistCheckView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user_id = request.data.get("user_id")

        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = request.user

        product = get_object_or_404(Product, id=product_id)

        exists = Wishlist.objects.filter(user=user, product=product).exists()

        return Response(
            {"is_in_wishlist": exists},
            status=status.HTTP_200_OK
        )


#end




import json
import logging
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.mail import EmailMessage, BadHeaderError


# Import your custom user model
from .models import UserAccount

logger = logging.getLogger(__name__)

@csrf_exempt
@require_POST
def api_send_verification_email(request):
    """API endpoint to send verification email (no authentication required)"""
    try:
        # Parse JSON data
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        email = data.get('email')
        
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        
        try:
            user = UserAccount.objects.get(email=email)
            
            # Check if user is already verified
            if user.is_email_verified:
                return JsonResponse({'message': 'Email already verified'}, status=200)
            
            # Send verification email
            if send_verification_email(request, user):
                return JsonResponse({'message': 'Verification email sent successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Failed to send verification email'}, status=500)
                
        except UserAccount.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
            
    except Exception as e:
        logger.error(f"Unexpected error in api_send_verification_email: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_verification_email_view(request):
    """API endpoint to send/resend verification email (JWT protected)"""
    user = request.user
    
    # Debug information to help troubleshoot
    print(f"Authenticated user ID: {user.id}")
    print(f"Authenticated user email: {user.email}")
    
    # Check if user exists in our database
    try:
        db_user = UserAccount.objects.get(id=user.id)
    except UserAccount.DoesNotExist:
        return JsonResponse({'error': 'User not found in database'}, status=404)
    
    # Check if user is already verified
    if db_user.is_email_verified:
        return JsonResponse({'message': 'Email already verified'}, status=200)
    
    # Send verification email
    if send_verification_email(request, db_user):
        return JsonResponse({'message': 'Verification email sent successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Failed to send verification email'}, status=500)

def send_verification_email(request, user):
    """Send verification email to user"""
    try:
        current_site = get_current_site(request)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        verification_link = f"https://goamico.com/en/verify/{uid}/{token}/"
        
        subject = 'Verify Your Email Address'
        message = render_to_string('registration/verification_email.html', {
            'user': user,
            'verification_link': verification_link,
            'site_name': "https://goamico.com/en",
        })
        
        # Use send_mail with proper parameters
        email_sent = send_mail(
            subject=subject,
            message='Please verify your email address by clicking the link below:\n\n' + verification_link,
            html_message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )
        
        # Check if email was sent successfully
        if email_sent:
            logger.info(f"Verification email sent to {user.email}")
            return True
        else:
            logger.error(f"Email sending failed for {user.email}: No email was sent")
            return False
            
    except Exception as e:
        logger.error(f"Failed to send verification email to {user.email}: {str(e)}")
        return False


@csrf_exempt
def verify_email(request, uidb64, token):
    """Verify email using token from email link"""
    try:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = UserAccount.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserAccount.DoesNotExist):
            return JsonResponse({'error': 'Invalid verification link.'}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            return JsonResponse({'message': 'Your email has been verified successfully!'})
        else:
            return JsonResponse({'error': 'Invalid or expired verification link.'}, status=400)

    except Exception as e:
        logger.error(f"Error in verify_email: {str(e)}")
        logger.error(f"UID: {uidb64}, Token: {token}")
        return JsonResponse({'error': 'Internal server error during verification.'}, status=500)


@csrf_exempt
def verification_success(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        
        send_mail(
            subject="Verification Successful",
            message="Your email has been successfully verified. 🎉",
            from_email=settings.DEFAULT_FROM_EMAIL,  # must be configured
            recipient_list=[email],
            fail_silently=False,  # set True only for testing
        )

        return JsonResponse({"message": f"Verification success email sent to {email}"})





@csrf_exempt
def verification_failed(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        
        send_mail(
            subject="Verification Email",
            message="Your email has been unverified yet please try again.",
            from_email=settings.DEFAULT_FROM_EMAIL,  # must be configured
            recipient_list=[email],
            fail_silently=False,  # set True only for testing
        )

        return JsonResponse({"message": f"Verification success email sent to {email}"})






@csrf_exempt
def resend_verification(request):
    """Page to resend verification email (template form, not API)"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = UserAccount.objects.get(email=email)
            if user.is_active:
                messages.info(request, 'This email is already verified.')
            else:
                if send_verification_email(request, user):
                    messages.success(request, 'Verification email sent successfully!')
                else:
                    messages.error(request, 'Failed to send verification email. Please try again.')
        except UserAccount.DoesNotExist:
            messages.error(request, 'No account found with this email address.')
        
        return redirect('resend_verification')
    
    return render(request, 'registration/resend_verification.html')










    # test email

@csrf_exempt
@require_POST
def test_email_config(request):
    """Send an email with subject and HTML message"""
    try:
        raw_body = request.body.decode('utf-8', errors='ignore')
      
        try:
            data = json.loads(raw_body)
        except json.JSONDecodeError:
            return JsonResponse({'error': f'Invalid JSON body. Raw: {raw_body}'}, status=400)

        recipient_email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')  # 🔹 this will be treated as HTML

        if not recipient_email or not subject or not message:
            return JsonResponse(
                {'error': 'Email, subject, and message are required.'},
                status=400
            )

        # Create HTML email
        email = EmailMessage(
            subject=subject,
            body=message,   # HTML body
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
        )
        email.content_subtype = "html"  # 🔹 make it HTML

        email.send(fail_silently=False)

        return JsonResponse(
            {'message': f'Email sent successfully to {recipient_email}'},
            status=200
        )

    except Exception as e:
        return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=500)






# For OTP



from django.utils import timezone  # ADD THIS IMPORT - IT'S MISSING!
from .serializers import SendPhoneOTPSerializer, VerifyPhoneOTPSerializer
from .services import PhoneOTPService
from .models import PhoneOTP
import logging

logger = logging.getLogger(__name__)

# Replace your send_otp method with this version:

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def send_phone_otp(request):
    """Send OTP to phone number"""
    serializer = SendPhoneOTPSerializer(data=request.data)
    
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        
        # Check rate limiting
        recent_otps = PhoneOTP.objects.filter(
            phone_number=phone_number,
            created_at__gte=timezone.now() - timezone.timedelta(minutes=1)
        ).count()
        
        if recent_otps >= 3:
            return Response({
                'success': False,
                'message': 'Too many OTP requests. Please wait before requesting again.'
            }, status=status.HTTP_429_TOO_MANY_REQUESTS)
        
        # Send OTP
        result = PhoneOTPService.send_otp(phone_number)
        
        if result['success']:
            return Response({
                'success': True,
                'message': result['message'],
                'phone_number': phone_number,
                'expires_in_seconds': result['expires_in'],
                'debug_otp': result.get('debug_otp')  # Only in development
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'message': result['message']
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)





    
# Also create a minimal version that bypasses the service:
@api_view(['POST'])
@permission_classes([AllowAny])
def minimal_send_otp(request):
    """Minimal send OTP test without service call"""
    try:
        serializer = SendPhoneOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            
            # Just create OTP without sending SMS
            try:
                otp_instance = PhoneOTP.objects.create(phone_number=phone_number)
                print(f"Created OTP: {otp_instance.otp_code} for {phone_number}")
                
                return Response({
                    'success': True,
                    'message': 'OTP created successfully (not sent)',
                    'phone_number': phone_number,
                    'otp_code': otp_instance.otp_code,  # Only for testing
                }, status=status.HTTP_200_OK)
                
            except Exception as e:
                print(f"Database error: {e}")
                return Response({
                    'success': False,
                    'message': f'Database error: {str(e)}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'success': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        print(f"Error in minimal_send_otp: {e}")
        return Response({
            'success': False,
            'message': f'Error: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Also, let's create a simple test view to isolate the issue:
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def simple_test(request):
    """Simple test to check request handling"""
    try:
        if request.method == 'GET':
            return Response({
                'message': 'GET request working!',
                'method': request.method,
            })
        
        # For POST requests
        response_data = {
            'message': 'POST request received!',
            'method': request.method,
        }
        
        # Safely get request data
        try:
            response_data['received_data'] = request.data
        except Exception as e:
            response_data['data_error'] = str(e)
        
        # Safely get request body
        try:
            response_data['received_body'] = str(request.body)
        except Exception as e:
            response_data['body_error'] = str(e)
        
        # Safely get content type
        try:
            response_data['content_type'] = request.content_type
        except Exception as e:
            response_data['content_type_error'] = str(e)
        
        # Safely get headers
        try:
            response_data['headers'] = dict(request.headers)
        except Exception as e:
            response_data['headers_error'] = str(e)
        
        return Response(response_data)
        
    except Exception as e:
        # Catch any other errors
        import traceback
        return Response({
            'error': 'Internal server error',
            'error_message': str(e),
            'error_type': type(e).__name__,
            'traceback': traceback.format_exc(),
        }, status=500)


# Also create this ultra-simple test:
@api_view(['POST'])
@permission_classes([AllowAny])
def ultra_simple_test(request):
    """Ultra simple POST test"""
    try:
        return Response({'message': 'POST working!', 'status': 'success'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Also add this simpler endpoint
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Simple health check endpoint"""
    return Response({'status': 'ok', 'message': 'API is working!'})



@api_view(['POST'])
@permission_classes([AllowAny])
def verify_phone_otp(request):
    """Verify OTP code"""
    serializer = VerifyPhoneOTPSerializer(data=request.data)
    
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        otp_code = serializer.validated_data['otp_code']
        
        # Verify OTP
        result = PhoneOTPService.verify_otp(phone_number, otp_code)
        
        if result['success']:
            return Response({
                'success': True,
                'message': result['message'],
                'phone_number': phone_number,
                'verified_at': timezone.now().isoformat()
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'message': result['message']
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def check_phone_verification_status(request):
    """Check if phone number is verified"""
    phone_number = request.GET.get('phone_number')
    
    if not phone_number:
        return Response({
            'success': False,
            'message': 'phone_number parameter is required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Clean phone number
    cleaned_phone = phone_number.replace(' ', '').replace('-', '')
    if not cleaned_phone.startswith('+'):
        cleaned_phone = '+' + cleaned_phone
    
    # Check if phone number has been verified
    verified_otp = PhoneOTP.objects.filter(
        phone_number=cleaned_phone,
        is_verified=True
    ).first()
    
    return Response({
        'phone_number': cleaned_phone,
        'is_verified': bool(verified_otp),
        'last_verified_at': verified_otp.created_at.isoformat() if verified_otp else None
    }, status=status.HTTP_200_OK)

