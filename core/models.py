from django.db import models

class PostCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategory,
                                 blank = True,
                                 null = True,
                                 on_delete=models.SET_NULL,
                                 related_name='category_post')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title

class PostComment(models.Model):
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='post_comments')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:10]