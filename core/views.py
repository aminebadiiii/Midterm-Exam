from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, TextbookForm
from .models import Textbook
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    # Retrieve unique course codes from the Textbook model
    course_codes = Textbook.objects.values_list('course_code', flat=True).distinct()
    print(course_codes)
    return render(request, 'home.html', {
        'course_codes': course_codes,
    })
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect('my_textbooks')  # Redirect to the "My Textbooks" page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def student_logout(request):
    # Log out the user
    logout(request)

    # Display a success message
    messages.success(request, 'You have been successfully logged out.')

    # Redirect to the login page (or home page)
    return redirect('login')


def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            # Display form errors
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def add_textbook(request):
    if request.method == 'POST':
        form = TextbookForm(request.POST)
        if form.is_valid():
            textbook = form.save(commit=False)
            textbook.owner = request.user  # Assign the logged-in student as the owner
            textbook.save()
            messages.success(request, 'Textbook added successfully!')
            return redirect('my_textbooks')  # Redirect to "My Textbooks" page
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TextbookForm()

    return render(request, 'add_textbook.html', {'form': form})


@login_required
def my_textbooks(request):
    # Retrieve all textbooks owned by the logged-in student
    textbooks = Textbook.objects.filter(is_available=True)

    return render(request, 'my_textbooks.html', {'textbooks': textbooks})


@login_required
def textbook_list_by_course(request, course_code):
    # Retrieve all available textbooks for the specified course code
    textbooks = Textbook.objects.filter(course_code=course_code, is_available=True)

    if not textbooks.exists():
        messages.info(request, f"No textbooks are currently available for the course {course_code}.")

    return render(request, 'textbook_list.html', {
        'course_code': course_code,
        'textbooks': textbooks
    })


@login_required
def delete_textbook(request, textbook_id):
    # Retrieve the textbook by ID or return a 404 error if it doesn't exist
    textbook = get_object_or_404(Textbook, id=textbook_id)

    # Ensure the logged-in user owns the textbook
    if textbook.owner != request.user:
        messages.error(request, 'You do not have permission to delete this textbook.')
        return redirect('my_textbooks')

    # Delete the textbook
    textbook.delete()
    messages.success(request, 'Textbook deleted successfully.')

    # Redirect back to the "My Textbooks" page
    return redirect('my_textbooks')