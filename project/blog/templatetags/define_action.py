from django import template

register=template.Library()

@register.simple_tag
def define(v):
	return v