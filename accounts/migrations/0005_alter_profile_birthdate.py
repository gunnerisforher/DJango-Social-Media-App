# Generated by Django 4.1.2 on 2022-10-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
