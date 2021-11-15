from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Post(models.Model):
    number = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.SET_NULL)

    # class Meta:
    #     permissions = [
    #         ('can_answer', 'Can Answer')
    #     ]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.number.__str__()
        return self.title
        return self.text

class Comment(models.Model):
  number = models.AutoField(verbose_name='댓글 번호',primary_key=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)

