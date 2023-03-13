from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from accounts.serializer import *
from rest_framework .response import Response
from rest_framework import status


class addUser(APIView):
    def post(self,request):
        ser = UserSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})

class GetUser(ListAPIView):
    qyeryset = User.objects.all()
    serializer_class = UserSerializer

class PutUser(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = User.objects.get(challan_no=pk)
        serializer = UserSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})


class DeleteUser(APIView):
    def post(self, request):
        data = request.data['data']
        User.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)
    
# ------------------------------------------------------------------

class addUserProfile(APIView):
    def post(self,request):
        ser = User_ProfileSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        
        
class GetUserProfile(ListAPIView):
    qyeryset = User_Profile.objects.all()
    serializer_class=User_ProfileSerializer

class PutUserProfile(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = User_Profile.objects.get(challan_no=pk)
        serializer = User_ProfileSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})
        
class DeleteUserProfile(APIView):
    def post(self, request):
        data = request.data['data']
        User_Profile.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)

# -------------------------------------------------------------------------

class addlogin_top(APIView):
    def post(self,request):
        ser = login_topSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        
class Getlogintop(ListAPIView):
    qyeryset = login_top.objects.all()
    serializer_class=login_topSerializer


class Putlogintop(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = login_top.objects.get(challan_no=pk)
        serializer = login_topSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})
        

class Deletelogintop(APIView):
    def post(self, request):
        data = request.data['data']
        login_top.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)

# ---------------------------------------------------------------------

class addUserCartProduct(APIView):
    def post(self,request):
        ser = UserCartProductSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        
class GetUserCartProduct(ListAPIView):
    qyeryset = UserCartProduct.objects.all()
    serializer_class=UserCartProductSerializer


class PutUserCartProduct(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = UserCartProduct.objects.get(challan_no=pk)
        serializer = UserCartProductSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})
        

class DeleteUserCartProduct(APIView):
    def post(self, request):
        data = request.data['data']
        UserCartProduct.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)

# ------------------------------------------------------

class addUserCart(APIView):
    def post(self,request):
        ser = UserCartSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        
        
class GetUserCart(ListAPIView):
    qyeryset = UserCart.objects.all()
    serializer_class=UserCartSerializer


class PutUserCart(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = UserCart.objects.get(challan_no=pk)
        serializer = UserCartSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})


class DeleteUserCart(APIView):
    def post(self, request):
        data = request.data['data']
        UserCartProduct.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)
