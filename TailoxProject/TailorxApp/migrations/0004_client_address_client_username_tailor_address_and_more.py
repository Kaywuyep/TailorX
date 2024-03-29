# Generated by Django 5.0.3 on 2024-03-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TailorxApp', '0003_tailor_location_tailor_tailor_pictures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='tailor',
            name='address',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='tailor',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
