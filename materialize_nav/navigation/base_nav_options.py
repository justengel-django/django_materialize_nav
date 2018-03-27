from dynamicmethod import dynamicmethod


__all__ = ['BaseNavOptions']


class BaseNavOptions(object):
    @dynamicmethod
    def get_context(self, request, context=None, *, notification=None, **kwargs):
        if context is None:
            context = {}

        context['previous_page'] = request.META.get("HTTP_REFERER", '/')
        context['notification'] = request.GET.get("notification", notification)

        # Force the request to be in the context
        if "request" not in context:
            context['request'] = request

        # Notify that the nav context was loaded
        request.nav_context_loaded = True

        return context
