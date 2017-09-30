import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()

@stringfilter
def custome_markdown(value):
    return mark_safe(markdown.markdown(value,
	extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
		safe_code=True,
		enable_attributes=False))

