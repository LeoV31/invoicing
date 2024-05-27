from datetime import date, datetime
from decimal import Decimal
from .models import Bill

class BillStrategy:
    def generate(self, investor, investment=None):
        raise NotImplementedError

    def bill_exists(self, investor, investment, fees_type):
        current_year = date.today().year
        if investment:
            return Bill.objects.filter(
                investor=investor,
                investment=investment,
                fees_type=fees_type,
                date_added__year=current_year,
            ).exists()
        else:
            return Bill.objects.filter(
                investor=investor,
                fees_type=fees_type,
                date_added__year=current_year
            ).exists()

class MembershipBillStrategy(BillStrategy):
    def generate(self, investor, investment=None):
        if self.bill_exists(investor, None, 'membership'):
            return None

        current_year = date.today().year
        total_invested_this_year = sum(
            investment.invested_amount
            for investment in investor.investments.all()
            if investment.date_added.year == current_year
        )
        if total_invested_this_year > 50000:
            return None     # Skip membership bill
        return Bill(
            investor=investor,
            fees_amount=3000,
            fees_type='membership'
        )

class UpfrontBillStrategy(BillStrategy):
    def generate(self, investor, investment):
        if investment.fees_type == 'upfront' and not self.bill_exists(investor, investment, 'upfront'):
            fees_amount = investment.invested_amount * investment.fee_percentage * Decimal(5)
            return Bill(
                investor=investor,
                investment=investment,
                fees_amount=fees_amount,
                fees_type='upfront'
            )
        return None

class YearlyBillStrategy(BillStrategy):
    def generate(self, investor, investment):
        if investment.fees_type == 'yearly' and not self.bill_exists(investor, investment, 'yearly'):
            today = date.today()
            years_invested = (today - investment.date_added).days / Decimal(365)
            if investment.date_added < datetime(2019, 4, 1).date():
                if years_invested < 1:
                    fees_amount = (today - investment.date_added).days / Decimal(365) * investment.fee_percentage * investment.invested_amount
                else:
                    fees_amount = investment.fee_percentage * investment.invested_amount
            else:
                if years_invested < 1:
                    fees_amount = (today - investment.date_added).days / Decimal(365) * investment.fee_percentage * investment.invested_amount
                elif years_invested < 2:
                    fees_amount = investment.fee_percentage * investment.invested_amount
                elif years_invested < 3:
                    fees_amount = (investment.fee_percentage - Decimal('0.002')) * investment.invested_amount
                elif years_invested < 4:
                    fees_amount = (investment.fee_percentage - Decimal('0.005')) * investment.invested_amount
                else:
                    fees_amount = (investment.fee_percentage - Decimal('0.01')) * investment.invested_amount

            return Bill(
                investor=investor,
                investment=investment,
                fees_amount=fees_amount,
                fees_type='yearly'
            )
        return None
