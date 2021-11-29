from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.contrib.auth.models import User
from accounts.models import adult, young


class post(models.Model):
    HELP_CHOICE = (
        ('אוזן קשבת', 'אוזן קשבת'),
        ('עזרה בבית', 'עזרה בבית'),
        ('עזרה בקניות', 'עזרה בקניות'),
        ('קניית תרופות', 'קניית תרופות'),
    )
    selected_help = models.CharField(
        max_length=200, null=True, choices=HELP_CHOICE)
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    phone = models.CharField(unique=False, blank=True, max_length=15)
    city = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        adult, null=True, on_delete=CASCADE, related_name='adult_post')
    youngs = models.ManyToManyField(young)

    def __str__(self):
        return self.title
