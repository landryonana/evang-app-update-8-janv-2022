# Generated by Django 2.2.24 on 2021-12-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evangelisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
