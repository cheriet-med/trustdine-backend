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

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Amenities.objects.all().order_by('-id')
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

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Languages.objects.all().order_by('-id')
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
        'category': ['in'],  # Allows searching multiple names
    }
  
    search_fields = []  # Removed category, new_price, stock

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, format=None):
        filtered_queryset = self.filter_queryset(self.get_queryset().order_by('?'))
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
                filter_backends = [SearchFilter]
                search_fields = ['images']

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
                filter_backends = [SearchFilter]
                search_fields = ['images']

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
                filter_backends = [SearchFilter]
                search_fields = ['images']

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
                filter_backends = [SearchFilter]
                search_fields = ['Reviews_image']

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








# order
class OrderGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                authentication_classes = [TokenAuthentication]
                permission_classes = [IsAuthenticated]
                queryset = Order.objects.all()
                serializer_class = OrderSerializer
                filter_backends = [DjangoFilterBackend, SearchFilter]
                filterset_fields = ['status', 'product', 'user']  # Specify the fields to filter by
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

