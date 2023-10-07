from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    title = "Home"



    # services
    services = Service.objects.all()

    context = {'title': title, 'services': services}

    context.update(get_web_info())


    return render(request, 'Home.html', context)


def service(request, id):
    title = "Service"

    # get the service
    service = Service.objects.get(id=id)

    # get the plans
    plans = service.plans.all()

    context = {'title': title, 'service': service, 'plans': plans}

    context.update(get_web_info())

    return render(request, 'Service/ServiceDetail.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        # check if the rmail alredy exest
        if Subscriber.objects.filter(email=email).exists():
            return home(request)

        # save the email
        subscriber = Subscriber(email=email)
        subscriber.save()

    # rederict home
    return home(request)


def get_web_info():
    # get the web info object
    web_info = WebInfo.objects.all().first()
    # genral info :
    owner_name = web_info.owner_name
    website_name = web_info.website_name
    website_description = web_info.website_description
    website_logo = web_info.website_logo.url

    # Hero info :
    Hero_title = web_info.Hero_title
    Hero_description = web_info.Hero_description
    Hero_image = web_info.Hero_image.url

    # about info :
    about_title = web_info.about_title
    about_description = web_info.about_description
    about_image = web_info.about_image.url

    # Services info :
    Services_title = web_info.Services_title
    Services_description = web_info.Services_description


    # Portfolio info :
    Portfolio_title = web_info.Portfolio_title
    Portfolio_description = web_info.Portfolio_description

    # Contact info :
    Contact_title = web_info.Contact_title
    Contact_description = web_info.Contact_description

    Location = web_info.Location
    Email = web_info.Email
    Phone = web_info.Phone
    linkedin = web_info.linkedin
    github = web_info.github

    # return the data as json
    return {
        'owner_name': owner_name,
        'website_name': website_name,
        'website_description': website_description,
        'website_logo': website_logo,
        'Hero_title': Hero_title,
        'Hero_description': Hero_description,
        'Hero_image': Hero_image,
        'about_title': about_title,
        'about_description': about_description,
        'about_image': about_image,
        'Services_title': Services_title,
        'Services_description': Services_description,
        'Portfolio_title': Portfolio_title,
        'Portfolio_description': Portfolio_description,
        'Contact_title': Contact_title,
        'Contact_description': Contact_description,
        'Location': Location,
        'Email': Email,
        'Phone': Phone,
        'linkedin': linkedin,
        'github': github,
    }


