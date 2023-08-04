from django import template
from DjangoTemplates.templates_app.models import Articles

register = template.Library()


@register.inclusion_tag('articles.html')
def show_articles():
    articles = Articles.objects.all()
    return {'articles': articles}

