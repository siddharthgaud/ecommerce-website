# Generated by Django 5.0 on 2024-07-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image1',
            field=models.ImageField(upload_to='uploads/slider/'),
        ),
    ]
