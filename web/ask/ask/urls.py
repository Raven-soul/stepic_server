from django.conf.urls import url, include
from django.contrib import admin

from ask.views import found, not_found

h = bytes("dfdf", encoding="utf8")

urlpatterns = [

    url(r'^$', found),

    url(r'^login/', found),
    url(r'^signup/', found),
    url(r'^ask/', found),
    url(r'^popular/', found),
    url(r'^new/', found),

    url(r'^admin/', admin.site.urls),
    url(r'^question/', include('qa.urls')),

    url(r'^', not_found),
]
