from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'chatrooms', ChatRoomViewSet, basename='chatroom')
#router.register(r'messages', MessageViewSet, basename='message')
#router.register(r'users/search', UserSearchViewSet, basename='user-search')

urlpatterns = [
        #path("/", include(router.urls)),
   path('', Index.as_view(), name='index'),
   path('newsletterpost/', NewsLetterPostGlobal.as_view(), name='newsletter-only-post'),
   path('newsletterid/<int:pk>', Newsletterid.as_view()),
   path('emailletterpost/', EmailLetterPostGlobal.as_view(), name='emailletter'),
   path('emailletterpostid/<int:pk>', EmailLetterPostid.as_view(), name='email-crud'),
   path('api/user/', UserDetailsView.as_view(), name='user-details'),
   path('post/', PostGlobal.as_view(), name='posts'),
   path('postid/<int:pk>', Postid.as_view()),
   path('product/', ProductGlobal.as_view(), name='product'),
   path('productid/<int:pk>', Productid.as_view()),
   path('productimage/', ProductImageGlobal.as_view(), name='product-image'),
   path('productimageid/<int:pk>', ProductImageid.as_view()),
 

   path('nearbyattractions/', NearbyattractionsGlobal.as_view(), name='Nearbyattractions'),
   path('nearbyattractionsid/<int:pk>', Nearbyattractionsid.as_view()),

   path('awards/', AwardsGlobal.as_view(), name='Awards'),
   path('awardsid/<int:pk>', Awardsid.as_view()),

   path('specialties/', SpecialtiesGlobal.as_view(), name='Specialties'),
   path('specialtiesid/<int:pk>', Specialtiesid.as_view()),


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



   path('amenities/', AmenitiesPostGlobal.as_view(), name='Amenities'),
   path('tamenitiesid/<int:pk>', Amenitiesid.as_view()),

   path('languages/', LanguagesPostGlobal.as_view(), name='Languages'),
   path('languagesid/<int:pk>', Languagesid.as_view()),


   path('reviewhlpful/', ReviewHelpfulGlobal.as_view(), name='Languages'),
   path('reviewhlpfulid/<int:pk>', ReviewHelpfulid.as_view()),

   path('reviewreport/', ReviewReportGlobal.as_view(), name='Languages'),
   path('reviewreportid/<int:pk>', ReviewReportid.as_view()),

   path('verify/', VerifyGlobal.as_view(), name='verify documents'),
   path('verifyid/<int:pk>', Verifyid.as_view()),

   path('score/', ReviewScoreGlobal.as_view(), name='Score'),
   path('scoreid/<int:pk>', ReviewScoreid.as_view()),


    path('api/submit-email/', SubmitEmailView.as_view(), name='submit_email'),
    path('api/trigger-emails/', trigger_emails, name='trigger_emails'),  # For Cron-Job.org

    path('api/validate-bill/', BillValidationView.as_view(), name='validate-bill'),

    path('auth/email-login-register/', email_login_or_register, name='email-login-register'),
    path('auth/email-login-register-cbv/', EmailLoginOrRegisterView.as_view(), name='email-login-register-cbv'),
    path('api/chat/', include(router.urls)),


    path('api/conversations/', get_conversations, name='get_conversations'),
    path('api/messages/<int:user_id>/', get_messages, name='get_messages'),
    path('api/messages/<int:user_id>/read/', mark_messages_read, name='mark_messages_read'),
    path('api/user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('api/search-users/', search_users, name='search_users'),
    path("get-ip-info/", get_ip_info, name="get_ip_info"),


    path("wishlist/<int:product_id>/", WishlistToggleView.as_view(), name="wishlist-toggle"),
    path("wishlist/", WishlistListView.as_view(), name="wishlist-list"),
    path("wishlist/check/<int:product_id>/", WishlistCheckView.as_view(), name="wishlist-check"),


    path('verify-email/<str:uidb64>/<str:token>/',  verify_email, name='verify_email'),
    path('send-verification-email/',  send_verification_email_view, name='send_verification_email'),
    path('api/send-verification-email/',  api_send_verification_email, name='api_send_verification_email'),
    path('resend-verification/',  resend_verification, name='resend_verification'),
    path('verification-success/',  verification_success, name='verification_success'),
    path('verification-failed/',  verification_failed, name='verification_failed'),


    path('test-email-config/', test_email_config, name='test_email_config'),





    path('send-otp/', send_phone_otp, name='send_phone_otp'),
    path('minimal-send-otp/', minimal_send_otp, name='minimal_send_otp'),
    path('verify-otp/', verify_phone_otp, name='verify_phone_otp'),
    path('check-status/', check_phone_verification_status, name='check_phone_status'),
    path('simple-test/', simple_test, name='simple_test'),
    path('ultra-simple/', ultra_simple_test, name='ultra_simple_test'),

    path('health/', health_check, name='health_check'),

]



