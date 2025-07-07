from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.utils import timezone
import uuid

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        #extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    full_name = models.CharField(max_length=1000, blank=True, null=True)
    address_line_1 = models.CharField(max_length=1000, blank=True, null=True)
    address_line_2 = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    postalCode = models.CharField(max_length=1000, blank=True, null=True)
    countryCode = models.CharField(max_length=1000, blank=True, null=True)
    phoneNumber = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.full_name

 
    
    def __str__(self):
        return self.email
        



class Offer(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    language = models.CharField(max_length=500, blank=True, null=True)
    date = models.CharField(max_length=500, blank=True, null=True)
    time = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.email





class NewsLetter(models.Model):
    email = models.CharField(max_length=1000,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.email

class EmailLetter(models.Model):
    email = models.CharField(max_length=1000,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    
    def __str__(self):
        return self.email



class Post(models.Model):
    url_en = models.CharField(max_length=1000,blank=True, null=True)
    url_ar = models.CharField(max_length=1000,blank=True, null=True)
    url_de = models.CharField(max_length=1000,blank=True, null=True)
    url_es = models.CharField(max_length=1000,blank=True, null=True)
    url_fr = models.CharField(max_length=1000,blank=True, null=True)
    url_it = models.CharField(max_length=1000,blank=True, null=True)
    url_nl = models.CharField(max_length=1000,blank=True, null=True)
    url_pt = models.CharField(max_length=1000,blank=True, null=True)
    url_ru = models.CharField(max_length=1000,blank=True, null=True)
    url_sv = models.CharField(max_length=1000,blank=True, null=True)
    image_en = CloudinaryField('images', blank=True, null=True)
    image_ar = CloudinaryField('images', blank=True, null=True)
    image_de = CloudinaryField('images', blank=True, null=True)
    image_es = CloudinaryField('images', blank=True, null=True)
    image_fr = CloudinaryField('images', blank=True, null=True)
    image_it = CloudinaryField('images', blank=True, null=True)
    image_nl = CloudinaryField('images', blank=True, null=True)
    image_pt = CloudinaryField('images', blank=True, null=True)
    image_ru = CloudinaryField('images', blank=True, null=True)
    image_sv = CloudinaryField('images', blank=True, null=True)
    tag_en = models.CharField(max_length=1000,blank=True, null=True)
    tag_ar = models.CharField(max_length=1000,blank=True, null=True)
    tag_de = models.CharField(max_length=1000,blank=True, null=True)
    tag_es = models.CharField(max_length=1000,blank=True, null=True)
    tag_fr = models.CharField(max_length=1000,blank=True, null=True)
    tag_it = models.CharField(max_length=1000,blank=True, null=True)
    tag_nl = models.CharField(max_length=1000,blank=True, null=True)
    tag_pt = models.CharField(max_length=1000,blank=True, null=True)
    tag_ru = models.CharField(max_length=1000,blank=True, null=True)
    tag_sv = models.CharField(max_length=1000,blank=True, null=True)
    title_en = models.CharField(max_length=1000,blank=True, null=True)
    title_ar = models.CharField(max_length=1000,blank=True, null=True)
    title_de = models.CharField(max_length=1000,blank=True, null=True)
    title_es = models.CharField(max_length=1000,blank=True, null=True)
    title_fr = models.CharField(max_length=1000,blank=True, null=True)
    title_it = models.CharField(max_length=1000,blank=True, null=True)
    title_nl = models.CharField(max_length=1000,blank=True, null=True)
    title_pt = models.CharField(max_length=1000,blank=True, null=True)
    title_ru = models.CharField(max_length=1000,blank=True, null=True)
    title_sv = models.CharField(max_length=1000,blank=True, null=True)
    description_en = models.CharField(max_length=1000,blank=True, null=True)
    description_ar = models.CharField(max_length=1000,blank=True, null=True)
    description_de = models.CharField(max_length=1000,blank=True, null=True)
    description_es = models.CharField(max_length=1000,blank=True, null=True)
    description_fr = models.CharField(max_length=1000,blank=True, null=True)
    description_it = models.CharField(max_length=1000,blank=True, null=True)
    description_nl = models.CharField(max_length=1000,blank=True, null=True)
    description_pt = models.CharField(max_length=1000,blank=True, null=True)
    description_ru = models.CharField(max_length=1000,blank=True, null=True)
    description_sv = models.CharField(max_length=1000,blank=True, null=True)
    content_en = models.CharField(max_length=10000,blank=True, null=True)
    content_ar = models.CharField(max_length=10000,blank=True, null=True)
    content_de = models.CharField(max_length=10000,blank=True, null=True)
    content_es = models.CharField(max_length=10000,blank=True, null=True)
    content_fr = models.CharField(max_length=10000,blank=True, null=True)
    content_it = models.CharField(max_length=10000,blank=True, null=True)
    content_nl = models.CharField(max_length=10000,blank=True, null=True)
    content_pt = models.CharField(max_length=10000,blank=True, null=True)
    content_ru = models.CharField(max_length=10000,blank=True, null=True)
    content_sv = models.CharField(max_length=10000,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)
    licence = models.CharField(max_length=10000,blank=True, null=True)
    keyword_1_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_sv = models.CharField(max_length=1000,blank=True, null=True)
    created_at_meta = models.CharField(max_length=50, blank=True)
    updated_at_meta = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        now = timezone.now().isoformat()
        if not self.created_at_meta:
            self.created_at_meta = now
        self.updated_at_meta = now
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en


# for ecommerce database


class Product(models.Model):
    url_en = models.CharField(max_length=1000,blank=True, null=True)
    url_ar = models.CharField(max_length=1000,blank=True, null=True)
    url_de = models.CharField(max_length=1000,blank=True, null=True)
    url_es = models.CharField(max_length=1000,blank=True, null=True)
    url_fr = models.CharField(max_length=1000,blank=True, null=True)
    url_it = models.CharField(max_length=1000,blank=True, null=True)
    url_nl = models.CharField(max_length=1000,blank=True, null=True)
    url_pt = models.CharField(max_length=1000,blank=True, null=True)
    url_ru = models.CharField(max_length=1000,blank=True, null=True)
    url_sv = models.CharField(max_length=1000,blank=True, null=True)
    title_en = models.CharField(max_length=1000,blank=True, null=True)
    title_ar = models.CharField(max_length=1000,blank=True, null=True)
    title_de = models.CharField(max_length=1000,blank=True, null=True)
    title_es = models.CharField(max_length=1000,blank=True, null=True)
    title_fr = models.CharField(max_length=1000,blank=True, null=True)
    title_it = models.CharField(max_length=1000,blank=True, null=True)
    title_nl = models.CharField(max_length=1000,blank=True, null=True)
    title_pt = models.CharField(max_length=1000,blank=True, null=True)
    title_ru = models.CharField(max_length=1000,blank=True, null=True)
    title_sv = models.CharField(max_length=1000,blank=True, null=True)
    content_en = models.CharField(max_length=10000,blank=True, null=True)
    content_ar = models.CharField(max_length=10000,blank=True, null=True)
    content_de = models.CharField(max_length=10000,blank=True, null=True)
    content_es = models.CharField(max_length=10000,blank=True, null=True)
    content_fr = models.CharField(max_length=10000,blank=True, null=True)
    content_it = models.CharField(max_length=10000,blank=True, null=True)
    content_nl = models.CharField(max_length=10000,blank=True, null=True)
    content_pt = models.CharField(max_length=10000,blank=True, null=True)
    content_ru = models.CharField(max_length=10000,blank=True, null=True)
    content_sv = models.CharField(max_length=10000,blank=True, null=True)
    tag_en = models.CharField(max_length=1000,blank=True, null=True)
    tag_ar = models.CharField(max_length=1000,blank=True, null=True)
    tag_de = models.CharField(max_length=1000,blank=True, null=True)
    tag_es = models.CharField(max_length=1000,blank=True, null=True)
    tag_fr = models.CharField(max_length=1000,blank=True, null=True)
    tag_it = models.CharField(max_length=1000,blank=True, null=True)
    tag_nl = models.CharField(max_length=1000,blank=True, null=True)
    tag_pt = models.CharField(max_length=1000,blank=True, null=True)
    tag_ru = models.CharField(max_length=1000,blank=True, null=True)
    tag_sv = models.CharField(max_length=1000,blank=True, null=True)
    image_en = CloudinaryField('images', blank=True, null=True)
    image_ar = CloudinaryField('images', blank=True, null=True)
    image_de = CloudinaryField('images', blank=True, null=True)
    image_es = CloudinaryField('images', blank=True, null=True)
    image_fr = CloudinaryField('images', blank=True, null=True)
    image_it = CloudinaryField('images', blank=True, null=True)
    image_nl = CloudinaryField('images', blank=True, null=True)
    image_pt = CloudinaryField('images', blank=True, null=True)
    image_ru = CloudinaryField('images', blank=True, null=True)
    image_sv = CloudinaryField('images', blank=True, null=True)
    tag1_en = models.CharField(max_length=1000,blank=True, null=True)
    tag1_ar = models.CharField(max_length=1000,blank=True, null=True)
    tag1_de = models.CharField(max_length=1000,blank=True, null=True)
    tag1_es = models.CharField(max_length=1000,blank=True, null=True)
    tag1_fr = models.CharField(max_length=1000,blank=True, null=True)
    tag1_it = models.CharField(max_length=1000,blank=True, null=True)
    tag1_nl = models.CharField(max_length=1000,blank=True, null=True)
    tag1_pt = models.CharField(max_length=1000,blank=True, null=True)
    tag1_ru = models.CharField(max_length=1000,blank=True, null=True)
    tag1_sv = models.CharField(max_length=1000,blank=True, null=True)
    image1_en = CloudinaryField('images', blank=True, null=True)
    image1_ar = CloudinaryField('images', blank=True, null=True)
    image1_de = CloudinaryField('images', blank=True, null=True)
    image1_es = CloudinaryField('images', blank=True, null=True)
    image1_fr = CloudinaryField('images', blank=True, null=True)
    image1_it = CloudinaryField('images', blank=True, null=True)
    image1_nl = CloudinaryField('images', blank=True, null=True)
    image1_pt = CloudinaryField('images', blank=True, null=True)
    image1_ru = CloudinaryField('images', blank=True, null=True)
    image1_sv = CloudinaryField('images', blank=True, null=True)
    old_price = models.CharField(max_length=500,blank=True, null=True)
    new_price = models.CharField(max_length=500,blank=True, null=True)
    category = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)
    dropshippingID = models.CharField(max_length=500,blank=True, null=True)
    coupon = models.CharField(max_length=500,blank=True, null=True)
    instock = models.CharField(max_length=1000, blank=True, null=True, default="yes")
    brand = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_1_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_2_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_3_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_4_sv = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_en = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_ar = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_de = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_es = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_fr = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_it = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_nl = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_pt = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_ru = models.CharField(max_length=1000,blank=True, null=True)
    keyword_5_sv = models.CharField(max_length=1000,blank=True, null=True)
    created_at_meta = models.CharField(max_length=50, blank=True)
    updated_at_meta = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        now = timezone.now().isoformat()
        if not self.created_at_meta:
            self.created_at_meta = now
        self.updated_at_meta = now
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title_en



class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image =  CloudinaryField('images')
    #is_primary = models.BooleanField(default=False)  # To mark the primary image for the product

    def __str__(self):
        return f"Image for {self.product.name}"



class ProductImageVariation(models.Model):
    product = models.ForeignKey(Product, related_name='color_variations', on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    #is_primary = models.BooleanField(default=False)  # To mark the primary image for the product

    def __str__(self):
        return f"Image for {self.product.name}"


class SizeVariation(models.Model):

    product = models.ForeignKey(Product, related_name='size_variations', on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    #stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size}"





class SendEmailForPassword(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    password = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date = models.CharField(max_length=500,blank=True, null=True)
    time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"








class ProductReview(models.Model):

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, related_name='reviews', on_delete=models.CASCADE)
    rating = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    updated_at = models.CharField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=1000, blank=True, null=True)
    size = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Review by {self.UserAccount.email} for {self.product.title_en}"

    #class Meta:
        #unique_together = ('product', 'user')  # Ensure a user can only review a product once





class RviewsImage(models.Model):
    ProductReview = models.ForeignKey(ProductReview, related_name='Reviews_image', on_delete=models.CASCADE)
    image =  CloudinaryField('images')
    #is_primary = models.BooleanField(default=False)  # To mark the primary image for the product

    def __str__(self):
        return f"Image for {self.RviewsImage.comment}"




class Order(models.Model):

    user = models.ForeignKey(UserAccount, related_name='user_orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='product_orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.CharField(max_length=500,blank=True, null=True)
    updated_at = models.CharField(max_length=500,blank=True, null=True)
    size = models.CharField(max_length=500,blank=True, null=True)
    color = models.CharField(max_length=500,blank=True, null=True)
    quantity = models.CharField(max_length=500,blank=True, null=True)
    price = models.CharField(max_length=500,blank=True, null=True)
    transation_ID_order = models.CharField(max_length=500,blank=True, null=True)
    transation_ID_item = models.CharField(max_length=500,blank=True, null=True)
    title_en = models.CharField(max_length=1000,blank=True, null=True)
    title_ar = models.CharField(max_length=1000,blank=True, null=True)
    title_de = models.CharField(max_length=1000,blank=True, null=True)
    title_es = models.CharField(max_length=1000,blank=True, null=True)
    title_fr = models.CharField(max_length=1000,blank=True, null=True)
    title_it = models.CharField(max_length=1000,blank=True, null=True)
    title_nl = models.CharField(max_length=1000,blank=True, null=True)
    title_pt = models.CharField(max_length=1000,blank=True, null=True)
    title_ru = models.CharField(max_length=1000,blank=True, null=True)
    title_sv = models.CharField(max_length=1000,blank=True, null=True)
    tag_en = models.CharField(max_length=1000,blank=True, null=True)
    tag_ar = models.CharField(max_length=1000,blank=True, null=True)
    tag_de = models.CharField(max_length=1000,blank=True, null=True)
    tag_es = models.CharField(max_length=1000,blank=True, null=True)
    tag_fr = models.CharField(max_length=1000,blank=True, null=True)
    tag_it = models.CharField(max_length=1000,blank=True, null=True)
    tag_nl = models.CharField(max_length=1000,blank=True, null=True)
    tag_pt = models.CharField(max_length=1000,blank=True, null=True)
    tag_ru = models.CharField(max_length=1000,blank=True, null=True)
    tag_sv = models.CharField(max_length=1000,blank=True, null=True)
    image_en = CloudinaryField('images', blank=True, null=True)
    image_ar = CloudinaryField('images', blank=True, null=True)
    image_de = CloudinaryField('images', blank=True, null=True)
    image_es = CloudinaryField('images', blank=True, null=True)
    image_fr = CloudinaryField('images', blank=True, null=True)
    image_it = CloudinaryField('images', blank=True, null=True)
    image_nl = CloudinaryField('images', blank=True, null=True)
    image_pt = CloudinaryField('images', blank=True, null=True)
    image_ru = CloudinaryField('images', blank=True, null=True)
    image_sv = CloudinaryField('images', blank=True, null=True)
    url_en = models.CharField(max_length=1000,blank=True, null=True)
    url_ar = models.CharField(max_length=1000,blank=True, null=True)
    url_de = models.CharField(max_length=1000,blank=True, null=True)
    url_es = models.CharField(max_length=1000,blank=True, null=True)
    url_fr = models.CharField(max_length=1000,blank=True, null=True)
    url_it = models.CharField(max_length=1000,blank=True, null=True)
    url_nl = models.CharField(max_length=1000,blank=True, null=True)
    url_pt = models.CharField(max_length=1000,blank=True, null=True)
    url_ru = models.CharField(max_length=1000,blank=True, null=True)
    url_sv = models.CharField(max_length=1000,blank=True, null=True)
    full_name = models.CharField(max_length=1000, blank=True, null=True)
    address_line_1 = models.CharField(max_length=1000, blank=True, null=True)
    address_line_2 = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    postalCode = models.CharField(max_length=1000, blank=True, null=True)
    countryCode = models.CharField(max_length=1000, blank=True, null=True)
    phoneNumber = models.CharField(max_length=1000, blank=True, null=True)
    payment_method = models.CharField(max_length=1000, blank=True, null=True)
    trakingNumber = models.CharField(max_length=1000, blank=True, null=True)
    viewed = models.CharField(max_length=1000, blank=True, null=True, default="no")
    dropshippingID = models.CharField(max_length=500,blank=True, null=True)
    orderN = models.CharField(max_length=500,blank=True, null=True)
    descount = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.full_name}"






class SendEmailCreateOrder(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    OrderID = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date_time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"





class SendEmailTrakingNumber(models.Model):
    name = models.CharField(max_length=500,blank=True, null=True)
    email = models.CharField(max_length=500,blank=True, null=True)
    trakingNumber = models.CharField(max_length=500,blank=True, null=True)
    language = models.CharField(max_length=500,blank=True, null=True)
    date_time = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"







class Feedback(models.Model):
  
    user = models.ForeignKey(UserAccount, related_name='feedback', on_delete=models.CASCADE)
    rating = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    updated_at = models.CharField(max_length=1000, blank=True, null=True)
   
    def __str__(self):
        return f"Review by {self.UserAccount.email}"



class Return(models.Model):
   
    user = models.ForeignKey(UserAccount, related_name='Return', on_delete=models.CASCADE)
    orderID = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    application = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    isviewed = models.CharField(max_length=1000, blank=True, null=True, default="no")
   
    def __str__(self):
        return f"{self.UserAccount.email}"






class Coupon(models.Model):
    
    copon = models.CharField(max_length=1000, blank=True, null=True)
    porcentage = models.CharField(max_length=1000, blank=True, null=True)
    productId = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.CharField(max_length=1000, blank=True, null=True)
    expired_at = models.CharField(max_length=1000, blank=True, null=True)
   
    def __str__(self):
        return self.copon










class ScheduledEmail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    welcome_sent = models.BooleanField(default=False)
    day1_sent = models.BooleanField(default=False)
    day2_sent = models.BooleanField(default=False)
    day3_sent = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.email






class test(models.Model):

    title = models.CharField(max_length=200)  # assuming you have a title field
    image_en = CloudinaryField('images', blank=True, null=True)
    
