from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class MontUser(models.Model):
    DORM_CHOICES = [
        ('page', 'Page'),
        ('emerson', 'Emerson'),
        ('clark', 'Clark'),
        ('vk', 'VK'),
        ('armington', 'Armington'),
        ('glc', 'GLC'),
        ('off campus', 'Off Campus'),
    ]

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField('User Phone', max_length=25)
    email = models.EmailField('User Email')
    dorm = models.CharField(max_length=50, choices=DORM_CHOICES)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


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
    photo = models.ImageField(upload_to='listings/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=False)

    def __str__(self):
        return self.title

