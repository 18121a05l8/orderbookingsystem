import imp
from re import I
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def order(input,showorders,executeorders,from_date,to_date,stock,execute_qty,execution_price):
    try:
        inputdata=json.loads(input.body)
        if(showorders and not executeorders):
            output=dict()
            i=1
            for inp in input['stock']:
                if inp['data']>from_date and inp['data']<to_date:
                    output['s.no'].append(i)
                    output['Stock'].append(stock)
                    output['orderqty'].append(inp['orderqty'])
                    output['ordertype'].append(inp['ordertype'])
                    output['executedqty'].append(inp['executedqty'])
                    output['price'].append(inp['price'])
                    output['order_status'].append("Processed")
                    output['orderdate'].append(inp["date"])
                    i+=1
            return JsonResponse(output)
        elif(executeorders):
            output=dict()
            i=1
            for inp in input['stock']:
                if inp['data']>from_date and inp['data']<to_date:
                    output['s.no'].append(i)            
                    output['Stock'].append(stock)
                    output['orderqty'].append(inp['orderqty'])
                    output['ordertype'].append(inp['ordertype'])
                    if execute_qty>=inp['orderqty']:
                        execute_qty-=inp['orderqty']
                        output['executedqty']=execute_qty
                        output['order_status'].append("accepted")
                    elif execute_qty!=0 and execute_qty<inp["orderqty"]:
                        execute_qty=0
                        output['executeqty']=execute_qty
                        output['order_status'].append("accepted")
                    elif execute_qty==0:
                        output['order_status'].append("Rejected")
                    output['price'].append(inp['price'])
                    output['orderdate'].append(inp["date"])
                    i+=1
            return JsonResponse(output)
    except:
        return Response(status.HTTP_400_BAD_REQUEST)
    







