# Generated by Django 3.1.3 on 2021-01-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210102_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]