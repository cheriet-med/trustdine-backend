from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
        #path("/", include(router.urls)),
   path('', Index.as_view(), name='index'),
   path('offer/', OfferGlobal.as_view(), name='offer get and post'),
   path('newsletterpost/', NewsLetterPostGlobal.as_view(), name='newsletter-only-post'),
   path('newsletterid/<int:pk>', Newsletterid.as_view()),
   path('emailletterpost/', EmailLetterPostGlobal.as_view(), name='emailletter-only-post'),
   path('api/user/', UserDetailsView.as_view(), name='user-details'),
   path('post/', PostGlobal.as_view(), name='posts'),
   path('postid/<int:pk>', Postid.as_view()),
   path('product/', ProductGlobal.as_view(), name='product'),
   path('productid/<int:pk>', Productid.as_view()),
   path('productimage/', ProductImageGlobal.as_view(), name='product-image'),
   path('productimageid/<int:pk>', ProductImageid.as_view()),
   path('productimagevariation/', ProductImageVariationGlobal.as_view(), name='product-image-variations'),
   path('productimagevariationid/<int:pk>', ProductImageVariationid.as_view()),
   path('productsizevariation/', ProductSizeVariationGlobal.as_view(), name='product-size-variations'),
   path('productsizevariationid/<int:pk>', ProductSizeVariationid.as_view()),
   path('productreviews/', ProductReviewsGlobal.as_view(), name='product-reviews'),
   path('productreviewsid/<int:pk>', ProductReviewsid.as_view()),
   path('reviewsimage/', ReviewsImageGlobal.as_view(), name='product-reviews-images'),
   path('reviewsimageid/<int:pk>', ReviewsImageid.as_view()),
   path('order/', OrderGlobal.as_view(), name='orders'),
   path('orderid/<int:pk>', Orderid.as_view()),
   path('userglobal/', UserGlobal.as_view(), name='user-informations'),

   path('infoglobal/', InformationsGlobal.as_view(), name='user-informations'),
   path('infoid/<int:pk>', InformationsId.as_view()),

   path('email/', SendEmailGlobal.as_view(), name='send-email'),
   path('emailcreateorder/', SendEmailCreateOrders.as_view(), name='send-email-create-order'),
   path('emailtrakingnumber/', SendEmailTrakinNumber.as_view(), name='send-email-traking-number'),

   path('returnglobal/', ReturnGlobal.as_view(), name='return'),
   path('returnid/<int:pk>', Returnid.as_view()),
   path('feedbackglobal/', FeedbackGlobal.as_view(), name='feedback'),
   path('feedbackid/<int:pk>', Feedbackid.as_view()),

   path('coponglobal/', CoponGlobal.as_view(), name='coupon'),
   path('coponid/<int:pk>', Coponid.as_view()),



   path('test/', testReview.as_view(), name='test'),
   path('testid/<int:pk>', testReviewid.as_view()),


    path('api/submit-email/', SubmitEmailView.as_view(), name='submit_email'),
    path('api/trigger-emails/', trigger_emails, name='trigger_emails'),  # For Cron-Job.org

]



