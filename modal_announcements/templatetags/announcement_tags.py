

import datetime

from django.db.models import Q
from django.utils import timezone

from mezzanine import template

from mezzanine_modal_announcements.models import SiteAnnouncement

register = template.Library()


@register.as_tag
def get_announcements():
    modals = SiteAnnouncement.objects.filter(deactivate=False)
    now = timezone.localtime(timezone.now())

    current_time = datetime.time(now.hour, now.minute, now.second)
    today = datetime.date(now.year, now.month, now.day)

    modals = modals.filter(
        Q(start_time__lte=current_time) | Q(start_time__isnull=True))
    modals = modals.filter(
        Q(end_time__gte=current_time) | Q(end_time__isnull=True))

    modals = modals.filter(
        Q(start_date__lte=today) | Q(start_date__isnull=True))
    modals = modals.filter(
        Q(end_date__gte=today) | Q(end_date__isnull=True))

    modals = modals.filter(
        Q(weekdays__contains=str(now.weekday())) | Q(weekdays=''))

    return modals
