from django import template
from django.contrib.auth.models import User
from spirit.topic.models import Topic
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def forum_stats():
    user_count = User.objects.count()
    topic_count = Topic.objects.count()
    return f"Зарегистрировано пользователей: {user_count} ⠀ Создано тем: {topic_count}"