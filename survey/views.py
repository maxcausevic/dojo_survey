from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')
def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['form_name']
    location_from_form = request.POST['form_location']
    language_from_form = request.POST['form_language']
    comments_from_form = request.POST['form_comments']
    context = {
        "form_name" : name_from_form,
        "form_location": location_from_form,
        "form_language" : language_from_form,
        "form_comments" : comments_from_form
    }
    return render(request,"show.html", context)

