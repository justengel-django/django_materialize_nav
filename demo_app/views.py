from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BasicForm, MaterializeForm
from .tables import BasicTable


def get_nav_context():
    """Using get nav context method is not a reliable as changing the settings! This will change all of the views
    with this context, but will not change other views like the login page. Use the settings to change the login page.
    """
    context = {'site_name': 'demo_app', 'PRIMARY_COLOR': 'teal', 'SECONDARY_COLOR': 'purple'}
    return context


def basic_content(request):
    context = get_nav_context()

    context['title'] = 'Basic Content'
    context['FIXED_SIDENAV'] = True

    return render(request, 'demo/basic_content.html', context)


def basic_table(request):
    context = get_nav_context()
    context['LINK_COLOR'] = 'purple lighten-2'

    context['title'] = 'Basic Table'
    context['FIXED_SIDENAV'] = True

    table = [{'name': 'Item ' + str(i), 'number': i, 'link': 'Link ' + str(i), 'button': 'Button ' + str(i)}
             for i in range(100)]
    context['table'] = BasicTable(table)

    return render(request, 'demo/basic_table.html', context)


def basic_form(request):
    context = get_nav_context()

    context['title'] = 'Basic Form'
    context['FIXED_SIDENAV'] = False

    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'The form was submitted successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'The form had errors!')
    else:
        form = BasicForm(initial=request.GET)

    context['form'] = form

    return render(request, 'demo/basic_form.html', context)


def materialize_form(request):
    context = get_nav_context()

    context['title'] = 'Materialize Form'
    context['FIXED_SIDENAV'] = False

    if request.method == "POST":
        form = MaterializeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['check_value']:
                messages.add_message(request, messages.SUCCESS, 'The form was submitted successfully!')
            else:
                messages.add_message(request, messages.WARNING, 'The checkbox was not checked!')
        else:
            messages.add_message(request, messages.ERROR, 'The form had errors!')
    else:
        form = MaterializeForm(initial=request.GET)

    context['form'] = form

    return render(request, 'demo/basic_form.html', context)
