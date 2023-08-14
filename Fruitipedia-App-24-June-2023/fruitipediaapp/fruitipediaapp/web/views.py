from django.shortcuts import render, redirect

from fruitipediaapp.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from fruitipediaapp.web.models import Profile, Fruit


# Create your views here.


def home_page(request):
    return render(request, template_name="web/index.html")


def dashboard_page(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.order_by('pk').all()

    context = {"fruits": fruits, "profile": profile}

    return render(request, template_name="web/dashboard.html", context=context)


def fruit_create(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('profile_create')

    form = FruitCreateForm(request.POST or None)

    if form.is_valid():
        fruit = form.save(commit=False)
        fruit.profile = profile
        fruit.save()
        return redirect("dashboard_page")

    context = {"profile": profile, "add_form": form}

    return render(request, "web/create-fruit.html", context)


def fruit_details(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.get(pk=pk)
    context = {"profile": profile, "fruit": fruit}

    return render(request, "web/details-fruit.html", context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitEditForm(instance=fruit)

    if request.method == "POST":
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("dashboard_page")

    context = {"edit_form": form, "fruit": fruit}
    return render(request, "web/edit-fruit.html", context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitDeleteForm(instance=fruit)

    if request.method == "POST":
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("dashboard_page")

    context = {"delete_form": form, "fruit": fruit}
    return render(request, "web/delete-fruit.html", context)


def profile_create(request):
    profile = Profile.objects.first()
    form = ProfileCreateForm()

    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_page")

    context = {"add_form": form, "profile": profile}

    return render(request, template_name="web/create-profile.html", context=context)


def profile_details(request):
    context = {
        "profile": Profile.objects.first()
    }

    return render(request, "web/details-profile.html", context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(instance=profile)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    context = {"form": form, "fruit": profile, }
    return render(request, "web/edit-profile.html", context)


def profile_delete(request):
    profile = Profile.objects.first()
    form = ProfileDeleteForm(instance=profile)

    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home_page")

    context = {"delete_form": form, "profile": profile}
    return render(request, "web/delete-profile.html", context)
