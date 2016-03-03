__author__ = 'kat'

from django.forms import ModelForm, Textarea
from models import XmlDoc


class XmlDocForm(ModelForm):

    class Meta:
        model = XmlDoc
        fields = '__all__'
        labels = {
            'xml_document': 'Write your XML document here',
        }
        help_texts = {
            'xml_document': 'Some useful help text.',
        }
        widgets = {
            'xml_document': Textarea(attrs={'cols': 70, 'rows': 10}),
            'xpath_query': Textarea(attrs={'cols': 70, 'rows': 10}),
        }