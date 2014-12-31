#coding:utf-8
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
import datetime

def inoutviewer_hello(req):
	return HttpResponse("Hello World!")

def inoutviewer_time(req):
	nowtime = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % nowtime
#	return HttpResponse("Hello World!")
	return HttpResponse(html)

def inoutviewer_time_offset(req, offset):
	offset = int(offset)
	nowtime = datetime.datetime.now()
	assert False
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	html = "<html><body>In %s hours, It is %s.</body></html>" % (offset, dt)
#	return HttpResponse("Hello World!")
	return HttpResponse(html)

def inout_template(req):
	
	raw_template = """<p>Dear {{ person_name }},</p>
	
	 <p>Thanks for placing an order from {{ company }}. It's scheduled to
	 ship on {{ ship_date|date:"F j, Y" }}.</p>
	
	 {% if ordered_warranty %}
	 <p>Your warranty information will be included in the packaging.</p>
	 {% else %}
	 <p>You didn't order a warranty, so you're on your own when
	 the products inevitably stop working.</p>
	 {% endif %}
	
	 <p>Sincerely,<br />{{ company }}</p>"""

	t = Template(raw_template)
	c = Context({'person_name': 'John Smith',
		'company': 'Outdoor Equipment',
		'ship_date': datetime.date(2009, 4, 2),
		'ordered_warranty': False
		})
	html = t.render(c)

	return HttpResponse(html)

#from outpy import item_lists
from inoutdbview.models import Inout

def inout_version1(req):
	m = Inout.objects.filter(money_type = "金钱", type = "投放", category = "游戏中").order_by('amount')
	return render_to_response('inout.html', {'item_lists':m})
