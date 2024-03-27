from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='main'),
    path('kontakt', views.ContactPage.as_view(), name='contact'),
    path('uslugi', views.ServicesPage.as_view(), name="services"),
    path('demontazhnye-i-podgotovitelnye-raboty', views.PrepareServisPage.as_view(), name='prepare'),
    path('malyarnye-raboty', views.MalarPage.as_view(), name="malar"),
    path('plitochnye-raboty', views.PlitkaPage.as_view(), name="plitka"),
    path('styazhka-pola', views.StyazhkaPage.as_view(), name="styazhka"),
    path('ustrojstvo-sten', views.UstrojstvoStenPage.as_view(), name="ustrojstvo-sten"),
    path('ustrojstvo-potolkov', views.UstrojstvoPotolkovPage.as_view(), name="ustrojstvo-potolkov"),
    path('ustanovka-mezhkomnatnykh-dverey', views.UstrojstvoDvereyPage.as_view(), name="ustanovka-mezhkomnatnykh-dverey"),
    path('elektromontazhnye-raboty', views.ElektromontazhnyeRabotyPage.as_view(), name="elektromontazhnye-raboty"),
    path('santekhnicheskie-raboty', views.SantekhnicheskieRabotyPage.as_view(), name="santekhnicheskie-raboty"),
    path('otdelochnye-raboty', views.OtdelochnyeRabotyPage.as_view(), name="otdelochnye-raboty"),
    path('shtukaturnye-raboty', views.ShtukaturnyeRabotyPage.as_view(), name="shtukaturnye-raboty"),
    path('poklejka-oboev', views.PoklejkaOboevPage.as_view(), name="poklejka-oboev"),
    path('remont-vannoj-komnaty', views.RemontVannojPage.as_view(), name="remont-vannoj-komnaty"),
    path('remont-v-tc', views.RemontVTCPage.as_view(), name="remont-v-tc"),
    path('otdelka-pomeshchenij', views.OtdelkaPomeshchenijPage.as_view(), name="otdelka-pomeshchenij"),
    path('shumoizolyatsiya', views.ShumoizolyatsiyaPage.as_view(), name="shumoizolyatsiya"),
    path('tekhnicheskaya-proverka', views.TekhnicheskayaProverkaPage.as_view(), name="tekhnicheskaya-proverka"),
    path('uslugi-elektrika', views.UslugiElektrikaPage.as_view(), name="uslugi-elektrika"),
    path('uslugi-santekhnika', views.UslugiSantekhnikaPage.as_view(), name="uslugi-santekhnika"),
    path('uslugi-plitochnika', views.UslugiPlitochnikaPage.as_view(), name="uslugi-plitochnika"),
    path('remont-balkonov', views.RemontBalkonovPage.as_view(), name="remont-balkonov"),
    path('nalivnoy-pol', views.NalivnoyPolPage.as_view(), name="nalivnoy-pol"),
    path('ukladka-laminata', views.UkladkaLaminataPage.as_view(), name="ukladka-laminata"),
    path('remont-v-novostrojkakh', views.RemontVNovostrojkakhPage.as_view(), name="remont-v-novostrojkakh"),
    path('remont-kottedzhej', views.RemontKottedzhejPage.as_view(), name="remont-kottedzhej"),
    path('remont/kosmeticheskij-remont', views.KosmeticheskijRemontPage.as_view(), name="kosmeticheskij-remont"),
    path('remont/kapitalnyj-remont-kvartir', views.KapitalnyjRemontKvartirPage.as_view(), name="kapitalnyj-remont-kvartir"),
    path('remont/evroremont', views.EvroremontPage.as_view(), name="evroremont"),
    path('nashi-raboti', views.NashiRabotiPage.as_view(), name="nashi-raboti"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
