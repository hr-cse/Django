# Generated by Django 2.1 on 2018-09-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnmodelform', '0002_auto_20180912_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
    ]
