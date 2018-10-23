from django.contrib import admin
from .models import client, project, requirement, task, rol, error, comment
# Register your models here.
admin.site.register(client)
admin.site.register(project)
admin.site.register(requirement)
admin.site.register(task)
admin.site.register(rol)
admin.site.register(error)
admin.site.register(comment)
