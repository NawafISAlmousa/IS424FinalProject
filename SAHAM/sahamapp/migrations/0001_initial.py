# Generated by Django 5.0.1 on 2024-05-18 13:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('freelancerId', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(6)])),
                ('description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(3)])),
                ('phonenumber', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceId', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='sahamapp.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('userName', models.CharField(max_length=32, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3)])),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(6)])),
                ('bookedServices', models.ManyToManyField(blank=True, related_name='customers', to='sahamapp.service')),
            ],
        ),
    ]