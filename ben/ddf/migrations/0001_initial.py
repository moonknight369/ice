# Generated by Django 4.1.1 on 2022-09-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
