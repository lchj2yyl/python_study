from django.db import models


class AuthorInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super(AuthorInfo, self).__init__(*args, **kwargs)


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(AuthorInfo)

    def __str__(self):
        return self.title.encode('utf-8')


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    content = models.CharField(max_length=1000)
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.name.encode('utf-8')

