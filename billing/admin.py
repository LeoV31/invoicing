from django.contrib import admin
from .models import Investor, Investment, Bill, CashCall

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'credit', 'iban', 'phone', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'updated_at')

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'investor', 'startup_name', 'invested_amount', 'fee_percentage', 'date_added', 'fees_type', 'created_at', 'updated_at')
    search_fields = ('startup_name', 'investor__name')
    list_filter = ('fees_type', 'date_added', 'created_at')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'investor', 'startup_name', 'fees_amount', 'fees_type', 'created_at', 'updated_at')
    search_fields = ('investor__name', 'investment__startup_name')
    list_filter = ('fees_type', 'created_at')

    def startup_name(self, obj):
        return obj.investment.startup_name if obj.investment else None
    startup_name.short_description = 'Startup Name'


@admin.register(CashCall)
class CashCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'investor', 'iban', 'total_amount', 'invoice_status', 'created_at', 'updated_at')
    search_fields = ('investor__name', 'iban')
    list_filter = ('invoice_status', 'created_at')

    def investor_name(self, obj):
        return obj.investor.name
    investor_name.short_description = 'Investor Name'
