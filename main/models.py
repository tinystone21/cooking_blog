from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey(
        'self', related_name='children',
        null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='recipes'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes'
    )
    created = models.DateTimeField()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})


class Image(models.Model):
    image = models.ImageField(upload_to='recipes')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='images'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.user.email
