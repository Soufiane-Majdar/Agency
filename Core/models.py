from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100  ,blank=True)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    # project_history my have many projects
    # project_history = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item = models.CharField(max_length=150)
    checked = models.BooleanField(default=True)

    def __str__(self):
        return self.item

# plan for Serveces
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    recommended = models.BooleanField(default=False, blank=True)

    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='services/', blank=True)
    icon = models.CharField(max_length=150,blank=True)
    plans = models.ManyToManyField(Plan, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, blank=True, null=True)

    STATUS_CHOICES = (
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')

    def __str__(self):
        return self.title









class Testimonial(models.Model):
    client = models.ForeignKey(Client,blank=True, null=True,on_delete=models.CASCADE)
    content = RichTextField()
    date = models.DateField(default=timezone.now)
    RATING_CHOICES = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Very good'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.client.name



class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
        

# Portfolio Model
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # description = RichTextField()
    image = models.ImageField(upload_to='portfolio/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(max_length=100)
    is_subscribed = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email





# SMTP_Host
class SMTPHost(models.Model):
    id = models.AutoField(primary_key=True)
    email_backend = models.CharField(max_length=255, default='django.core.mail.backends.smtp.EmailBackend',blank=True)
    email_host = models.CharField(max_length=255, default='smtp.gmail.com',blank=True)
    email_port = models.IntegerField(default=587,blank=True)
    email_use_tls = models.BooleanField(default=True,blank=True)
    email_host_password = models.CharField(max_length=255,blank=True)
    email_host_user = models.EmailField(max_length=255,blank=True)
    is_hosting = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"SMTPHost {self.id} - {self.email_host_user}"





# WebIfo Model to store website information like title, description, etc. you can make one object of this model
class WebInfo(models.Model):
    owner_name = models.CharField(max_length=150,default='Soufiane Majdar')
    website_name = models.CharField(max_length=150,default='Agency')
    website_description = RichTextField(null=True, blank=True)
    website_logo = models.ImageField(upload_to='WebInfo/', null=True, blank=True)


    Hero_title = models.CharField(max_length=150)
    Hero_description = RichTextField(null=True, blank=True)
    Hero_image = models.ImageField(upload_to='WebInfo/', null=True, blank=True)

    about_title = models.CharField(max_length=150)
    about_description = RichTextField(null=True, blank=True)
    about_image = models.ImageField(upload_to='WebInfo/', null=True, blank=True)

    Services_title = models.CharField(max_length=150)
    Services_description = RichTextField(null=True, blank=True)


    Portfolio_title = models.CharField(max_length=150)
    Portfolio_description = RichTextField(null=True, blank=True)

    Testimonial_title = models.CharField(max_length=150,blank=True)
    Testimonial_description = RichTextField(null=True, blank=True)

    Contact_title = models.CharField(max_length=150)
    Contact_description = RichTextField(null=True, blank=True)

    Location = models.TextField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True, max_length=254)
    Phone = models.CharField(null=True, blank=True, max_length=20)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.website_name

    # making only one object of this model
    def save(self, *args, **kwargs):
        if not self.pk and WebInfo.objects.exists():
            raise ValidationError('There is can be only one WebInfo instance')
        return super(WebInfo, self).save(*args, **kwargs)
