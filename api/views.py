from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from rest_framework import authentication,permissions

from rest_framework.decorators import action

from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView

from api.serializers import CustomerSerializers,WorkSerializers

from django.contrib.auth.models import User

from api.models import Customer,Work


# Create your views here.

class CustomerViewsetView(ModelViewSet):

    serializer_class=CustomerSerializers

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self,serializer):

        serializer.save(technician=self.request.user)


    #url:http://127.0.0.1:8000/api/customers/{id}/add_work/
    #method:post


   # @action(methods=["post"],detail=True)
    #def add_work(self,request,*args,**kwargs):

     #   id=kwargs.get("pk")

      #  customer_instance=Customer.objects.get(id=id)

       # serializer_instance=WorkSerializers(data=request.data)

        #if serializer_instance.is_valid():
#
 #           serializer_instance.save(customer=customer_instance)
#
 #           return Response(data=serializer_instance.data)
        
  #      else:

   #         return Response(data=serializer_instance.errors)
        



# rest_framework.generics.py

#CreateApiView (create)View()
#ListApiView() list
#RetriveApiView()
#UpdateApiView
#DestroyApiView()


class WorkCreativeView(CreateAPIView):

    serializer_class=WorkSerializers

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self,serializer):

        id=self.kwargs.get("pk")

        customer_instance=Customer.objects.get(id=id)

        serializer.save(customer=customer_instance)


class WorkDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class=WorkSerializers

    queryset=Work.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    





