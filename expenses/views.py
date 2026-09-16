from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer

@api_view(['POST'])
def create_expense_api(request):
    serializer=ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)


@api_view(['GET'])
def list_expense_api(request):
    exp=Expense.objects.all()
    serializer=ExpenseSerializer(exp , many=True)
    return Response(serializer.data , status=200)


@api_view(['GET'])
def detail_expense_api(request,id):
    exp=Expense.objects.get(id=id)
    serializer=ExpenseSerializer(exp)
    return Response(serializer.data,status=200)


@api_view(['PATCH'])
def update_expense_api(request,id):
    exp=Expense.objects.get(id=id)
    serializer=ExpenseSerializer(exp , data=request.data , partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=206)
    return Response(serializer.errors , status=400)


@api_view(['DELETE'])
def delete_expense_api(request,id):
    exp=Expense.objects.get(id=id)
    exp.delete()
    return Response(status=204)

