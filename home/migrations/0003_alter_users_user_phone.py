# Generated by Django 4.0.4 on 2022-06-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_phone',
            field=models.IntegerField(),
        ),
    ]