from django.db import models
from markdown import markdown
from tagging.fields import TagField
import datetime, tagging



class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
		)
	title = models.CharField(max_length=250, help_text = u'Maximum 250 characters')
	excerpt = models.TextField(help_text = u'A short summary of the entry.')
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)

	excerpt_html = models.TextField(editable=False, blank=True)
	body_html = models.TextField(editable=False, blank=True)

	enable_comments = models.BooleanField(default=True)
	slug = models.SlugField(unique_for_date='pub_date', help_text=u'Suggested value automatically generated from title. Must be unique.')
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, help_text=u'Only entries with live status will be publicly displayed.')

	tags = TagField(help_text=u'Seperate tags with spaces.')
	love_count = models.IntegerField(default=0)

#	live = LiveEntryManager()
#	objects = models.Manager()

	class Meta:
	    ordering = ['-pub_date']
	    verbose_name_plural = u'Entries'

	def __unicode__(self):
	    return self.title

	def save(self, force_insert=False, force_update=False):
	    self.body_html = markdown(self.body)
	    self.excerpt_html = markdown(self.excerpt)
	    super(Entry, self).save(force_insert, force_update)

	@models.permalink
	def get_absolute_url(self):
		return ('blog_entry_detail', (), { 'year': self.pub_date.strftime("%Y"),
										   'month': self.pub_date.strftime("%b").lower(),
										   'day': self.pub_date.strftime("%d"),
										   'slug': self.slug })
    
tagging.register(Entry, tag_descriptor_attr='etags')
