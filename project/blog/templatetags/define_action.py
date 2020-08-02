from django import template

register=template.Library()

@register.filter(name='Range')
def Range(x):
	return range(1,x+1)