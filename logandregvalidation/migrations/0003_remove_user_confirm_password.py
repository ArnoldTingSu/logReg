# Generated by Django 2.2 on 2021-03-30 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logandregvalidation', '0002_user_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
    ]