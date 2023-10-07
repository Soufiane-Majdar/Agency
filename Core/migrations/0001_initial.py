# Generated by Django 4.2.6 on 2023-10-07 17:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('in_progress', 'In progress'), ('completed', 'Completed'), ('pending', 'Pending')], default='in_progress', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.client')),
            ],
        ),
        migrations.CreateModel(
            name='SMTPHost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email_backend', models.CharField(blank=True, default='django.core.mail.backends.smtp.EmailBackend', max_length=255)),
                ('email_host', models.CharField(blank=True, default='smtp.gmail.com', max_length=255)),
                ('email_port', models.IntegerField(blank=True, default=587)),
                ('email_use_tls', models.BooleanField(blank=True, default=True)),
                ('email_host_password', models.CharField(blank=True, max_length=255)),
                ('email_host_user', models.EmailField(blank=True, max_length=255)),
                ('is_hosting', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('is_subscribed', models.BooleanField(default=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('rating', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Very good')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, upload_to='services/')),
                ('projects', models.ManyToManyField(blank=True, to='Core.project')),
            ],
        ),
    ]