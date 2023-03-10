# Generated by Django 3.2.16 on 2022-12-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm_app', '0002_userregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('your_message', models.TextField(max_length=200)),
            ],
        ),
    ]
