from rest_framework import serializers
from .models import *  # Replace with your model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.utils.text import slugify
import uuid
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from django.conf import settings
from django.contrib.auth import get_user_model
import re


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = UserAccount
        fields = ('id', 'email', 'password', 'full_name')  # no is_partner, no is_staff

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.data.get('register_as') == 'partner':
            validated_data['is_staff'] = True
        else:
            validated_data['is_staff'] = False
        return super().create(validated_data)



class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ['password'] 
        extra_kwargs = {
            'email': {'read_only': True},
            'is_staff': {'read_only': True},
            #'is_active': {'read_only': True},
            'is_superuser': {'read_only': True},
        }

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = '__all__'



class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'



class EmailUserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


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





class NearbyattractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nearbyattractions
        fields = '__all__'  # Serialize all fields in the model



class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'  # Serialize all fields in the model


class SpecialtiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialties
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






class BillValidationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value.strip()







class ReviewHelpfulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewHelpful
        fields = '__all__'  # Serialize all fields in the model




class ReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReport
        fields = '__all__'  # Serialize all fields in the model



class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = '__all__'  # Serialize all fields in the model



class ReviewScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewScore
        fields = '__all__'  # Serialize all fields in the model


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__' 


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'id', 'email', 'is_active', 'is_staff', 'full_name',
            'address_line_1', 'address_line_2', 'city', 'state',
            'postalCode', 'countryCode', 'phoneNumber', 'status',
            'profile_image', 'username', 'title', 'identity_verified',
            'location', 'plan', 'about', 'pets', 'born', 'time_spend',
            'want_to_go', 'obsessed', 'website', 'language',
            'latitude', 'longtitude', 'joined', 'types', 'is_phone_number_verified', 'is_email_verified'
        ]
        read_only_fields = ['id', 'is_staff']









# for live chat 

User = get_user_model()  # This will get your custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'profile_image']  # Use your custom fields

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp', 'is_read']
3








"""

# for live chat rooms





# Get the custom user model
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
   
    display_name = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = UserModel
        fields = [
            'id', 
            'email', 
            'full_name', 
            'username',
            'display_name',
            'avatar',
            'profile_image',
            'is_active',
            'title',
            'location'
        ]
        read_only_fields = fields

    def get_display_name(self, obj):
      
        if obj.full_name:
            return obj.full_name
        elif obj.username:
            return obj.username
        return obj.email.split('@')[0]

    def get_avatar(self, obj):
      
        if obj.profile_image:
            return obj.profile_image.url
        return None

class MessageSerializer(serializers.ModelSerializer):
   
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)
    replies = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    read_by_users = UserSerializer(source='read_by', many=True, read_only=True)
    is_read = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = [
            'id',
            'content',
            'message_type',
            'timestamp',
            'edited_at',
            'is_edited',
            'is_deleted',
            'user',
            'user_id',
            'room',
            'parent_message',
            'replies',
            'reply_count',
            'read_by_users',
            'is_read'
        ]
        read_only_fields = ['id', 'timestamp', 'edited_at', 'is_edited']

    def get_replies(self, obj):
       
        if obj.replies.exists():
            return MessageSerializer(
                obj.replies.filter(is_deleted=False)[:5], 
                many=True, 
                context=self.context
            ).data
        return []

    def get_reply_count(self, obj):
      
        return obj.replies.filter(is_deleted=False).count()

    def get_is_read(self, obj):
      
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.read_by.filter(id=request.user.id).exists()
        return False

    def create(self, validated_data):
       
        user_id = validated_data.pop('user_id', None)
        request = self.context.get('request')
        
        if user_id:
            try:
                user = UserModel.objects.get(id=user_id)
                validated_data['user'] = user
            except UserModel.DoesNotExist:
                raise serializers.ValidationError("User not found")
        elif request and request.user.is_authenticated:
            validated_data['user'] = request.user
        else:
            raise serializers.ValidationError("User is required")
        
        return super().create(validated_data)

class CreateMessageSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Message
        fields = ['content', 'message_type', 'parent_message']
        
    def create(self, validated_data):
        
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        else:
            raise serializers.ValidationError("Authentication required")
        
        return super().create(validated_data)

class OnlineUserSerializer(serializers.ModelSerializer):
   
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = OnlineUser
        fields = ['user', 'last_seen']

class ChatRoomSerializer(serializers.ModelSerializer):
   
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    latest_message = MessageSerializer(read_only=True)
    message_count = serializers.SerializerMethodField()
    online_users = OnlineUserSerializer(many=True, read_only=True)
    online_count = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatRoom
        fields = [
            'id',
            'name',
            'display_name',
            'description',
            'created_at',
            'created_by',
            'members',
            'member_ids',
            'member_count',
            'is_private',
            'is_active',
            'latest_message',
            'message_count',
            'online_users',
            'online_count',
            'unread_count'
        ]
        read_only_fields = ['id', 'created_at', 'member_count']

    def get_message_count(self, obj):
       
        return obj.messages.filter(is_deleted=False).count()

    def get_online_count(self, obj):
      
        return obj.online_users.count()

    def get_unread_count(self, obj):
       
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Get user's last read message timestamp or room join time
            # This is a simplified version - you might want to track this differently
            user_messages = obj.messages.exclude(
                read_by=request.user
            ).exclude(
                user=request.user
            ).filter(is_deleted=False)
            return user_messages.count()
        return 0

    def create(self, validated_data):
       
        member_ids = validated_data.pop('member_ids', [])
        request = self.context.get('request')
        
        if request and request.user.is_authenticated:
            validated_data['created_by'] = request.user
        
        room = super().create(validated_data)
        
        # Add members
        if member_ids:
            members = UserModel.objects.filter(id__in=member_ids)
            room.members.set(members)
        
        # Add creator as member
        if request and request.user.is_authenticated:
            room.members.add(request.user)
        
        return room

class ChatRoomListSerializer(serializers.ModelSerializer):
   
    created_by = UserSerializer(read_only=True)
    latest_message = MessageSerializer(read_only=True)
    member_count = serializers.ReadOnlyField()
    online_count = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatRoom
        fields = [
            'id',
            'name',
            'display_name',
            'description',
            'created_at',
            'created_by',
            'member_count',
            'is_private',
            'is_active',
            'latest_message',
            'online_count',
            'unread_count'
        ]

    def get_online_count(self, obj):
        return obj.online_users.count()

    def get_unread_count(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.messages.exclude(
                read_by=request.user
            ).exclude(
                user=request.user
            ).filter(is_deleted=False).count()
        return 0


        """



class SendPhoneOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    
    def validate_phone_number(self, value):
        # Basic phone number validation
        phone_pattern = r'^\+?[1-9]\d{1,14}$'
        if not re.match(phone_pattern, value.replace(' ', '').replace('-', '')):
            raise serializers.ValidationError("Invalid phone number format")
        
        # Clean phone number
        cleaned_phone = value.replace(' ', '').replace('-', '')
        if not cleaned_phone.startswith('+'):
            cleaned_phone = '+' + cleaned_phone
        
        return cleaned_phone

class VerifyPhoneOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp_code = serializers.CharField(max_length=6, min_length=4)
    
    def validate_phone_number(self, value):
        phone_pattern = r'^\+?[1-9]\d{1,14}$'
        if not re.match(phone_pattern, value.replace(' ', '').replace('-', '')):
            raise serializers.ValidationError("Invalid phone number format")
        
        cleaned_phone = value.replace(' ', '').replace('-', '')
        if not cleaned_phone.startswith('+'):
            cleaned_phone = '+' + cleaned_phone
        
        return cleaned_phone
    
    def validate_otp_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("OTP must contain only digits")
        return value