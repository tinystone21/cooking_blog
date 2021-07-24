from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, DeleteView, FormView,
                                  CreateView)

from main.forms import RecipeForm, ImageForm, CommentForm, UserRegistrationForm
from main.models import Recipe, Comment, Category, Image


class MainPageView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.filter(category_id=self.slug)
        return context


class RecipeDetailView(DetailView, FormView):
    model = Recipe
    template_name = 'recipe-detail.html'
    context_object_name = 'recipe'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        print(request.POST)
        recipe = self.get_object()
        Comment.objects.create(
            recipe=recipe, user=request.user,
            text=request.POST['text']
        )
        return HttpResponseRedirect(self.get_object().get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image.id)
        return context


def add_recipe(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = ImageFormSet(
            request.POST, request.FILES,
            queryset=Image.objects.none()
        )
        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, recipe=recipe)
            return redirect(recipe.get_absolute_url())
    else:
        recipe_form = RecipeForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add-recipe.html', locals())


def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    formset = ImageFormSet(
        request.POST or None, request.FILES or None,
        queryset=Image.objects.filter(recipe=recipe)
    )

    if recipe_form.is_valid() and formset.is_valid():
        recipe = recipe_form.save()

        for form in formset:
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
        return redirect(recipe.get_absolute_url())
    return render(request, 'update-recipe.html', locals())


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Successfully deleted'
        )
        return HttpResponseRedirect(success_url)


class CommentCreateView(FormView):
    model = Comment
    template_name = 'add-comment.html'


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration-detail.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print('yes')
        super(UserRegistrationView, self).form_valid(form)
        return redirect('home')

    def form_invalid(self, form):
        print('no')
        form.save()
        super(UserRegistrationView, self).form_invalid(form)
        return redirect('home')
