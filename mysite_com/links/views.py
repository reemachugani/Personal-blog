from links.models import Link
from tagging.models import Tag
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime, time


MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')


def links_home(request):
	return render_to_response('blog/bookmarks.html', {'links': Link.objects.all()}, context_instance=RequestContext(request))


def archive_by_month(request, year, month):
	date_stamp = time.strptime(year+month, "%Y%m")
	pub_date = datetime.date(*date_stamp[:3])
	links = Link.objects.filter(Q(pub_date__year = pub_date.year)).filter(Q(pub_date__month = pub_date.month))
	ctx = {'links':links, 'year':year, 'month':MONTH_NAMES[int(month)]}
	return render_to_response('links/archive_by_month.html', ctx, context_instance=RequestContext(request))


def tag_page(request, tag):
	links = Link.objects.filter(tags__contains = tag)
	return render_to_response('blog/bookmarks.html', {'links':links, 'tag': tag}, context_instance=RequestContext(request))
