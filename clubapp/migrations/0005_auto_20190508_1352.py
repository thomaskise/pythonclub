# Generated by Django 2.2 on 2019-05-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0004_auto_20190508_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resourcetype',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='ResourceType',
        ),
    ]