from django.db import models

# Create your models here.

class Project_data(models.Model):
  title = models.CharField(max_length=50)
  details = models.CharField(max_length=800)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  target = models.IntegerField()
  start_date = models.DateField()
  end_date = models.DateField()
  rating = models.IntegerField(default=3)
  reports = models.IntegerField(default=0)
  
  def __str__(self):
    return self.title
  
class Category(models.Model):
  name = models.CharField(max_length=50)  
  
  def __str__(self):
    return self.name
  
  
class Project_pics(models.Model):
  project = models.ForeignKey('Project_data',on_delete=models.CASCADE)
  image = models.ImageField(upload_to='project/static/project_pics/')
  
  def __str__(self):
    return self.project.title
  
class project_comments(models.Model):
  project = models.ForeignKey('Project_data',on_delete=models.CASCADE)
  comment = models.TextField()
  
  def __str__(self):
    return self.comment

class Tag(models.Model):
  name = models.CharField(max_length=50)  
  
  def __str__(self):
    return self.name

class project_tags(models.Model):
  project = models.ForeignKey('Project_data',on_delete=models.CASCADE)
  tag_id = models.ForeignKey('Tag',on_delete=models.CASCADE)
  
  def __str__(self):
    return self.project.title + " - " + self.tag_id.name

