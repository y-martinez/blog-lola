from django.conf import settings


def settings_context(request):
    """
    Expose django settings to template engine
    """
    parsed_settings = {"DEBUG": settings.DEBUG, "APP_VERSION": settings.APP_VERSION}

    if hasattr(settings, "SENTRY_DSN"):
        parsed_settings["SENTRY_DSN"] = settings.SENTRY_DSN

    if hasattr(settings, "SENTRY_ENVIRONMENT"):
        parsed_settings["SENTRY_ENVIRONMENT"] = settings.SENTRY_ENVIRONMENT

    return {"SETTINGS": parsed_settings}
