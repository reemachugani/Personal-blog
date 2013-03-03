from django.db import models
from markdown import markdown
from tagging.fields import TagField
import tagging, datetime 

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length=250)
	url = models.URLField('URL', unique=True)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(unique_for_date='pub_date', 
		help_text='Must be unique for the publication date.')
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, blank=True)
	tags = TagField(help_text=u'Seperate tags with spaces.')

	class Meta:
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		super(Link, self).save()

	# @models.permalink
	# def get_absolute_url(self):
	# 	return ('links_link_detail', (), { 'year': self.pub_date.strftime("%Y"),
	# 									   'month': self.pub_date.strftime("%b").lower(),
	# 									   'day': self.pub_date.strftime("%d"),
	# 									   'slug': self.slug })
    
tagging.register(Link, tag_descriptor_attr='etags')
