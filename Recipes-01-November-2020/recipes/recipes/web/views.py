from django.shortcuts import render, redirect

from recipes.web.forms import RecipeModelForm, DeleteRecipeModelForm
from recipes.web.models import Recipe


# Create your views here.
def home_page(request):
    recipe = Recipe.objects.order_by('pk').all()
    context = {"recipes": recipe}
    return render(request, template_name='web/index.html', context=context)


def create_recipe(request):
    form_recipe = RecipeModelForm(request.POST or None)

    if form_recipe.is_valid():
        recipe = form_recipe.save(commit=False)
        recipe.save()
        return redirect("home_page")

    context = {"create_form": form_recipe}

    return render(request, "web/create.html", context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form_recipe = RecipeModelForm(instance=recipe)

    context = {"edit_form": form_recipe, "recipe": recipe}

    if request.method == "POST":
        form_recipe = RecipeModelForm(request.POST, instance=recipe)
        if form_recipe.is_valid():
            form_recipe.save()
            return redirect("home_page")

    return render(request, "web/edit.html", context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = DeleteRecipeModelForm(instance=recipe)

    if request.method == "POST":
        form = DeleteRecipeModelForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.delete()
            return redirect("home_page")

    context = {"delete_form": form, "recipe": recipe}

    return render(request, "web/delete.html", context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}

    return render(request, "web/details.html", context)
