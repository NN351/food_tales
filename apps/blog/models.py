from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='blog')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title