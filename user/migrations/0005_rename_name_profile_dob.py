# Generated by Django 5.2.3 on 2025-06-20 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='dob',
        ),
    ]
