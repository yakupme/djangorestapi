# Generated by Django 2.0.1 on 2018-01-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made', models.CharField(max_length=20)),
                ('modelname', models.CharField(max_length=20, unique=True)),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('silver', 'silver'), ('gold', 'gold'), ('red', 'red')], max_length=20)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
