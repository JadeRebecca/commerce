# Generated by Django 3.1.3 on 2020-12-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201229_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, default='0.1', max_digits=5),
        ),
    ]
