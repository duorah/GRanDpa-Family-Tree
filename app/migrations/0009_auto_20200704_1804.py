# Generated by Django 3.0.7 on 2020-07-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200704_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='suffix',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
