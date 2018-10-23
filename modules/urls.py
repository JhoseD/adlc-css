from django.urls import path
from .views import index
from .views import list_client, create_client, update_client, delete_client, view_client, client_projects
from .views import list_project, create_project, update_project, delete_project, view_project, project_rols, project_tasks, project_requirements
from .views import list_requirement, create_requirement, update_requirement, delete_requirement, view_requirement
from .views import list_task, create_task, update_task, delete_task, view_task, task_comments, task_errors, list_task_not_started, list_task_in_process, list_task_finished
from .views import list_error, create_error, update_error, delete_error, view_error
from .views import list_comment, create_comment, update_comment, delete_comment, view_comment
from .views import list_rol, create_rol, update_rol, delete_rol, view_rol

from .views import LoginView, CrearUsuarioView, log_out

urlpatterns = [
    path('', index, name = 'index'),
    path('index', index, name = 'index'),

    path('list_client', list_client, name = 'list_client'),
    path('create_client', create_client, name = 'create_client'),
    path('update_client/<int:id>/', update_client, name = 'update_client'),
    path('delete_client/<int:id>/', delete_client, name = 'delete_client'),
    path('view_client/<int:id>/', view_client, name = 'view_client'),
    path('client_projects/<int:id>/', client_projects, name = 'client_projects'),


    path('list_project', list_project, name = 'list_project'),
    path('create_project', create_project, name = 'create_project'),
    path('update_project/<int:id>/', update_project, name = 'update_project'),
    path('delete_project/<int:id>/', delete_project, name = 'delete_project'),
    path('view_project/<int:id>/', view_project, name = 'view_project'),
    path('project_rols/<int:id>/', project_rols, name = 'project_rols'),
    path('project_tasks/<int:id>/', project_tasks, name = 'project_tasks'),
    path('project_requirements/<int:id>/', project_requirements, name = 'project_requirements'),


    path('list_requirement', list_requirement, name = 'list_requirement'),
    path('create_requirement', create_requirement, name = 'create_requirement'),
    path('update_requirement/<int:id>/', update_requirement, name = 'update_requirement'),
    path('delete_requirement/<int:id>/', delete_requirement, name = 'delete_requirement'),
    path('view_requirement/<int:id>/', view_requirement, name = 'view_requirement'),


    path('list_task', list_task, name = 'list_task'),
    path('create_task', create_task, name = 'create_task'),
    path('update_task/<int:id>/', update_task, name = 'update_task'),
    path('delete_task/<int:id>/', delete_task, name = 'delete_task'),
    path('view_task/<int:id>/', view_task, name = 'view_task'),
    path('task_comments/<int:id>/', task_comments, name = 'task_comments'),
    path('task_errors/<int:id>/', task_errors, name = 'task_errors'),
    path('list_task_not_started/<int:id>/', list_task_not_started, name = 'list_task_not_started'),
    path('list_task_in_process/<int:id>/', list_task_in_process, name = 'list_task_in_process'),
    path('list_task_finished/<int:id>/', list_task_finished, name = 'list_task_finished'),


    path('list_error', list_error, name = 'list_error'),
    path('create_error', create_error, name = 'create_error'),
    path('update_error/<int:id>/', update_error, name = 'update_error'),
    path('delete_error/<int:id>/', delete_error, name = 'delete_error'),
    path('view_error/<int:id>/', view_error, name = 'view_error'),


    path('list_comment', list_comment, name = 'list_comment'),
    path('create_comment', create_comment, name = 'create_comment'),
    path('update_comment/<int:id>/', update_comment, name = 'update_comment'),
    path('delete_comment/<int:id>/', delete_comment, name = 'delete_comment'),
    path('view_comment/<int:id>/', view_comment, name = 'view_comment'),


    path('list_rol', list_rol, name = 'list_rol'),
    path('create_rol', create_rol, name = 'create_rol'),
    path('update_rol/<int:id>/', update_rol, name = 'update_rol'),
    path('delete_rol/<int:id>/', delete_rol, name = 'delete_rol'),
    path('view_rol/<int:id>/', view_rol, name = 'view_rol'),

    path('login', LoginView.as_view(), name = 'login'),
    path('logout', log_out, name = 'logout'),
    path('signup', CrearUsuarioView.as_view(), name = 'signup'),
]
