from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class client(models.Model):
    name = models.CharField(max_length = 75)
    telephone = models.CharField(max_length = 25)
    email = models.EmailField()
    address = models.CharField(max_length = 150)

    def __str__(self):
        return '%s' % (self.name)

class project(models.Model):
    name = models.CharField(max_length = 75)
    percent = models.PositiveSmallIntegerField()
    created_at = models.DateField(auto_now_add = True)
    file = models.URLField(blank = True)
    client_id = models.ForeignKey(client, on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

class requirement(models.Model):
	title = models.CharField(max_length = 45)
	description = models.TextField()
	start_date = models.DateField(auto_now_add = True)
	end_date = models.DateField(blank = True, null = True)
	project_id = models.ForeignKey(project, on_delete = models.CASCADE)

	def __str__(self):
		return '%s' % (self.title)

class task(models.Model):
    title = models.CharField(max_length = 50)
    percent = models.PositiveSmallIntegerField()
    state_choices = (
		('Not Started', 'Not Started'),
		('In Process', 'In Process'),
		('Finished', 'Finished'),
		)
    state = models.CharField(
		max_length = 12,
		choices = state_choices,
		default = 'Not Started',
		)
    hours = models.PositiveSmallIntegerField()
    project_id = models.ForeignKey(project, on_delete = models.CASCADE)
    user_in_charge = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'in_charge')
    user_supervisor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'supervisor')

    def __str__(self):
        return '%s' % (self.title)

class rol(models.Model):
    rol_choices = (
		('Scrum Master', 'Scrum Master'),
		('Product Owner', 'Product Owner'),
		('Team/Developer', 'Team/Developer'),
		)
    rol = models.CharField(
		max_length = 15,
		choices = rol_choices,
		default = 'Team/Developer',
		)
    project_id = models.ForeignKey(project, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.rol, self.project_id, self.user_id)

class error(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    state_choices = (
		('Solved', 'Solved'),
		('Not Solved', 'Not Solved'),
		)
    state = models.CharField(
		max_length = 11,
		choices = state_choices,
		default = 'Not Solved',
		)
    task_id = models.ForeignKey(task, on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % (self.title)

class comment(models.Model):
    title = models.CharField(max_length = 50)
    comment = models.TextField()
    task_id = models.ForeignKey(task, on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % (self.title)
    # rsim 175
    # rsim 11 levanta 4g
    # depende del model del iphone if 4 rsim 10
