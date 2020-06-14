from typing import List, Dict, Any, Optional

from django.utils.module_loading import import_string
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from wagtail.core.models import Page
from rest_framework.serializers import Serializer

from blog.mixins import EnhancedEditHandlerMixin, SeoMixin

class BasePage(EnhancedEditHandlerMixin, SeoMixin, Page):
    # Basepage is not anything creatable in admin
    is_creatable = False
    show_in_menus_default = True

    extra_panels: List = []
    serializer_class = "blog.serializers.BasePageSerializer"

    def __init__(self, *args, **kwargs):
        #TODO PENDIENTE AQUI
        self.template = "pages/base_page.html"
        self.component_name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def get_context(self, request: HttpRequest, *args, **kwargs) -> Dict[str, Any]:
        context = super().get_context(request, *args, **kwargs)

        return {**context, "props": self.get_component_data({"request": request})}

    def serve(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.should_serve_json(request):
            json = self.get_component_data({"request": request})
            return JsonResponse(json)

        return super().serve(request, *args, **kwargs)

    @staticmethod
    def should_serve_json(request: HttpRequest) -> bool:
        return (
            request.GET.get("format", None) == "json"
            or request.content_type == "application/json"
        )

    def get_component_data(self, context: Optional[Dict]) -> Dict[str, Any]:
        return {
            "component_name": self.component_name,
            "component_props": self.to_dict(context),
        }

    def to_dict(self, context: Optional[Dict]) -> Dict[str, Any]:
        context = context or {}
        serializer_cls = self.get_serializer_class()
        serializer = serializer_cls(self, context=context)
        return serializer.data

    def get_serializer_class(self) -> Serializer:
        return import_string(self.serializer_class)
