# Generated by Django 2.1 on 2018-09-17 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
    ]
