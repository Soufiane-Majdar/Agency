# Generated by Django 4.2.6 on 2023-10-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_alter_webinfo_contact_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='projects',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
