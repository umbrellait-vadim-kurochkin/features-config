from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Stream(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)]) #min_length=3
    project_code = models.UUIDField(default="84989767-80db-4b66-b45b-ca4454d49d8a", editable=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title

class Feature(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    #changed_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=30) #min_length=3, 
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    feature = models.ForeignKey('self', related_name='feature_id', on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    environment = models.PositiveSmallIntegerField()
    default_value = models.PositiveSmallIntegerField()
    rollout_threshold = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    changed_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.title

class Condition(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    #changed_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=30) #min_length=3, 
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE) # * to *
    description = models.TextField()
    value = models.PositiveSmallIntegerField()
    #rollout_threshold = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    changed_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.title

class Parameter(models.Model):
    title = models.CharField(max_length=30)
    data_type = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

class Operator(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class ExpressionValue(models.Model):
    title = models.CharField(max_length=30)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title