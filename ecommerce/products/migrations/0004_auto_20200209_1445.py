# Generated by Django 3.0.3 on 2020-02-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200209_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='nazwa',
            new_name='name',
        ),
    ]
