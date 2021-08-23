from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app1.models import StudentInfo
from app1.serializers import StudentInfoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def studentInfo_list(request):
    """
    List all code StudentInfo, or create a new StudentInfo.
    """
    if request.method == 'GET':
        studentlist = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(studentlist, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentInfo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        studentinfo = StudentInfo.objects.get(pk=pk)
    except StudentInfo.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentInfoSerializer(studentinfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentInfoSerializer(studentinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        studentinfo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
