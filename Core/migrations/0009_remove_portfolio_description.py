# Generated by Django 4.2.6 on 2023-10-08 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
    ]
