# Generated by Django 5.0.1 on 2024-02-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(blank=True, default='static/listings/default_image.jpeg', null=True, upload_to='listings /'),
        ),
    ]
