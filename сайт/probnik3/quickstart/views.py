from django.shortcuts import render
from quickstart.models import BankClients, BankWorkers, InvestType, MoneyCourse, InvestRegist
from .forms import bankClientsForm, bankWorkersForm, investTypeForm, moneyCourseForm, investRegistForm
# Create your views here.

def index_page(request):

    """ new_worker = Worker(name = "aye", second_name = "amogus", salary = 40000)
    new_worker.save()
    Worker.objects.create(name="ty", second_name="ty", salary="34000") """

    """ Worker_to_change = Worker.objects.get(id=3)
    print(Worker_to_change)
    Worker_to_change.second_name = 'sasy'
    Worker_to_change.save() """

    """ Worker.objects.filter(id=3).update(name="tycto") """

    """ all_workers = Worker.objects.all()
    print(all_workers) """

    """ Worker.objects.get(id=6).delete() """

    """ for i in all_workers:
        print(i.second_name, i.name, i.salary, i.id) """

    all_BankClients = BankClients.objects.all()
    all_BankWorkers = BankWorkers.objects.all()
    all_InvestType = InvestType.objects.all()
    all_MoneyCourse = MoneyCourse.objects.all()
    all_InvestRegist = InvestRegist.objects.all()

    

    return render(request, 'index.html', context={
        'all_BankClients':all_BankClients,
        'all_BankWorkers': all_BankWorkers,
        'all_InvestType':all_InvestType,
        'all_MoneyCourse':all_MoneyCourse,
        'all_InvestRegist':all_InvestRegist})

def bankClients(request):

    all_bankCkients = BankClients.objects.all()
    error = ''

    if request.method == 'POST':
        form = bankClientsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неправильные данные'
    form = bankClientsForm()


    data = {
        'form': form,
        'error': error
    }

    return render(request, 'bankClients.html', data)

def bankWorkers(request):

    error = ''

    if request.method == "POST":
        form = bankWorkersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Неправильные данные"
    form = bankWorkersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'bankWorkers.html', data)

def investType(request):

    error = ''

    if request.method == "POST":
        form = investTypeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Неправильные данные"
    form = investTypeForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'investType.html', data)

def moneyCourse(request):

    error = ''

    if request.method == "POST":
        form = moneyCourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Неправильные данные"
    form = moneyCourseForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'moneyCourse.html', data)

def investRegist(request):

    error = ''

    if request.method == "POST":
        form = investRegistForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Неправильные данные"
    form = investRegistForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'investRegist.html', data)