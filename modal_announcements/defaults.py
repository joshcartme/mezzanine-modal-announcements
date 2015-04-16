
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="ANNOUNCEMENT_FREQUENCY",
    label=_("Announcement frequency"),
    description=_("Controls how often (in minutes) popup "
                  "announcements will be shown to the same visitor"),
    editable=True,
    default="15",
)


register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    append=True,
    default=("ANNOUNCEMENT_FREQUENCY",),
)
