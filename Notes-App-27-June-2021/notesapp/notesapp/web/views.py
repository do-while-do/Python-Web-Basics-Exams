from django.shortcuts import render, redirect

from notesapp.web.forms import ProfileModelForm, NoteModelForm, DeleteNoteModelForm
from notesapp.web.models import Profile, Note


def home_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.order_by('pk').all()
    form = ProfileModelForm()

    if request.method == "POST":
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home_page")

    context = {"notes": notes, "add_form": form, "profile": profile}

    return render(request, template_name="web/home-with-profile.html", context=context)


def add_note(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('home_page')

    form = NoteModelForm(request.POST or None)

    if form.is_valid():
        note = form.save(commit=False)
        note.profile = profile
        note.save()
        return redirect("home_page")

    context = {"profile": profile, "add_form": form}

    return render(request, "web/note-create.html", context)


def edit_note(request, pk):
    profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    form = NoteModelForm(instance=note)

    context = {"edit_form": form, "profile": profile, "note": note}

    if request.method == "POST":
        form = NoteModelForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home_page")

    return render(request, "web/note-edit.html", context)


def delete_note(request, pk):
    profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    form = DeleteNoteModelForm(instance=note)

    if request.method == "POST":
        form = DeleteNoteModelForm(request.POST, instance=note)
        if form.is_valid():
            note.delete()
            return redirect("home_page")

    context = {"delete_form": form, "profile": profile, "note": note}

    return render(request, "web/note-delete.html", context)


def details_note(request, pk):
    profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)
    context = {"profile": profile, "note": note}

    return render(request, "web/note-details.html", context)


def profile_view(request):
    context = {
        "profile": Profile.objects.first()
    }

    return render(request, "web/profile.html", context)


def profile_delete(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('home_page')

    return render(request, "web/profile.html")
