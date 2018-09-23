# Generated by Django 2.1 on 2018-09-21 18:16

from django.db import migrations, models
import mlm.models


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0003_auto_20180922_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childrentable',
            name='userId',
            field=models.ForeignKey(on_delete=mlm.models.UserTable, related_name='childrenTable', to='mlm.ChildrenTable'),
        ),
        migrations.AlterField(
            model_name='wifetable',
            name='userId',
            field=models.ForeignKey(on_delete=mlm.models.UserTable, related_name='wifeTable', to='mlm.WifeTable'),
        ),
    ]
