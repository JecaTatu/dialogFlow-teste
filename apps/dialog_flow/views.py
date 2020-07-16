from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from apps.user.models import User

import json

# Create your views here.

class webhookDialog(APIView):

    def post(self, request, format=None):

        req = json.loads(request.body)

        action = req.get('queryResult').get('action')
        parameters = req.get('queryResult').get('parameters')

        if action == "register":
            user = User.objects.filter(email=parameters['email']).exists()
            if not user:
                users = User.objects.count()
                new_user = User.objects.create_user(
                    name=parameters['name'], username=parameters['name']+str(users), email=parameters['email'], password='asdqwe123'
                )

        fulfillmentText = {'fulfillmentText': 'Obrigada por se cadastrar, isso nos ajuda muito!'}

        return Response(fulfillmentText)