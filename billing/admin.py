from django.contrib import admin
from .models import Investor, Investment, Bill, CashCall

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'credit', 'phone', 'email')
    search_fields = ('name', 'email')

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('investor', 'startup_name', 'invested_amount', 'fee_percentage', 'date_added', 'fees_type')
    list_filter = ('investor', 'fees_type')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('investor', 'investment', 'fees_amount', 'date_added', 'fees_type')
    list_filter = ('investor', 'fees_type')
    search_fields = ('investor__name', 'investment__startup_name')

@admin.register(CashCall)
class CashCallAdmin(admin.ModelAdmin):
    list_display = ('investor', 'total_amount', 'invoice_status', 'date_added', 'date_modified')
    list_filter = ('investor', 'invoice_status')
    filter_horizontal = ('bills',)
    search_fields = ('investor__name',)
