from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from storages.backends.s3boto3 import S3Boto3Storage


class MontUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email_is_verified = models.BooleanField(default=False)
    phone = models.CharField('User Phone', max_length=25, default=0)
    
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_mont_user(sender, instance, created, **kwargs):
    if created:
        MontUser.objects.create(user=instance)


class MediaStorage(S3Boto3Storage):
    location = 'media/listings'
    file_overwrite = False


class Listing(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('not_great', 'Not Great'),
        ('bad', 'Bad'),
    ]

    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('dorm_related', 'Dorm Related'),
        ('clothing_accessories', 'Clothing and Accessories'),
        ('sports_outdoors', 'Sports and Outdoors'),
        ('westmont_textbooks', 'Westmont Textbooks'),
        ('other_books', 'Other Books'),
        ('music', 'Music'),
        ('automotive', 'Automotive'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    seller = models.IntegerField(blank=False, default=1)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    photo = models.ImageField(upload_to='listings/', null=True, blank=True, storage=MediaStorage())
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

