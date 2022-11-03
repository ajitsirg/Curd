# Generated by Django 4.0.5 on 2022-11-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coustmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.DateField()),
                ('phone', models.IntegerField(max_length=11, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=35, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
