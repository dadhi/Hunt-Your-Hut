# Generated by Django 3.1.4 on 2020-12-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_property_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='test_field',
        ),
    ]