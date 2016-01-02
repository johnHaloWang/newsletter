from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.contrib.sites.requests import RequestSite
from .models import SignUp



def about(request):
    return render(request, "newsletter/about.html", {})

def index(request):
    return render(request, "newsletter/index.html", {})

def home(request):
    title = 'Sign Up Now'
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)
    # if request.method == "POST":
    #     print(request.POST)

    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        #form.save()
        #print(request.POST['email'])
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }
        # print(instance)
    if request.user.is_authenticated() and request.user.is_staff:
        i = 1
        # for instance in SignUp.objects.all():
        #     print(i)
        #     print(instance.full_name)
        #
        #     i+=1
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }

    return render(request, 'newsletter/home.html', context)

def contact(request):
    title = "Contact Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
         # for key,value in form.cleaned_data.items():
         #    print(key, value)
            # print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, "youotheremail@email.com"]
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  fail_silently=False)
        # print(email, message, full_name)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "newsletter/forms.html", context)