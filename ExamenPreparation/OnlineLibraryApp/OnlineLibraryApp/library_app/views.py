from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from OnlineLibraryApp.library_app.forms import ProfileCreateForm, BookCreateForm, ProfileDeleteForm
from OnlineLibraryApp.library_app.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except ObjectDoesNotExist:
        return None


def index(request):
    user_profile = get_profile()
    all_books = Book.objects.all()
    if user_profile is None:
        if request.method == 'GET':
            form = ProfileCreateForm()
            context = {
                'form': form,
                'not_profile': True
            }
            return render(request, 'home-no-profile.html', context)
        else:
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('index')
    context = {
        'all_books': all_books,
        'user_profile': user_profile
        }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookCreateForm(instance=book, initial=book.__dict__)
    else:
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'book': book,
        'form': form
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def profile_page(request):
    user_profile = get_profile()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    user_pofile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm(instance=user_pofile, initial=user_pofile.__dict__)
    else:
        form = ProfileCreateForm(request.POST, instance=user_pofile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    user_pofile = get_profile()
    all_books = Book.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=user_pofile, initial=user_pofile.__dict__)
    else:
        user_pofile.delete()
        all_books.delete()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'delete-profile.html', context)
