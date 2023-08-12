from django.shortcuts import render, redirect

from online_library.web.forms import ProfileModelForm, BookModelForm, UserEditForm, UserDeleteForm
from online_library.web.models import Profile, Book


# Create your views here.


def home_page(request):
    profile = Profile.objects.first()
    books = Book.objects.order_by('pk').all()
    form = ProfileModelForm()

    if request.method == "POST":
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home_page")

    context = {"books": books, "add_form": form, "profile": profile}

    return render(request, template_name="web/home-with-profile.html", context=context)


def add_book(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('home_page')

    form = BookModelForm(request.POST or None)

    if form.is_valid():
        book = form.save(commit=False)
        book.profile = profile
        book.save()
        return redirect("home_page")

    context = {"profile": profile, "add_form": form}

    return render(request, "web/add-book.html", context)


def edit_book(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    form = BookModelForm(instance=book)

    context = {"edit_form": form, "profile": profile, "book": book}

    if request.method == "POST":
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("home_page")

    return render(request, "web/edit-book.html", context)


def book_details(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    context = {"profile": profile, "book": book}

    return render(request, "web/book-details.html", context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("home_page")


def profile_page(request):
    context = {
        "profile": Profile.objects.first()
    }

    return render(request, "web/profile.html", context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = UserEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_page')
    context = {
        "form": form,
    }
    return render(request, 'web/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = UserDeleteForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('home_page')
    context = {
        "form": form,
    }

    return render(request, "web/delete-profile.html", context)
