from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import ProductLine, Product, Feature
from django.db import connection
import json


def prodhome(request):
    context = {
        'productLine': ProductLine.objects.all(),
        'product': Product.objects.all(),
        'features': Feature.objects.all()
    }
    return render(request, 'product/prodhome.html', context)


def proddata(request):

    cursor = connection.cursor()
    cursor.execute("Select ppl.productLineName, pp.productName, pf.featureName from product_productline as ppl INNER JOIN product_product as pp ON ppl.id = pp.ProdLine_id LEFT JOIN product_feature as pf ON pp.id = pf.prodParent_id;")
    r = cursor.fetchall()
    rlist = json.dumps(r)

    cursor.execute("Select count(*) from product_productline as ppl INNER JOIN product_product as pp ON ppl.id = pp.ProdLine_id LEFT JOIN product_feature as pf ON pp.id = pf.prodParent_id;")
    count = cursor.fetchone()
    print(r, count)
    return render(request, 'product/prodhome.html', {'data': rlist, 'count': count})
