from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

import json

# Create your views here.

class webhookDialog(APIView):

    def post(self, request, format=None):
        # build a request object
        req = json.loads(request.body)
        # get action from json
        action = req.get('queryResult').get('action')
        # return a fulfillment message
        fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}

        return Response(fulfillmentText)