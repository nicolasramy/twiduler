from django.db import models


class Author(models.Model):

    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1

    STATUS_CHOICES = (
        (STATUS_INACTIVE, 'Inactive'),
        (STATUS_ACTIVE, 'Active'),
    )
    status = models.IntegerField(default=STATUS_INACTIVE, choices=STATUS_CHOICES)

    username = models.CharField(max_length=200)

    oauth_consumer_key = models.CharField(max_length=200)
    oauth_signature = models.CharField(max_length=200)
    oauth_access_token = models.CharField(max_length=200)
    oauth_access_token_secret = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)


class Tweet(models.Model):
    message = models.CharField(max_length=140)
    author = models.ForeignKey(Author)
    schedule = models.DateTimeField()

