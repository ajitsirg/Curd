# Generated by Django 4.0.5 on 2022-11-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='companyName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='gstNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='panCard',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='panImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
