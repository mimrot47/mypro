# Generated by Django 3.0.5 on 2020-06-16 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200616_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]
