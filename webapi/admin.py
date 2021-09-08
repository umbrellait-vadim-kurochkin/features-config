from django.contrib import admin
from .models import Stream, Feature, Condition, Parameter, Operator, ExpressionValue

class StreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'author', 'created_at')
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(Stream, StreamAdmin)
admin.site.register(Feature)
admin.site.register(Condition)
admin.site.register(Parameter)
admin.site.register(Operator)
admin.site.register(ExpressionValue)