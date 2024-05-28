from django.core.management.base import BaseCommand
from billing.models import Investor, Bill, CashCall
from decimal import Decimal
from datetime import date
from django.db.models import Sum


class Command(BaseCommand):
    help = 'Generate cash calls for the current year bills'

    def handle(self, *args, **kwargs):
        current_year = date.today().year
        investors = Investor.objects.all()

        for investor in investors:
            # Find all bills for the current year
            bills = Bill.objects.filter(investor=investor, created_at__year=current_year)

            # Check if there's a paid cash call for the current year
            paid_cash_calls = CashCall.objects.filter(
                investor=investor,
                created_at__year=current_year,
                invoice_status='paid'
            )

            for paid_cash_call in paid_cash_calls:
                paid_bills = paid_cash_call.bills.all()
                bills = bills.exclude(id__in=paid_bills.values_list('id', flat=True))

            if bills.exists():
                total_amount = bills.aggregate(total=Sum('fees_amount')).get('total') or Decimal('0.00')

                cash_call = CashCall.objects.create(
                    investor=investor,
                    total_amount=total_amount,
                    iban=investor.iban,
                    invoice_status='created'
                )
                cash_call.bills.set(bills)
                cash_call.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully created cash call for investor: {investor.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'No new bills to include in the cash call for investor {investor.name}'))
