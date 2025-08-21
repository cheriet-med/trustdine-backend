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

        

        """Process the uploaded image with quality checks and upscaling for blurry images"""
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
            
            # If image is blurry, try to upscale and enhance it before OCR
            if is_blurry:
                try:
                    # Upscale using OpenCV and sharpening
                    img = cv2.imread(temp_file_path)
                    
                    # Double the resolution using INTER_CUBIC interpolation
                    upscaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                    
                    # Apply sharpening filter
                    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                    sharpened = cv2.filter2D(upscaled, -1, kernel)
                    
                    # Save the enhanced image temporarily
                    enhanced_path = temp_file_path + "_enhanced.png"
                    cv2.imwrite(enhanced_path, sharpened)
                    
                    # Check if enhancement helped
                    enhanced_quality = self.check_image_quality(enhanced_path)
                    if enhanced_quality.get('sharpness_score', 0) > quality_report.get('sharpness_score', 0):
                        # Use the enhanced image if it's better
                        image = Image.open(enhanced_path)
                        quality_report = enhanced_quality
                        is_blurry = enhanced_quality.get('is_blurry', True)
                    
                except Exception as e:
                    # If enhancement fails, proceed with original image
                    print(f"Image enhancement failed: {str(e)}")
            
            if is_blurry:
                return {
                    'status': 'rejected',
                    'message': 'Image is too blurry to process',
                    'data': {
                        'quality_report': quality_report,
                        'is_bill': True,
                        'potential_titles': [input_title]
                    }
                }
            
            # Extract text using OCR with higher quality settings
            extracted_text = pytesseract.image_to_string(
                image, 
                lang='eng',
                config='--psm 6 --oem 3'  # Assume uniform block of text, LSTM OCR engine
            )
            
            # If very little text extracted, check if it's due to blurriness
            if len(extracted_text.strip()) < 20:  # Threshold for minimal text
                quality_report = self.check_image_quality(temp_file_path)
                if quality_report.get('is_blurry', False):
                    return {
                        'status': 'rejected',
                        'message': 'Image is too blurry - extracted very little text',
                        'data': {
                            'extracted_text': extracted_text,
                            'quality_report': quality_report,
                            'is_bill': True,
                            'potential_titles': [input_title]
                        }
                    }
            
            # Rest of your existing processing...
            extracted_data = self.extract_bill_data(extracted_text)
            validation_result = self.validate_bill_data(extracted_data, input_title)
            
            return validation_result
            
        finally:
            # Clean up temporary files
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            enhanced_path = temp_file_path + "_enhanced.png"
            if os.path.exists(enhanced_path):
                os.unlink(enhanced_path)
    
    def check_image_quality(self, image_path):
        """Check if image is blurry using OpenCV"""
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                return {'error': 'Could not read image'}
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Calculate Laplacian variance (measure of blurriness)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # Threshold for blur detection (adjust as needed)
            is_blurry = laplacian_var < 100  # Lower values mean more blurry
            
            return {
                'is_blurry': is_blurry,
                'sharpness_score': laplacian_var,
                'threshold': 100,
                'resolution': f"{image.shape[1]}x{image.shape[0]}"
            }
        except Exception as e:
            return {'error': f'Quality check failed: {str(e)}'}
    
    def extract_bill_data(self, text):
        """Extract relevant data from OCR text with restaurant-specific improvements"""
        # Enhanced bill indicators for restaurants
        bill_indicators = [
            'invoice', 'bill', 'receipt', 'statement', 'payment',
            'total', 'amount', 'due', 'subtotal', 'tax', 'charge',
            'check', 'thank you', 'vat', 'service', 'table', 'tab',
            'cosmopolitan', 'tel no', 'custom', 'servicenot included'
        ]
        
        # Extract potential titles/company names
        lines = text.strip().split('\n')
        potential_titles = []
        
        for i, line in enumerate(lines[:5]):  # Check first 5 lines
            clean_line = line.strip()
            if len(clean_line) > 2 and not re.match(r'^[\d\s\-\/\.\,\$]+$', clean_line):
                potential_titles.append(clean_line)
        
        # Enhanced date extraction
        date_patterns = [
 # Your exact format (day.month.year/hour:minute:second)
        r'(\d{2}\.\d{2}\.\d{4}/\d{2}:\d{2}:\d{2})',
        
        # More flexible versions that might appear in OCR
        r'(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{2,4}\s*/\s*\d{1,2}\s*:\s*\d{1,2}\s*:\s*\d{1,2})',
        r'(\d{1,2}\.\d{1,2}\.\d{2,4}\s+\d{1,2}:\d{1,2}:\d{1,2})',
    # Full date-time with seconds (dot + space)
    r'\b(\d{4}\.\d{2}\.\d{2}\.\s*\d{2}:\d{2}:\d{2})\b',   # 2025.08.15. 13:44:57

    # Full date-time with seconds (dot + slash)
    r'(\d{2}\.\d{2}\.\d{4}/\d{2}:\d{2}:\d{2})',

    # Date + time (without seconds, dot + space)
    r'\b(\d{4}\.\d{2}\.\d{2}\.\s*\d{2}:\d{2})\b',         # 2025.08.15. 13:44

    # Date only
    r'\b(\d{4}\.\d{2}\.\d{2})\b',                         # 2025.08.15
    r'\b(\d{2}\.\d{2}\.\d{4})\b',                         # 07.11.2025

    # Common international date formats
    r'\b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})\b',
    r'\b(\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2})\b',
    r'\b(\d{1,2}[-/](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/]\d{2,4})\b',
    r'\b(\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4})\b',
    r'\b((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{2,4})\b',

    # Time only (last so it doesn’t override full datetime)
    r'\b(\d{1,2}:\d{1,2}(:\d{1,2})?)\b'
]

        extracted_dates = []
        for pattern in date_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get the full date group (group 0) or the first subgroup
                date_str = match.group(0) if len(match.groups()) == 0 else match.group(1)
                if date_str:
                    extracted_dates.append(date_str)



        # Enhanced amount extraction for restaurant bills
        amount_pattern = r'\b\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?\s*(?:Ft|HUF|USD|EUR|GBP)?\b'
        amounts = re.findall(amount_pattern, text)
        amounts = [amt.replace('£', '').replace('$', '').replace(',', '').strip() for amt in amounts]
        
        # Check if text contains bill indicators (case insensitive)
        lower_text = text.lower()
        is_bill = any(indicator.lower() in lower_text for indicator in bill_indicators)
        
        # Additional check for restaurant bills - look for itemized purchases
        has_items = bool(re.search(r'\d+\s+[A-Za-z].+\d+\.\d{2}', text))
        
        return {
            'extracted_text': text,
            'potential_titles': potential_titles,
            'extracted_dates': extracted_dates,
            'amounts': amounts,
            'is_bill': is_bill or has_items,  # Consider it a bill if it has items
            'bill_indicators_found': [indicator for indicator in bill_indicators 
                                    if indicator.lower() in lower_text],
            'has_items': has_items
        }
    
    def validate_bill_data(self, extracted_data, input_title):
        """Validate the extracted data against input criteria"""
        
        # Check if it's a bill
        if not extracted_data['is_bill']:
            return {
                'status': 'rejected',
                'message': 'Document does not appear to be a bill or to blurry',
                'data': extracted_data
            }
        
        # Check title match
        title_found = False
        matched_title = None
        
        for potential_title in extracted_data['potential_titles']:
            # Flexible matching - check if input title is contained in extracted title or vice versa
            if (input_title.lower() in potential_title.lower() or 
                potential_title.lower() in input_title.lower() or
                self.fuzzy_match(input_title.lower(), potential_title.lower())):
                title_found = True
                matched_title = potential_title
                break
        
        if not title_found:
            return {
                'status': 'rejected',
                'message': 'Title not found in the bill',
                'data': extracted_data
            }
        
        # Check date validity (within 21 days)
        date_valid = False
        valid_date = None
        current_date = datetime.now()
        
        for date_str in extracted_data['extracted_dates']:
            try:
                # Try different date formats
                parsed_date = self.parse_date(date_str)
                if parsed_date:
                    days_diff = (current_date - parsed_date).days
                    if 0 <= days_diff <= 21:
                        date_valid = True
                        valid_date = parsed_date.strftime('%Y-%m-%d')
                        break
            except:
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
                    'all_dates_found': extracted_data['extracted_dates']
                }
            }
        }
    
    def fuzzy_match(self, str1, str2, threshold=0.6):
        """Simple fuzzy matching for titles"""
        # Remove common words and special characters
        common_words = ['inc', 'ltd', 'llc', 'corp', 'company', 'co', 'the', 'and', '&']
        
        def clean_string(s):
            s = re.sub(r'[^\w\s]', ' ', s.lower())
            words = s.split()
            return ' '.join([w for w in words if w not in common_words and len(w) > 1])
        
        clean_str1 = clean_string(str1)
        clean_str2 = clean_string(str2)
        
        if not clean_str1 or not clean_str2:
            return False
        
        # Simple word overlap ratio
        words1 = set(clean_str1.split())
        words2 = set(clean_str2.split())
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        if not union:
            return False
        
        similarity = len(intersection) / len(union)
        return similarity >= threshold
    
    def parse_date(self, date_str):

        """Parse various date formats with improved month handling"""
        # Clean the date string
        clean_date = date_str.strip().rstrip('.').replace(':', '').strip()
        
        # Additional cleaning for invoice date prefixes
        clean_date = re.sub(r'^(Invoice|Bill|Receipt)\s*(Date)?\s*[:]?\s*', '', clean_date, flags=re.IGNORECASE)
        
        date_formats = [
            # Day-Month-Year variations
            '%d-%b-%y',     # 20-May-18
            '%d-%B-%y',     # 20-May-18 (full month)
            '%d/%b/%y',     # 20/May/18
            '%d/%B/%y',     # 20/May/18 (full month)
            '%d %b %y',     # 20 May 18
            '%d %B %y',     # 20 May 18 (full month)
            '%d-%m-%Y',     # 20-05-2018
            '%d/%m/%Y',     # 20/05/2018
            '%d.%m.%Y',     # 20.05.2018
            '%d %m %Y',     # 20 05 2018
            '%d-%m-%y',     # 20-05-18
            '%d/%m/%y',     # 20/05/18
            '%d.%m.%y',     # 20.05.18
            '%d %m %y',     # 20 05 18

            # Month-Day-Year (US style)
            '%m-%d-%Y',     # 05-20-2018
            '%m/%d/%Y',     # 05/20/2018
            '%m.%d.%Y',     # 05.20.2018
            '%m %d %Y',     # 05 20 2018
            '%m-%d-%y',     # 05-20-18
            '%m/%d/%y',     # 05/20/18
            '%m.%d.%y',     # 05.20.18
            '%m %d %y',     # 05 20 18
            '%b-%d-%Y',     # May-20-2018
            '%B-%d-%Y',     # May-20-2018 (full month)
            '%b %d %Y',     # May 20 2018
            '%B %d %Y',     # May 20 2018 (full month)
            '%b-%d-%y',     # May-20-18
            '%B-%d-%y',     # May-20-18 (full month)
            '%b %d %y',     # May 20 18
            '%B %d %y',     # May 20 18 (full month)

            # Year-Month-Day (ISO & variants)
            '%Y-%m-%d',     # 2018-05-20
            '%Y/%m/%d',     # 2018/05/20
            '%Y.%m.%d',     # 2018.05.20
            '%Y %m %d',     # 2018 05 20
            '%y-%m-%d',     # 18-05-20
            '%y/%m/%d',     # 18/05/20
            '%y.%m.%d',     # 18.05.20
            '%y %m %d',     # 18 05 20

            # Year-Month-Day (with month names)
            '%Y-%b-%d',     # 2018-May-20
            '%Y-%B-%d',     # 2018-May-20 (full month)
            '%Y/%b/%d',     # 2018/May/20
            '%Y/%B/%d',     # 2018/May/20 (full month)
            '%Y %b %d',     # 2018 May 20
            '%Y %B %d',     # 2018 May 20 (full month)

            # Extra compact styles
            '%d%b%Y',       # 20May2018
            '%d%B%Y',       # 20May2018 (full month)
            '%b%d%Y',       # May202018
            '%B%d%Y',       # May202018 (full month)
            '%Y%b%d',       # 2018May20
            '%Y%B%d',       # 2018May20 (full month)
            '%Y%m%d',       # 20180520
            '%y%m%d',       # 180520

            # Your requested format
            '%Y.%m.%d',     # 2025.08.15
        ]

        
        for fmt in date_formats:
            try:
                return datetime.strptime(clean_date, fmt)
            except ValueError:
                continue
        
        return None

