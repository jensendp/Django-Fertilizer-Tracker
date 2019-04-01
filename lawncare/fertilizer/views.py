from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Fertilizer, Application, ApplicationAmount
from decimal import Decimal

def index(request):
    applications = Application.objects.all()
    application_amounts = []
    for application in applications:
        application_amounts.append(get_application_amounts(application))

    context = {
        'applicationAmounts': application_amounts
    }

    return render(request, 'fertilizer/index.html', context)

def get_application_amounts(application):
    bag_weight = application.Fertilizer.bag_weight
    bag_coverage = application.Fertilizer.bag_coverage
    lbs_per_k = round(bag_weight / (bag_coverage / 1000), 1)
    applied_n = round((application.Fertilizer.percent_N * Decimal(lbs_per_k)) / 100, 2)
    applied_p = round((application.Fertilizer.percent_P * Decimal(lbs_per_k)) / 100, 2)
    applied_k = round((application.Fertilizer.percent_K * Decimal(lbs_per_k)) / 100, 2)

    return ApplicationAmount(application, applied_n, applied_p, applied_k)

def fertilizers(request):
    fertilizers = Fertilizer.objects.all()
    context = {
        'fertilizers': fertilizers
    }
    return render(request, 'fertilizer/fertilizers.html', context)

def detail(request, fert_id):
    try:
        fertilizer = Fertilizer.objects.get(pk=fert_id)
        context = { 'fertilizer': fertilizer }
    except Fertilizer.DoesNotExist:
        raise Http404("Fertilizer does not exist")
    return render(request, 'fertilizer/fertilizer.html', context)

def apply(request, fert_id):
    fertilizer = Fertilizer.objects.get(pk=fert_id)
    bags = request.POST['bags']
    date = request.POST['date']

    fertilizer.application_set.create(bags_applied=bags, date_applied=date)
    return HttpResponseRedirect('/fert')