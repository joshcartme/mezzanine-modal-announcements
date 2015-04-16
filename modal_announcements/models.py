
from django.db import models

from mezzanine.core.models import Orderable, SiteRelated, RichText


class SiteAnnouncement(Orderable, SiteRelated, RichText):
    '''
    A modal that pops up on the home page
    '''
    title = models.CharField(max_length=200)
    deactivate = models.BooleanField(
        default=False,
        help_text="If checked this modal will not show")
    start_time = models.TimeField(
        blank=True, null=True,
        help_text="If present the modal will only show after this time")
    end_time = models.TimeField(
        blank=True, null=True,
        help_text="If present the model will only show before this time")
    start_date = models.DateField(
        blank=True, null=True,
        help_text="If present the modal will only show on or after this date")
    end_date = models.DateField(
        blank=True, null=True,
        help_text="If present the modal will only show on or before this date")
    weekdays = models.CharField(
        max_length=14, blank=True,
        help_text="The announcement will only show on the selected days of "
                  "the week, hold ctrl (cmd on a mac) to select more than "
                  "one.  If blank the announcement will be eligible to show on "
                  "any day of the week")

    def __unicode__(self):
        return self.title
