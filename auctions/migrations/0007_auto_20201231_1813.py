# Generated by Django 3.1.3 on 2020-12-31 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_starting_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
