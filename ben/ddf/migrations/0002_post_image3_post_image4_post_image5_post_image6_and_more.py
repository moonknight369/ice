# Generated by Django 4.1.1 on 2022-09-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image5',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image6',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image7',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image8',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
