# Generated by Django 3.0.7 on 2020-07-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200705_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='given_name',
            new_name='given',
        ),
        migrations.AddField(
            model_name='person',
            name='sibling',
            field=models.ManyToManyField(blank=True, related_name='_person_sibling_+', to='app.Person'),
        ),
    ]
