# Generated by Django 3.2.8 on 2021-11-01 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp2', '0003_auto_20211101_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
