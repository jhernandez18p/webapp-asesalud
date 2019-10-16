from django.conf import settings
from django.conf.urls import handler404, handler500, handler403, handler400
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flats
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve


favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=True)

sitemaps = {
    "flatpages": FlatPageSitemap,
}

urlpatterns = [
    path('', include( 'client.base.urls' )),
    path('adminsite/', admin.site.urls),
    path('auth/', include( 'server.auth.urls' )),
    path('dashboard/', include( 'client.panel.urls' )),
    re_path(r'^favicon\.ico$', favicon_view),
]

admin.site.site_title = "Dev2tech CMS"
admin.site.site_header = "CMS"

handler400 = "server.auth.views.my_custom_bad_request_view"
handler403 = "server.auth.views.my_custom_permission_denied_view"
handler404 = "server.auth.views.my_custom_page_not_found_view"
handler500 = "server.auth.views.my_custom_error_view"

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),        
    ]