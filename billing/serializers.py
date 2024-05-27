from rest_framework import serializers
from .models import Investor, Investment, Bill, CashCall

class InvestorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investor
        fields = ['url', 'id', 'name', 'address', 'credit', 'phone', 'email']

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investment
        fields = ['url', 'id', 'investor', 'startup_name', 'invested_amount', 'fee_percentage', 'date_added', 'fees_type']

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['url', 'id', 'investor', 'investment', 'fees_amount', 'date_added', 'fees_type']

class CashCallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CashCall
        fields = ['url', 'id', 'investor', 'bills', 'iban', 'date_added', 'date_modified', 'total_amount', 'invoice_status']
