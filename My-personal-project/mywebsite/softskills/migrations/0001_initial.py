# Generated by Django 4.0.6 on 2022-08-05 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soft_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
