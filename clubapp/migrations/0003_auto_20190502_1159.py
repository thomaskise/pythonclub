# Generated by Django 2.2 on 2019-05-02 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0002_auto_20190423_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minutes',
            old_name='meetingagenda',
            new_name='meetingminutes',
        ),
    ]
