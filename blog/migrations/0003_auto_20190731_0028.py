# Generated by Django 2.2.1 on 2019-07-30 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190526_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='writer',
            new_name='body',
        ),
    ]
