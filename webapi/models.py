from django.db import models
from django.conf import settings
from django.utils import timezone

class Stream(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=30) #min_length=3
    project_code = models.UUIDField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        #self.created_date = timezone.now()
        self.save()

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