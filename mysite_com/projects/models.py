from django.db import models
from markdown import markdown

class Project(models.Model):
	title = models.CharField(max_length=250, help_text = u'Maximum 250 characters')
	slug = models.SlugField(help_text=u'Suggested value automatically generated from title. Must be unique.')
	about = models.TextField()
	about_html = models.TextField(editable=False, blank=True)
	tech = models.TextField(help_text=u'Technologies used.')
	tech_html = models.TextField(editable=False, blank=True)
	url = models.URLField('URL', unique=True)

	def __unicode__(self):
		return self.title

	def save(self):
		self.about_html = markdown(self.about)
		self.tech_html = markdown(self.tech)
		super(Project, self).save()


# class Picture(models.Model):
# 	pic = models.ImageField()
# 	project = models.ForeignKey(Project)

# 	def __unicode__(self):
# 		return self.id 	