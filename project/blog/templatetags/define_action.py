from django import template

register=template.Library()

rightFalse=0
leftFalse=0

@register.filter(name='Range')
def Range(x):
	return range(1,x+1)


@register.simple_tag
def define(v):
	return v

@register.filter(name='checkForDot')
def checkForDot(x,page):
	global rightFalse,leftFalse
	currentPage = page.number
	lastPage = page.paginator.num_pages 
	print(leftFalse)
	if x==1 or x==lastPage:
		return 'true'
	else:
		if x<currentPage:
			if currentPage-1-x-1<0:
				return 'true'
			else:
				if leftFalse <6:
					leftFalse=leftFalse+1
					return 'false'
				else:
					return 'd'
		else:
			if x-currentPage-1-1<0:
				return 'true'
			else:
				if rightFalse <6:
					rightFalse=rightFalse+1
					return 'false'
				else:
					return 'd'

@register.filter(name='incVar')
def incVar(x):
	return x+1