from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# category model for category of blog post
class Category(models.Model):
    name = models.CharField(max_length=100)

    # string representation of name
    def __str__(self):
        return self.name


# post model defining all Post model fields
class Post(models.Model):

    # model manager that filters posts based on status
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # category connected via foreign key to post model (defaults to category 1)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1) # PROTECT ensures if category is deleted, posts will not also be deleted
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # slug allows us to use slugify title of post to use in url/unique identifier
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') # CASCADE ensures if a user is deleted, users posts also delete
    # giving options variable for post status choice
    status = models.CharField(
        max_length=10, choices=options, default='published')

    objects = models.Manager() # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',) # order posts by descending order

        # default return title
        def __str__(self):
            return self.title
