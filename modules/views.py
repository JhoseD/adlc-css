from django.shortcuts import render, redirect
from .models import client, project, requirement, task, rol, error, comment
from .forms import client_form, project_form, requirement_form, task_form, rol_form, error_form, comment_form
from django.contrib.auth.models import User

# Login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import FormView

from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

# client
@login_required
def list_client(request):
	data = client.objects.all()
	return render(request, 'client/client_list.html', {'data': data})

@login_required
def create_client(request):
	if request.method == 'POST':
		form = client_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_client')
	else:
		form = client_form()
		return render(request, 'client/client.html', {'form': form})

@login_required
def update_client(request, id):
    data = client.objects.get(id = id)
    form = client_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_client')
    return render(request, 'client/client.html', {'form': form, 'data': data})

@login_required
def delete_client(request, id):
    data = client.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_client')
    return render(request, 'delete_confirm.html')
@login_required
def view_client(request, id):
    data = client.objects.get(id = id)
    return render(request, 'client/view.html', {'data': data})

# client projects
@login_required
def client_projects(request, id):
    data_ = client.objects.get(id = id)
    data = project.objects.filter(client_id = id)
    return render(request, 'client/client_projects.html', {'data_': data_,'data': data})
# end client


# project
@login_required
def list_project(request):
	data = project.objects.all()
	return render(request, 'project/project_list.html', {'data': data})

@login_required
def create_project(request):
	if request.method == 'POST':
		form = project_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_project')
	else:
		form = project_form()
		return render(request, 'project/project.html', {'form': form})

@login_required
def update_project(request, id):
    data = project.objects.get(id = id)
    form = project_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_project')
    return render(request, 'project/project.html', {'form': form, 'data': data})

@login_required
def delete_project(request, id):
    data = project.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_project')
    return render(request, 'delete_confirm.html')

@login_required
def view_project(request, id):
    data = project.objects.get(id = id)
    return render(request, 'project/view.html', {'data': data})

# project relations list
@login_required
def project_rols(request, id):
    data_ = project.objects.get(id = id)
    data = rol.objects.filter(project_id = id)
    return render(request, 'project/project_rols.html', {'data_': data_,'data': data})

@login_required
def project_requirements(request, id):
    data_ = project.objects.get(id = id)
    data = requirement.objects.filter(project_id = id)
    rol_ = rol.objects.filter(project_id = id)
    return render(request, 'project/project_requirements.html', {'data_': data_,'data': data, 'rol_': rol_})

@login_required
def project_tasks(request, id):
    data_ = project.objects.get(id = id)
    data = task.objects.filter(project_id = id)
    rol_ = rol.objects.filter(project_id = id)
    return render(request, 'project/project_tasks.html', {'data_': data_,'data': data, 'rol_': rol_})
# end project


# requirement
@login_required
def list_requirement(request):
	data = requirement.objects.all()
	return render(request, 'requirement/requirement_list.html', {'data': data})

@login_required
def create_requirement(request):
	if request.method == 'POST':
		form = requirement_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_requirement')
	else:
		form = requirement_form()
		return render(request, 'requirement/requirement.html', {'form': form})

@login_required
def update_requirement(request, id):
    data = requirement.objects.get(id = id)
    form = requirement_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_requirement')
    return render(request, 'requirement/requirement.html', {'form': form, 'data': data})

@login_required
def delete_requirement(request, id):
    data = requirement.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_requirement')
    return render(request, 'delete_confirm.html')

@login_required
def view_requirement(request, id):
    data = requirement.objects.get(id = id)
    return render(request, 'requirement/view.html', {'data': data})
# end requirement


# task
@login_required
def list_task(request):
	data = task.objects.all()
	return render(request, 'task/task_list.html', {'data': data})

# tasks per state
@login_required
def list_task_not_started(request, id):
    data_ = project.objects.get(id = id)
    data = task.objects.filter(state = 'Not Started', project_id = id)
    return render(request, 'project/project_tasks.html', {'data': data, 'data_': data_})

@login_required
def list_task_in_process(request, id):
    data_ = project.objects.get(id = id)
    data = task.objects.filter(state = 'In Process', project_id = id)
    return render(request, 'project/project_tasks.html', {'data': data, 'data_': data_})

@login_required
def list_task_finished(request, id):
    data_ = project.objects.get(id = id)
    data = task.objects.filter(state = 'Finished', project_id = id)
    return render(request, 'project/project_tasks.html', {'data': data, 'data_': data_})
# tasks per state

@login_required
def create_task(request):
	if request.method == 'POST':
		form = task_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_task')
	else:
		form = task_form()
		return render(request, 'task/task.html', {'form': form})

@login_required
def update_task(request, id):
    data = task.objects.get(id = id)
    form = task_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_task')
    return render(request, 'task/task.html', {'form': form, 'data': data})

@login_required
def delete_task(request, id):
    data = task.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_task')
    return render(request, 'delete_confirm.html')

@login_required
def view_task(request, id):
    data = task.objects.get(id = id)
    return render(request, 'task/view.html', {'data': data})

# task relations list
@login_required
def task_comments(request, id):
    data_ = task.objects.get(id = id)
    data = comment.objects.filter(task_id = id)
    return render(request, 'task/task_comments.html', {'data_': data_,'data': data})

@login_required
def task_errors(request, id):
    data_ = task.objects.get(id = id)
    data = error.objects.filter(task_id = id)
    return render(request, 'task/task_errors.html', {'data_': data_,'data': data})
# end task


# error
@login_required
def list_error(request):
	data = error.objects.all()
	return render(request, 'error/error_list.html', {'data': data})

@login_required
def create_error(request):
	if request.method == 'POST':
		form = error_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_error')
	else:
		form = error_form()
		return render(request, 'error/error.html', {'form': form})

@login_required
def update_error(request, id):
    data = error.objects.get(id = id)
    form = error_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_error')
    return render(request, 'error/error.html', {'form': form, 'data': data})

@login_required
def delete_error(request, id):
    data = error.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_error')
    return render(request, 'delete_confirm.html')

@login_required
def view_error(request, id):
    data = error.objects.get(id = id)
    return render(request, 'error/view.html', {'data': data})
# end error


# comments
@login_required
def list_comment(request):
	data = comment.objects.all()
	return render(request, 'comment/comment_list.html', {'data': data})

@login_required
def create_comment(request):
	if request.method == 'POST':
		form = comment_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_comment')
	else:
		form = comment_form()
		return render(request, 'comment/comment.html', {'form': form})

@login_required
def update_comment(request, id):
    data = comment.objects.get(id = id)
    form = comment_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_comment')
    return render(request, 'comment/comment.html', {'form': form, 'data': data})

@login_required
def delete_comment(request, id):
    data = comment.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_comment')
    return render(request, 'delete_confirm.html')
@login_required
def view_comment(request, id):
    data = comment.objects.get(id = id)
    return render(request, 'comment/view.html', {'data': data})
# end comment


# rol
@login_required
def list_rol(request):
	data = rol.objects.all()
	return render(request, 'rol/rol_list.html', {'data': data})

@login_required
def create_rol(request):
	if request.method == 'POST':
		form = rol_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_rol')
	else:
		form = rol_form()
		return render(request, 'rol/rol.html', {'form': form})

@login_required
def update_rol(request, id):
    data = rol.objects.get(id = id)
    form = rol_form(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return redirect('list_rol')
    return render(request, 'rol/rol.html', {'form': form, 'data': data})

@login_required
def delete_rol(request, id):
    data = rol.objects.get(id = id)
    if(request.method == 'POST'):
        data.delete()
        return redirect('list_rol')
    return render(request, 'delete_confirm.html')

@login_required
def view_rol(request, id):
    data = rol.objects.get(id = id)
    return render(request, 'rol/view.html', {'data': data})
# end rol

# login
class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = 'index'

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)


def log_out(request):
    logout(request)
    return redirect('index')

class CrearUsuarioView(CreateView):
	model = User
	template_name = 'create_user.html'
	form_class = UserCreationForm
	success_url = 'index'
# end login