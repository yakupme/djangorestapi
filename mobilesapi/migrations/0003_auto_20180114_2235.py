# Generated by Django 2.0.1 on 2018-01-14 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobilesapi', '0002_auto_20180114_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilephone',
            old_name='colour',
            new_name='color',
        ),
    ]
