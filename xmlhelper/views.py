#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import XmlDocForm
from .models import XmlDoc, Result
from lxml import etree, html
from django.template import loader


def index(request):
    return render(request, 'xmlhelper/index.html')


def xpath(request):
    if request.method == "POST":
        form = XmlDocForm(request.POST)
        if form.is_valid():
            doc = form.save()
            form_handler()
            doc.save()
    else:
        form = XmlDocForm()

    title1 = "Write your XML document here"
    title2 = "Write your XPath query here"

    return render(request, 'xmlhelper/xpath.html', {'form': form,
                                                    'title1': title1,
                                                    'title2': title2,
                                                    })


def form_handler():
    doc_num = XmlDoc.objects.count()
    xmldoc = XmlDoc.objects.get(pk=doc_num)
    xmldoc.print_xml()


def result_handler(request):
    template = loader.get_template('xmlhelper/new.html')

    parsed_xml = html.parse('/home/kat/course/xmlhelper/templates/xmlhelper/data.xml')

    obj_num = XmlDoc.objects.count()
    last_obj = XmlDoc.objects.get(pk=obj_num)
    xpath_q = last_obj.xpath_query

    result_text = parsed_xml.xpath(xpath_q) # example in ex.html

    isEmpty = False

    if result_text:
        Result.create(result_text).save()
    else:
        isEmpty = True

    obj_num = Result.objects.count()
    results = Result.objects.get(pk=obj_num)

    context = {
        'results': results,
        'isEmpty': isEmpty,
    }

    return HttpResponse(template.render(context, request))


def contact(request):
    return render(request, 'xmlhelper/contact.html')

