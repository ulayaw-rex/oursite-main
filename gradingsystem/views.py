from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Gender, User, Teacher
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def index_login(request):
    teachers = Teacher.objects.all()
    return render(request, 'login/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')  # redirect to home page after login
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login/index.html', {'error_message': error_message})
            pass
    return render(request, 'login/index.html')

def index_gender(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders
    }
    return render(request, 'gender/index.html', context)

def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) #insert into genders(gender) values(gender)
    messages.success(request, 'Gender successfully saved!')
    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #SELECT * FROM genders WHERE gender_id = gender_id

    context = {
        'gender': gender,
    }

    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender': gender,
    }

    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')

    Gender.objects.filter(pk=gender_id).update(gender=gender) #UPDATE genders SET gender = gender WHERE gender_id = gender_id
    messages.success(request, 'Gender Successfully Saved')


    return redirect("/genders")

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender': gender,
    }

    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() # DELETE FROM genders WHERE gender_id = gender_id
    messages.success(request, 'Gender Successfully Deleted')

    return redirect('/genders')

def index_user(request):
    users = User.objects.select_related('gender') #SELECT * FROM users LEFT JOIN genders ON users.gender_id = genders.gender_id

    context = {
        'users': users
    }

    return render(request, 'user/index.html', context)

def create_user(request):
    genders = Gender.objects.all() #SELECT * FROM genders

    context = {
        'genders': genders
    }
    return render(request, 'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lasttName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    math = request.POST.get('math')
    science = request.POST.get('science')
    english = request.POST.get('english')
    filipino = request.POST.get('filipino')
    history = request.POST.get('history')
    homeroom = request.POST.get('homeroom')
    User.objects.create(first_name=firstName, middle_name=middleName, last_name=lasttName, age=age, birth_date=birthDate, gender_id=genderId, math=math, science=science, english=english, filipino=filipino, history=history, homeroom=homeroom)
    messages.success(request, 'User successfully saved.')
    return redirect('user')
    
def show_user(request, student_id):
    user = User.objects.get(pk=student_id) 

    context = {
        'user': user,
    }

    return render(request, 'user/show.html', context)

def delete_user(request, student_id):
    user = User.objects.get(pk=student_id)

    context = {
        'user': user,
    }

    return render(request, 'user/delete.html', context)

def destroy_user(request, student_id):
    User.objects.filter(pk=student_id).delete() # DELETE FROM genders WHERE gender_id = gender_id
    messages.success(request, 'User Successfully Deleted')

    return redirect('user')

def edit_user(request, student_id):
    genders = Gender.objects.all()
    user = User.objects.select_related('gender').get(pk=student_id)

    context = {
        'genders': genders,
        'user': user,
    }

    return render(request, 'user/edit.html', context)

def update_user(request, student_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lasttName = request.POST.get('last_name')
    age = request.POST.get('age')
    genderId = request.POST.get('gender_id')
    math = request.POST.get('math')
    science = request.POST.get('science')
    english = request.POST.get('english')
    filipino = request.POST.get('filipino')
    history = request.POST.get('history')
    homeroom = request.POST.get('homeroom')

    User.objects.filter(pk=student_id).update(first_name=firstName, middle_name=middleName, last_name=lasttName, age=age, gender_id=genderId, math=math, science=science, english=english, filipino=filipino, history=history, homeroom=homeroom)
    messages.success(request, 'Gender Successfully Saved')


    return redirect("user")

def create_sign_up(request):
    teachers = Teacher.objects.all()

    return render(request, 'login/signup.html')

def store_sign_up(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

    if password == confirmPassword:
        Teacher.objects.create(username=username, password=make_password(password))

        messages.success(request, 'Your account is successfully saved.')

        return redirect('/')
    else:
        messages.error(request, 'Password do not match.')
        return redirect('teacher/create')