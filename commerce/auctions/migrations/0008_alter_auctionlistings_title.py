# Generated by Django 4.0.1 on 2022-04-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auctionlistings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]