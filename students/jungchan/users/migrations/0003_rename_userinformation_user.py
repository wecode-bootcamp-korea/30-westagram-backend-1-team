# Generated by Django 4.0.2 on 2022-02-21 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userinformation_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInformation',
            new_name='User',
        ),
    ]
