from django.contrib import admin
from django.conf import settings
from django.urls import include, re_path, path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views import defaults as default_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap


urlpatterns = [path('i18n/', include('django.conf.urls.i18n')),]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += i18n_patterns(
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        prefix_default_language=False
    )
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

urlpatterns += i18n_patterns(
    re_path(settings.ADMIN_URL, admin.site.urls),
    #re_path(r'^search/$', search_views.search, name='search'),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'', include(wagtail_urls)),
    re_path(r"^sitemap\.xml$", sitemap, name="sitemap"),
    prefix_default_language=False)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)