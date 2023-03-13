from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from product.serializer import *
from rest_framework .response import Response
from rest_framework import status

class addproductMain(APIView):
    def post(self,request):
        ser = productMainSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        


class GetproductMain(ListAPIView):
    qyeryset = productMain.objects.all()
    serializer_class = productMainSerializer

class PutproductMain(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = productMain.objects.get(challan_no=pk)
        serializer = productMainSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})


class DeleteproductMain(APIView):
    def post(self, request):
        data = request.data['data']
        productMain.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)
    

    
# ------------------------------------------------------------------



class addproductImage(APIView):
    def post(self,request):
        ser = productImageSerializer(data=request.data,partial=True)
        if ser.is_valid:
            ser.save()
            return Response({"status": "success","data":ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error","data":ser.errors})
        
class GetproductImage(ListAPIView):
    qyeryset = productImage.objects.all()
    serializer_class = productImageSerializer

class PutproductImage(APIView):
    def put(self,request,pk,format=None):
        print (request.data)
        userdetails = productImage.objects.get(challan_no=pk)
        serializer = productImageSerializer(userdetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors})


class DeleteproductImage(APIView):
    def post(self, request):
        data = request.data['data']
        productImage.objects.filter(id__in=data).delete()
        return Response(status=status.HTTP_200_OK)
