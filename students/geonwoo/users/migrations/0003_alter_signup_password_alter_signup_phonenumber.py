# Generated by Django 4.0.2 on 2022-02-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_signup_password_alter_signup_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phoneNumber',
            field=models.CharField(max_length=30),
        ),
    ]