from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStamp(models.Model):
    """General Abstract model that can inherited by other model which requires timestamp"""

    created_at = models.DateTimeField(
        _("Created Date"),
        auto_now_add=True,
        help_text=_("Eg. 2020-07-16T19:40:02.785988+05:45"),
    )
    updated_at = models.DateTimeField(
        _("Updated Date"),
        auto_now=True,
        help_text=_("Eg. 2020-07-16T19:40:02.785988+05:45"),
    )

    class Meta:
        abstract = True


class Category(TimeStamp):
    name = models.CharField(
        _("Main category of TODO list"),
        max_length=50,
        help_text=_("Eg. Backlog, ToDo, Doing, Research, On hold etc."),
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.created_by}"


class ToDo(TimeStamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        _("Title of TODO item"),
        max_length=255,
        help_text=_("Eg. Integrate login system."),
    )
    deadline = models.DateTimeField(
        _("Deadline of TODO"),
        blank=True,
        null=True,
        help_text=_("Eg. 2020-07-16T19:40:02.785988+05:45"),
    )

    def __str__(self):
        return f"{self.title} | {self.category} | {self.created_by}"
