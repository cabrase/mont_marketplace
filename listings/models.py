from django.db import models


class MontUser(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField('User Phone', max_length=25)
    email = models.EmailField('User Email')
    dorm = models.CharField(max_length=50)
    
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
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    seller = models.ForeignKey(MontUser, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    photo = models.ImageField(upload_to='listings/', null=True, blank=True)
    is_active = models.BooleanField()
    date_created = models.DateField('Date Posted')

    def __str__(self):
        return self.title

