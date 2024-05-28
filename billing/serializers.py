from rest_framework import serializers
from .models import Investor, Investment, Bill, CashCall

class InvestorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investor
        fields = ['url', 'id', 'name', 'address', 'credit', 'iban', 'phone', 'email', 'created_at', 'updated_at']

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investment
        fields = ['url', 'id', 'investor', 'startup_name', 'invested_amount', 'fee_percentage', 'date_added', 'fees_type', 'created_at', 'updated_at']

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['url', 'id', 'investor', 'investment', 'fees_amount', 'fees_type', 'created_at', 'updated_at']

class CashCallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CashCall
        fields = ['url', 'id', 'investor', 'bills', 'iban', 'total_amount', 'invoice_status', 'created_at', 'updated_at']

class InvestorBillsSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True)

    class Meta:
        model = Investor
        fields = ['id', 'name', 'bills']
