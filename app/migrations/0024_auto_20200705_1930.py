# Generated by Django 3.0.7 on 2020-07-05 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200705_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_id',
            new_name='personid',
        ),
    ]
