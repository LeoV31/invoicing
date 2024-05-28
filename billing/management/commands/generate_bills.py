from django.core.management.base import BaseCommand
from billing.models import Investor, Investment
from billing.bill_strategies import MembershipBillStrategy, UpfrontBillStrategy, YearlyBillStrategy

class Command(BaseCommand):
    help = 'Generate bills for investments'

    def handle(self, *args, **kwargs):
        investors = Investor.objects.all()
        membership_strategy = MembershipBillStrategy()
        upfront_strategy = UpfrontBillStrategy()
        yearly_strategy = YearlyBillStrategy()

        for investor in investors:
            bills_created = False
            membership_bill = membership_strategy.generate(investor)
            if membership_bill:
                membership_bill.save()
                bills_created = True

            investments = investor.investments.all()
            for investment in investments:
                upfront_bill = upfront_strategy.generate(investor, investment)
                if upfront_bill:
                    upfront_bill.save()
                    bills_created = True

                yearly_bill = yearly_strategy.generate(investor, investment)
                if yearly_bill:
                    yearly_bill.save()
                    bills_created = True
            if bills_created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created bills for investor: {investor.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'No bills created for investor: {investor.name}'))
