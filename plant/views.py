from django.shortcuts import render
from plant.models import *
from django.core.paginator import Paginator
from plant.forms import *
# Create your views here.
def view_plant(request):
    header = "Главная страница"
    context = {'header': header}
    return render(request, 'plant.html',context)

def view_plant_employee(request):
    header = "Работники"
    # employee = Employee.objects.all().order_by('id')
    employee = Employee.objects.select_related('brigade').all().order_by('id')
    # # создаем пагинатор
    posts_per_page = request.GET.get('posts_per_page', 3)
    paginator = Paginator(employee,posts_per_page)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page',1)

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    context = {'header': header, 'page_post': page_posts}
    return render(request, 'employee.html', context)

def sign_up_by_plant(request):
    # error = None
    # good = None
    brigades =[]
    br = Brigade.objects.all().values_list('name', flat=True)
    for b in br:
        brigades.append(b)
    if request.method == "POST":
        form = EmployeeRegistr(request.POST)
        info = {'good': None, 'error': None, 'brigades': brigades}
        if form.is_valid():
            username = form.cleaned_data['name']
            users = Employee.objects.all().values_list('name', flat=True)
            if username in users:
                error = 'Такой сотрудник уже существует.'
            position = form.cleaned_data['position']
            boss = form.cleaned_data['boss']
            brigade = form.cleaned_data['brigade']
            br = Brigade.objects.get(name=brigade).id

            print('выбор',str(br),error,username,users)
            if error == None:
                Employee.objects.create(name=username, position=position, boss=boss, activ = True, brigade_id=br)
                good = f'Приветствуем, {username}!'
                info['good'] = good
                info['error'] = error
        else:
            error = 'Форма не валидна.'
        info['error'] = error
        return render(request, 'registration_page.html', info)
    else:
        form = EmployeeRegistr()
        return render(request, 'registration_page.html')
