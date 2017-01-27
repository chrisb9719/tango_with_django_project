from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Prder the categories by no. likes in descending order.
    # Retrive the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render a response and send it back!
    return render(request, 'rango/index.html', context_dict)

    # Construct a dictionary to pass ro the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the template!

    # Return a redndered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    #  Note that the first parameter is the template we wish to use.


def show_category(request, category_name_slug):
        # Create a context dictionary which wwe can pass
        # to the template rendering engine.
        context_dict = {}

        try:
            # Can we find a category name slug with the given name?
            # If we can't, the .get() method raises a DoesNotExist exception.
            #So the .get() method returns one model instance or raises an exception.
            category = Category.objects.get(slug=category_name_slug)

            #Retireve all of the associated pages.
            #Note that filter() will return a list of page objects or an empty list.
            pages=Page.objects.filter(category=category)

            #Adds our results list to the template context under name pages.
            context_dict['pages'] = pages
            #We also add the category object from
            #the database to the context dictionary
            #We'll use this in the template to verify tat the category exists
            context_dict['category'] = category
        except Category.DoesNotExist:
            #we get here if we didn't find the specified category
            #Don't do anything -
            #The template will display the "no category" message for us.
            context_dict['category'] = None
            context_dict['pages'] = None

        #Go render the response and return it to the client
        return render(request, 'rango/category.html', context_dict)