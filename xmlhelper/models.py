from __future__ import unicode_literals
from django.db import models


class XmlDoc(models.Model):
    xml_document = models.TextField()
    xpath_query = models.TextField()

    def print_xml(self):
        xml_file = open("xmlhelper/templates/xmlhelper/data.xml", "w")
        xml_file.write(str(self.xml_document))
        xml_file.close()


class Result(models.Model):
    res = models.TextField()

    @classmethod
    def create(cls, text):
        result = cls(res=text)
        return result

