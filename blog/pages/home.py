from django.utils.translation import gettext_lazy as _

from blog.pages.base import BasePage


class HomePage(BasePage):
    extra_panels = BasePage.extra_panels
    serializer_class = "blog.serializers.HomePageSerializer"
    parent_page_types = []
    #subpage_types = ['blog.BlogIndexPage', 'organization.OrganizationIndexPage', 'contact_us.ContactFormPage', 'about_us.AboutUsPage']
    class Meta:
        verbose_name = _("Home")