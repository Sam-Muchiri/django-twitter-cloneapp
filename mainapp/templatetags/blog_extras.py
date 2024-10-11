from django import template
register = template.Library()

@register.filter
def truncate_chars(value, nums_chars):
    """
    Truncates the blog post content to 'num_chars' characters.
    """
    if len(value)>nums_chars:
        return value[:nums_chars]+'...'
    return value