# Generated by Django 4.0.6 on 2022-08-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technical_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
