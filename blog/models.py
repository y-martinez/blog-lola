from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet

from blog.pages import BasePage, HomePage
from colorfield.fields import ColorField

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, help_text=_("Category name"))
    slug = models.SlugField(unique=True, max_length=80)
    color = ColorField(help_text=_("Category color")) #models.CharField(max_length=7, help_text=_("Category color"))

    panels = [
        FieldPanel('name'),
        FieldPanel('color'),
    ]

    class Meta:
        verbose_name = _("Blog category")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BlogCategory, self).save(args, kwargs)

@register_setting
class SiteSetting(BaseSetting):
    gtm_id = models.CharField(max_length=50, blank=True)
    google_site_verification = models.CharField(max_length=255, blank=True)

    cookie_content = RichTextField(
        blank=True, null=True, verbose_name=_("Cookie bar content"), features=[]
    )

    panels = [FieldPanel("gtm_id"), FieldPanel("cookie_content")]

    def __str__(self):
        return str(self.site)

    class Meta:
        verbose_name = _("Site setting")
        verbose_name_plural = _("Site settings")
