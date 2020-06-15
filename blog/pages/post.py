from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.pages.base import BasePage
import datetime, re

class BlogIndexPage(RoutablePageMixin, BasePage):

    parent_page_types = ['blog.HomePage']
    subpage_types = ['blog.PostPage']

    max_count = 1

    @property
    def blog_page(self):
        return self.specific

    def get_posts(self):
        return PostPage.objects.descendant_of(self).live().order_by('-first_published_at')

class PostPage(BasePage):
    date = models.DateField(_("Post date"), default=datetime.datetime.today, help_text=_("Date when the post will be posted"))
    excerpt = models.CharField(_("Excerpt"), max_length=255, help_text=_("Post's summary, maximum 255 characters"))
    body = RichTextField(verbose_name=_("Post's Body"), help_text=_("It will be the main content of your post"))
    visit_count = models.PositiveIntegerField(default=0, editable=False)

    header_image = models.ForeignKey(
        'custom_image.customimage',
        verbose_name=_("Header Image"),
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_("Header Image. It will be used after the title in the post")
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
        index.SearchField('excerpt')
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        MultiFieldPanel([
            FieldPanel('date'),
            #FieldPanel('visit_count'),
            #FieldPanel('tags'),
            #FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading=_("Additional Post's information")),
        FieldPanel('excerpt', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    @property
    def blog_page(self):
        return self.get_parent().specific