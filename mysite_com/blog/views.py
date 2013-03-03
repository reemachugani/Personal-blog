from blog.models import Entry
from tagging.models import Tag
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models import F
import datetime, time


MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')


def blog_home(request):
	return render_to_response('blog/blog_home.html', {'entries': Entry.objects.filter(status = 1)}, context_instance=RequestContext(request))


def archive_by_month(request, year, month):
	date_stamp = time.strptime(year+month, "%Y%m")
	pub_date = datetime.date(*date_stamp[:3])
	entries = Entry.objects.filter(status = 1).filter(Q(pub_date__year = pub_date.year)).filter(Q(pub_date__month = pub_date.month))
	ctx = {'entries':entries, 'year':year, 'month':MONTH_NAMES[int(month)]}
	return render_to_response('blog/archive_by_month.html', ctx, context_instance=RequestContext(request))


def entry_detail(request, year, month, day, slug):
	date_stamp = time.strptime(year+month+day, "%Y%b%d")
	pub_date = datetime.date(*date_stamp[:3])
	entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
								pub_date__month=pub_date.month,
								pub_date__day=pub_date.day,
								slug=slug)
	return render_to_response('articles/blog_entry.html',	{'entry': entry }, context_instance=RequestContext(request))


def tag_page(request, tag):
	entries = Entry.objects.filter(status = 1).filter(tags__contains = tag)
	return render_to_response('blog/blog_home.html',{'entries': entries, 'tag': tag }, context_instance=RequestContext(request))

def love_inc(request, slug):
	entry = Entry.live.get(slug=slug)
	Entry.live.filter(slug=slug).update(love_count=F('love_count') + 1)
	return HttpResponseRedirect(entry.get_absolute_url())
