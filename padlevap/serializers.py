from rest_framework import serializers
from .models import *  # Replace with your model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.utils.text import slugify
import uuid
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = UserAccount
        fields = ('email', 'password')



class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','full_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postalCode', 'countryCode', 'phoneNumber', 'status')



class EmailUserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email', 'full_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postalCode', 'countryCode', 'phoneNumber')



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'  # Serialize all fields in the model

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'  # Serialize all fields in the model


class EmailLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLetter
        fields = '__all__'  # Serialize all fields in the model




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Serialize all fields in the model





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Serialize all fields in the model





class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'  # Serialize all fields in the model




class ProductImagesVariantionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageVariation
        fields = '__all__'  # Serialize all fields in the model




class SizeVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariation
        fields = '__all__'  # Serialize all fields in the model



class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'  # Serialize all fields in the model



class RviewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RviewsImage
        fields = '__all__'  # Serialize all fields in the model

        

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all(), required=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False)
    class Meta:
        model = Order
        fields = '__all__'  # Serialize all fields in the model



class SendEmailForPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailForPassword
        fields = '__all__'  # Serialize all fields in the model





class SendEmailCreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailCreateOrder
        fields = '__all__'  # Serialize all fields in the model




class SendEmailTrakingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmailTrakingNumber
        fields = '__all__'  # Serialize all fields in the model




class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'  # Serialize all fields in the model




class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'  # Serialize all fields in the model




class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'  # Serialize all fields in the model




class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEmail
        fields = ['email', 'language', 'name']




class TestSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()  # Add this to get full URL
    
    class Meta:
        model = test
        fields = '__all__'
    
    def get_image_url(self, obj):
        """Return the full Cloudinary URL"""
        if obj.image_en:
            return CloudinaryImage(str(obj.image_en)).build_url()
        return None
    
    def create(self, validated_data):
        image_file = validated_data.get('image_en')
        
        if image_file:
            # Extract original filename
            original_filename = os.path.splitext(image_file.name)[0]
            clean_filename = slugify(original_filename)
            unique_id = str(uuid.uuid4())[:8]
            public_id = f"review-images/{clean_filename}-{unique_id}"
            
            try:
                upload_result = cloudinary.uploader.upload(
                    image_file,
                    public_id=public_id,
                    folder="review-images",
                    overwrite=False
                )
                
                # The URL will now contain your original filename
                print(f"Uploaded URL: {upload_result['secure_url']}")
                # This will be something like:
                # https://res.cloudinary.com/your-cloud/image/upload/v1234567890/review-images/nextjs-icon-abc12345.jpg
                
                validated_data['image_en'] = upload_result['public_id']
                
            except Exception as e:
                raise serializers.ValidationError(f"Image upload failed: {str(e)}")
        
        return super().create(validated_data)