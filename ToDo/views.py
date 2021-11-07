from django.shortcuts import render, get_list_or_404
from .models import Task
from .forms import task_form
from django.shortcuts import redirect

# Create your views here.
# render generuje strone
# sciezke zaczynamy juz od templates

def task_list(request):

    tasks = Task.objects.all()
    pending_count = Task.objects.filter(status=True).count()
    if request.method == 'POST':
        form = task_form(request.POST)                  #utworzenie wypelnionego formularza na podstawie tego co jest w request.POST
        if form.is_valid():                              #sprawdzamy czy formularz jest wypelniony poprawnie
            new_task = form.save(commit = False)
            new_task.save()                                               # tu mozemy dolozyc inne wartosci do obiektu ktory zaraz zapisze w bazie


    else:
        form = task_form() # jesli nic nie wysylamy formularzem bo dopiero ladujemy strone to tylko go pokazujemy formularz z forms.py

    return render(request,'ToDo/Task/task_list.html',
                  {'tasks': tasks,'form':form, 'pending_count':pending_count} # zmienne ktore chce przekazac w tym szablonie
                  )

def change_status(request, pk):
    task_to_change = Task.objects.get(id=pk)
    if task_to_change.status == True:

        task_to_change.status = False
    else:
        task_to_change.status = True
    task_to_change.save()
    return redirect('ToDo:task_list')


def delete_task(request, pk):
    task_to_delete = Task.objects.get(id=pk)

    task_to_delete.delete()
    return redirect('ToDo:task_list')

def mark_all_done(request):

    task_to_change = Task.objects.all()
    task_to_change.update(status=False)
    return redirect('ToDo:task_list')

def delete_all(request):

    task_to_delete = Task.objects.all()
    task_to_delete.delete()
    return redirect('ToDo:task_list')