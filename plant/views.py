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
def sign_up_by_django(request):
    error = None
    good = None
    if request.method == "POST":
        form = EmployeeRegistr(request.POST)

        if form.is_valid():
            username = form.cleaned_data['name']
            users = Employee.objects.all().values_list('name', flat=True)
            if username in users:
                error = 'Такой логин уже существует.'
            position = form.cleaned_data['position']
            boss = form.cleaned_data['boss']
            brigade = form.cleaned_data['brigade']
            if error == None:
                Employee.objects.create(name=username, position=position, boss=boss, activ = True, brigade=brigade)
                good = f'Приветствуем, {username}!'
        else:
            error = 'Форма не валидна.'
        info = {'good': good, 'error': error}
        return render(request, 'registration_page.html', info)
    else:
        form = UserRegistr()
        return render(request, 'registration_page.html')
