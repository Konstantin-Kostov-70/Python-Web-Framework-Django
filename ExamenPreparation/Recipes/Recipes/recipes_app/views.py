from django.shortcuts import render, redirect

from Recipes.recipes_app.forms import RecipeCreateForm, RecipeDeleteForm
from Recipes.recipes_app.models import Recipe


def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeCreateForm(instance=recipe, initial=recipe.__dict__)
    else:
        form = RecipeCreateForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe, initial=recipe.__dict__)
    else:
        recipe.delete()
        return redirect('index')
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    all_ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'all_ingredients': all_ingredients
    }
    return render(request, 'details.html', context)
