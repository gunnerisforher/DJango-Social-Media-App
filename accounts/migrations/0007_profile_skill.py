# Generated by Django 4.1.2 on 2022-10-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]