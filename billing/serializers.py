from rest_framework import serializers
from .models import Investor, Investment, Bill, CashCall

class InvestorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'url', 'name', 'address', 'credit', 'iban', 'phone', 'email', 'created_at', 'updated_at']

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    investor_name = serializers.CharField(source='investor.name', read_only=True)

    class Meta:
        model = Investment
        fields = ['id', 'url', 'investor', 'investor_name', 'startup_name', 'invested_amount', 'fee_percentage', 'date_added', 'fees_type', 'created_at', 'updated_at']

class BillSerializer(serializers.HyperlinkedModelSerializer):
    investor_name = serializers.CharField(source='investor.name', read_only=True)
    startup_name = serializers.CharField(source='investment.startup_name', read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'url', 'investor', 'investor_name', 'investment', 'startup_name', 'fees_amount', 'fees_type', 'created_at', 'updated_at']

class CashCallSerializer(serializers.HyperlinkedModelSerializer):
    investor_name = serializers.CharField(source='investor.name', read_only=True)
    class Meta:
        model = CashCall
        fields = ['id', 'url', 'investor', 'investor_name', 'bills', 'iban', 'total_amount', 'invoice_status', 'created_at', 'updated_at']

class InvestorBillsSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True)

    class Meta:
        model = Investor
        fields = ['id', 'name', 'bills']
