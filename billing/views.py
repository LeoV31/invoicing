from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Investor, Investment, Bill, CashCall
from .serializers import InvestorSerializer, InvestmentSerializer, BillSerializer, CashCallSerializer, InvestorBillsSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'investors': reverse('investor-list', request=request, format=format),
        'investments': reverse('investment-list', request=request, format=format),
        'bills': reverse('bill-list', request=request, format=format),
        'grouped-bills': reverse('grouped-bills', request=request, format=format),
        'cashcalls': reverse('cashcall-list', request=request, format=format),
    })

@api_view(['GET', 'POST'])
def investor_list(request):
    if request.method == 'GET':
        investors = Investor.objects.all()
        serializer = InvestorSerializer(investors, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvestorSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def investor_detail(request, pk):
    try:
        investor = Investor.objects.get(pk=pk)
    except Investor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvestorSerializer(investor, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvestorSerializer(investor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        investor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def investment_list(request):
    if request.method == 'GET':
        investments = Investment.objects.all()
        serializer = InvestmentSerializer(investments, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvestmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def investment_detail(request, pk):
    try:
        investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvestmentSerializer(investment, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvestmentSerializer(investment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def bill_list(request):
    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BillSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bill_detail(request, pk):
    try:
        bill = Bill.objects.get(pk=pk)
    except Bill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillSerializer(bill, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BillSerializer(bill, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cashcall_list(request):
    if request.method == 'GET':
        cashcalls = CashCall.objects.all()
        serializer = CashCallSerializer(cashcalls, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CashCallSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cashcall_detail(request, pk):
    try:
        cashcall = CashCall.objects.get(pk=pk)
    except CashCall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CashCallSerializer(cashcall, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CashCallSerializer(cashcall, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cashcall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def grouped_bills_view(request):
    investors = Investor.objects.prefetch_related('bills').all()
    serializer = InvestorBillsSerializer(investors, many=True, context={'request': request})
    return Response(serializer.data)
