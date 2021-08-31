from django.contrib import admin
from .models import Stream, Feature, Condition, Parameter, Operator, ExpressionValue

admin.site.register(Stream)
admin.site.register(Feature)
admin.site.register(Condition)
admin.site.register(Parameter)
admin.site.register(Operator)
admin.site.register(ExpressionValue)