from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = "main/index.html"


class ContactPage(TemplateView):
    template_name = "main/contacts.html"


class ServicesPage(TemplateView):
    template_name = "main/services.html"


class PrepareServisPage(TemplateView):
    template_name = "main/services/demont-raboty.html"


class MalarPage(TemplateView):
    template_name = "main/services/malar.html"


class PlitkaPage(TemplateView):
    template_name = "main/services/plitka.html"


class StyazhkaPage(TemplateView):
    template_name = "main/services/styazhka.html"


class UstrojstvoStenPage(TemplateView):
    template_name = "main/services/ustrojstvo-sten.html"


class UstrojstvoPotolkovPage(TemplateView):
    template_name = "main/services/ustrojstvo-potolkov.html"


class UstrojstvoDvereyPage (TemplateView):
    template_name = "main/services/ustanovka-dverey.html"


class ElektromontazhnyeRabotyPage (TemplateView):
    template_name = "main/services/elektromontazhnye-raboty.html"


class SantekhnicheskieRabotyPage (TemplateView):
    template_name = "main/services/santekhnicheskie-raboty.html"


class OtdelochnyeRabotyPage(TemplateView):
    template_name = "main/services/otdelochnye-raboty.html"


class ShtukaturnyeRabotyPage(TemplateView):
    template_name = "main/services/shtukaturnye-raboty.html"


class PoklejkaOboevPage(TemplateView):
    template_name = "main/services/poklejka-oboev.html"


class RemontVannojPage(TemplateView):
    template_name = "main/services/remont-vannoj-komnaty.html"


class RemontVTCPage(TemplateView):
    template_name = "main/services/remont-v-tc.html"


class OtdelkaPomeshchenijPage(TemplateView):
    template_name = "main/services/otdelka-pomeshchenij.html"


class ShumoizolyatsiyaPage(TemplateView):
    template_name = "main/services/shumoizolyatsiya.html"


class TekhnicheskayaProverkaPage(TemplateView):
    template_name = "main/services/tekhnicheskaya-proverka.html"


class UslugiElektrikaPage(TemplateView):
    template_name = "main/services/uslugi-elektrika.html"


class UslugiSantekhnikaPage(TemplateView):
    template_name = "main/services/uslugi-santekhnika.html"


class UslugiPlitochnikaPage(TemplateView):
    template_name = "main/services/uslugi-plitochnika.html"


class RemontBalkonovPage(TemplateView):
    template_name = "main/services/remont-balkonov.html"


class NalivnoyPolPage(TemplateView):
    template_name = "main/services/nalivnoy-pol.html"


class UkladkaLaminataPage(TemplateView):
    template_name = "main/services/ukladka-laminata.html"


class RemontVNovostrojkakhPage(TemplateView):
    template_name = "main/services/remont-v-novostrojkakh.html"


class RemontKottedzhejPage(TemplateView):
    template_name = "main/services/remont-kottedzhej.html"


class KosmeticheskijRemontPage(TemplateView):
    template_name = "main/services/kosmeticheskij-remont.html"


class KapitalnyjRemontKvartirPage(TemplateView):
    template_name = "main/services/kapitalnyj-remont-kvartir.html"


class EvroremontPage(TemplateView):
    template_name = "main/services/evroremont.html"


class NashiRabotiPage(TemplateView):
    template_name = "main/nashi-raboti.html"