# Generated by Django 3.2.8 on 2024-09-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemTrade', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='dormitory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facauty',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
