from django import template
from notesapp.web.models import Profile

register = template.Library()


@register.inclusion_tag(
    'web/tags/navigation.html',
    name='custom_navigation'
)
def inclusion_custom_navigation():
    inner_context = {
        "profile": Profile.objects.first()
    }
    return inner_context
