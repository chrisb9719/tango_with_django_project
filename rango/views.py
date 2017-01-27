from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    #Query the database for a list of ALL categories currently stored.
    #Prder the categories by no. likes in descending order.
    #Retrive the top 5 only - or all if less than 5.
    #Place the list in our context_dict dictionary
    #that will be passed to the template engine.

    category_list = Categroy.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    #Render a response and send it back!
    return render(request, 'rango/index.html', context_dict)

    # Construct a dictionary to pass ro the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the template!

    # Return a redndered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    #  Note that the first parameter is the template we wish to use.
