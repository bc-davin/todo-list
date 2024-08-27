from django.shortcuts import render
from .serializers import signUpserializers
from rest_framework import status, generics, mixins 
from rest_framework.response import Response
# Create your views here.


class SignUpView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = signUpserializers

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            reponse = {
                "Message": "User created successfully",
                'data': serializer.data,
                'status': status.HTTP_201_CREATED
            }
            return Response(data=reponse, status=status.HTTP_201_CREATED)
    def create(self, request, *args, **kwargs):
        data= request.data
        password = request.data.get('password')
        user = super().create(request, *args, **kwargs)
        user.set_password(password)
        user.save()
        return user