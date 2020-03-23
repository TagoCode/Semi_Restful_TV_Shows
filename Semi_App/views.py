from django.shortcuts import render, redirect
from .models import *
# Create your views here.



def listShows(request):
    context = {
        "list_of_things": Shows.objects.all()
        # ^ this gets all show objects out of the database, and sets them as "list_of_things" to be used in HTML
    }
    return render(request, 'shows.html', context)

def addshow(request):
    return render(request, 'new.html')

def edit(request, show_id):
    context = {
        "this_show": Shows.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def viewShow(request, show_id):
    context = {
    "this_show": Shows.objects.get(id=show_id)
}
    return render(request, 'viewshow.html', context)


def createShow(request):
    # request.POST contains the information from the form itself
    title_from_form = request.POST['title']
    network_from_form = request.POST['network']
    date_from_form = request.POST['date']
    description_from_form = request.POST['desc']

    # code for creating an entry in the database
    # so now we need to create a show object with ^^ information
    Shows.objects.create(show_title=title_from_form, network=network_from_form, date=date_from_form, description=description_from_form)
    # ^ this is the code that ACTUALLY creates an entry in our database
    return redirect('/')


def updateCreateShow(request, show_id):
    show_to_edit = Shows.objects.get(id=show_id)
    show_to_edit.show_title = request.POST['title'] # These three fields
    show_to_edit.network = request.POST['network']  # need to be in the 
                                                    # form you create
    show_to_edit.description = request.POST['desc']
    show_to_edit.save()

    return redirect('/')

def deleteShow(request, show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect("/")