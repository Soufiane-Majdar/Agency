# Generated by Django 4.2.6 on 2023-10-08 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_webinfo_testimonial_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.client'),
        ),
    ]