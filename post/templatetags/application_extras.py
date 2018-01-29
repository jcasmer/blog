'''
Custom template tags
'''
from django import template
register = template.Library()  # pylint: disable=invalid-name


@register.filter('is_pair')
def is_pair(number):
    '''
    Return if a number is pair or not
    '''
    return number % 2 == 0


@register.filter('fieldtype')
def fieldtype(field):
    '''
    Return the widget type of a field
    '''
    return field.field.widget.__class__.__name__.lower()


@register.filter('is_textarea')
def is_textarea(field, args=None):
    '''
    Return if a widget is textarea
    '''
    flag = fieldtype(field) == 'textarea'
    if args is None:
        return flag
    args = [arg.strip() for arg in args.split(' ')]
    if flag:
        return args[0]
    return args[1]


@register.filter('is_radio')
def is_radio(field, args=None):
    '''
    Return if a widget is textarea
    '''
    flag = fieldtype(field) == 'radioselect'
    if args is None:
        return flag
    args = [arg.strip() for arg in args.split(' ')]
    if flag:
        return args[0]
    return args[1]


@register.filter('is_select')
def is_select(field, args=None):
    '''
    Return the widget type of a field
    '''
    flag = fieldtype(field) == 'select'
    if args is None:
        return flag
    args = [arg.strip() for arg in args.split(' ')]
    if flag:
        return args[0]
    return args[1]

@register.filter('is_required')
def is_required(field, args=None):
    '''
    Return if a widget is textarea
    '''
    flag = field.field.widget.is_required
    if args is None:
        return flag
    args = [arg.strip() for arg in args.split(' ')]
    if flag:
        return args[0]
    return args[1]


@register.filter('next')
def next_element(value, arg):
    '''
    Next element
    '''
    try:
        return value[list(value.fields)[int(arg) + 1]]
    except IndexError:
        return None


@register.filter('previous')
def previous_element(value, arg):
    '''
    Previous element
    '''
    if int(arg) == 0:
        return None
    return value[list(value.fields)[int(arg) - 1]]
