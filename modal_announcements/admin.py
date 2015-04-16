
from django import forms
from django.contrib import admin

from .models import SiteAnnouncement


DAYS_OF_THE_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class SiteAnnouncementModelForm(forms.ModelForm):
    weekdays = forms.MultipleChoiceField(
        choices=DAYS_OF_THE_WEEK, required=False)

    class Meta:
        model = SiteAnnouncement

    def clean_weekdays(self):
        weekdays = self.cleaned_data['weekdays']
        weekdays_str = ''
        for weekday in weekdays:
            weekdays_str += '%s,' % weekday
        return weekdays_str

    @classmethod
    def preprocess(cls, data):
        """
        A preprocessor for the order form data that can be overridden
        by custom form classes. The default preprocessor here handles
        copying billing fields to shipping fields if "same" checked.
        """


class SiteAnnouncementAdmin(admin.ModelAdmin):
    form = SiteAnnouncementModelForm
    list_display = ['title',
                    'start_time', 'end_time',
                    'start_date', 'end_date',
                    'deactivate', '_order']
    list_editable = ['deactivate', '_order']
    fields = ['deactivate', 'title', 'content',
              'start_time', 'end_time',
              'start_date', 'end_date',
              'weekdays']

admin.site.register(SiteAnnouncement, SiteAnnouncementAdmin)
