from rest_framework import serializers
from wagtail.images.shortcuts import get_rendition_or_not_found
from wagtail.core import fields
from wagtail.api.v2 import serializers as wagtail_serializers

from blog.models import SiteSetting
from blog.pages import BasePage, HomePage

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ["gtm_id", "cookie_content"]

class SeoSerializer(serializers.ModelSerializer):
    seo_og_image = serializers.SerializerMethodField()
    seo_twitter_image = serializers.SerializerMethodField()

    class Meta:
        model = BasePage
        fields = [
            "seo_og_image",
            "seo_html_title",
            "seo_meta_description",
            "seo_og_title",
            "seo_og_description",
            "seo_og_url",
            "seo_og_type",
            "seo_twitter_title",
            "seo_twitter_description",
            "seo_twitter_image",
            "seo_meta_robots",
            "canonical_link",
        ]

    def get_seo_og_image(self, page):
        root_url = page.get_site().root_url
        image = page.seo_og_image

        if not image:
            return None

        rendition = get_rendition_or_not_found(image, "max-1200x630")

        if not rendition:
            return None

        return f"{root_url}{rendition.url}"

    def get_seo_twitter_image(self, page):
        root_url = page.get_site().root_url
        image = page.seo_twitter_image

        if not image:
            return None

        rendition = get_rendition_or_not_found(image, "max-1200x630")

        if not rendition:
            return None

        return f"{root_url}{rendition.url}"

class BasePageSerializer(serializers.ModelSerializer):
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping.update(
        {fields.StreamField: wagtail_serializers.StreamField}
    )

    seo = serializers.SerializerMethodField()
    site_setting = serializers.SerializerMethodField()

    class Meta:
        model = BasePage
        fields = [
            "title",
            "last_published_at",
            "seo_title",
            "search_description",
            "seo",
            "site_setting",
        ]

    def get_seo(self, page):
        return SeoSerializer(page).data

    def get_site_setting(self, page):
        site_setting = SiteSetting.for_site(page.get_site())
        return SiteSettingSerializer(site_setting).data

class HomePageSerializer(BasePageSerializer):
    class Meta:
        model = HomePage
        fields = BasePageSerializer.Meta.fields