from links.models import Link
from tagging.models import Tag
import datetime, time

MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')


def archive(request):
    archive_data = []
    count = {}
    mcount = {}
    links = Link.objects.all()
    for link in links:
        year = link.pub_date.year
        month = link.pub_date.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.iterkeys(), reverse=True):
        archive_data.append({'isyear': True,
                             'year': year, 
                             'count': count[year],})
        for month in sorted(mcount[year].iterkeys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month], 
                                 'count': mcount[year][month],})
    return {'links_archive':archive_data}


def tag_cloud(request):
	MAX_WEIGHT = 5
	tag_list = Tag.objects.usage_for_model(Link, counts = True)
	min_count = max_count = tag_list[0].count
	for tag in tag_list:
		# tag_count = tag.count
		if tag.count < min_count:
			min_count = tag.count
		if max_count < tag.count:
			max_count = tag.count
	range = float(max_count - min_count)
	if range == 0.0:
		range = 1.0
	for tag in tag_list:
		tag.weight = int(MAX_WEIGHT * (tag.count - min_count) / range)

	return {'links_tag_list':tag_list}