from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    title = "Home"



    # services
    services = Service.objects.all()

    #get portfolios
    portfolios = Portfolio.objects.all()

    # get all categories of the portfolios
    P_Category = []
    for portfolio in portfolios:
        if portfolio.category not in P_Category:
            P_Category.append(portfolio.category)

    # get the testimonials
    testimonials = Testimonial.objects.all()

    print(testimonials)


    context = {'title': title, 'services': services, 'portfolios': portfolios, 'P_Category': P_Category, 'testimonials': testimonials}

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


# contact
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # save the contact form
        contact_form = ContactForm(name=name, subject=subject, email=email, message=message)
        contact_form.save()
    
    return home(request)





## login as client
def login(request):

    title="Login"
    context={'title':title}

    # if the method is post
    if request.method == 'POST':
        # get the username and password
        username = request.POST['username']
        password = request.POST['password']

        # check if the client exists
        if Client.objects.filter(username=username).exists():
            # get the client
            client = Client.objects.get(username=username)

            # check if the password is correct
            if client.password == password:
                # login the client
                request.session['client_id'] = client.id
                return home(request)
            else:
                context['error'] = 'Password is incorrect'
                # add get_web_info
                context.update(get_web_info())
                # return the login page with error
                return render(request, 'User/login.html', context)
        else:
            context['error'] = 'Client not found'
            # add get_web_info
            context.update(get_web_info())
            # return the login page with error
            return render(request, 'User/login.html', context)

    context.update(get_web_info())
    # if the method is get
    return render(request, 'User/login.html', context)


def signup(request):

    title="Register"
    context={'title':title}

    # if the method is post
# get the data : [full_name,username,email,password,phone,company]

    if request.method == 'POST':
        # get the data
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        company = request.POST['company']

        # check if the username or email already exists
        if Client.objects.filter(username=username).exists() or Client.objects.filter(email=email).exists():
            context['error'] = 'Username or email already exists'
            # add get_web_info
            context.update(get_web_info())
            # return the login page with error
            return render(request, 'User/signup.html', context)

        # save the client
        client = Client(name=full_name, username=username, email=email, password=password, phone_number=phone, company_name=company)
        client.save()

        # login the client
        request.session['client_id'] = client.id
        return home(request)



    else:
        context.update(get_web_info())
        # if the method is get
        return render(request, 'User/signup.html', context)


# logout
def logout(request):
    # delete the session
    del request.session['client_id']

    # return home
    return home(request)

# client dashboard
def dashboard(request):
    title="Dashboard"
    context={'title':title}
   # if client not logged in
    if 'client_id' not in request.session:
        return login(request)

    # get all the projects where the client is the owner
    projects = Project.objects.filter(client=request.session['client_id'])

    client = Client.objects.get(id=request.session['client_id'])

    context['projects'] = projects
    context['client'] = client

    context.update(get_web_info())

    return render(request, 'User/dashboard.html', context)
    







# Order a project plan 
def order(request, id):
    # if client is not logged in
    if 'client_id' not in request.session:
        return login(request)
    
    # if the Project already exists
    if Project.objects.filter(client=request.session['client_id'], plan=id).exists():
        return dashboard(request)
    
        # get the client
    client = Client.objects.get(id=request.session['client_id'])

    # get the plan
    plan = Plan.objects.get(id=id)

    # get the Service which the plan belongs to
    service = plan.service_set.all().first()

    # create the order by creating a Project
    project = Project(title=service.name+' - '+plan.name, description=service.description, client=client, plan=plan)
    project.save()

    # return the dashboard  
    return dashboard(request)














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

    # Testimonial info :
    Testimonial_title = web_info.Testimonial_title
    Testimonial_description = web_info.Testimonial_description

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
        'Testimonial_title': Testimonial_title,
        'Testimonial_description': Testimonial_description,
        'Contact_title': Contact_title,
        'Contact_description': Contact_description,
        'Location': Location,
        'Email': Email,
        'Phone': Phone,
        'linkedin': linkedin,
        'github': github,
    }
