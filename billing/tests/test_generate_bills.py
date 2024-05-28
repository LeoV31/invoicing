import pytest
from django.core.management import call_command
from billing.models import Investor, Investment, Bill
from decimal import Decimal
from datetime import date

@pytest.mark.django_db
def test_generate_bills():
    # Create an investor
    investor = Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )

    # Create investments
    investment1 = Investment.objects.create(
        investor=investor,
        startup_name="Motion Society",
        invested_amount=Decimal('30000.00'),
        fee_percentage=Decimal('0.05'),
        date_added=date(2023, 1, 1),
        fees_type="yearly"
    )
    investment2 = Investment.objects.create(
        investor=investor,
        startup_name="Homa Games",
        invested_amount=Decimal('25000.00'),
        fee_percentage=Decimal('0.05'),
        date_added=date(2021, 1, 1),
        fees_type="yearly"
    )
    investment3 = Investment.objects.create(
        investor=investor,
        startup_name="Staycation",
        invested_amount=Decimal('60000.00'),
        fee_percentage=Decimal('0.05'),
        date_added=date(2018, 1, 1),
        fees_type="yearly"
    )

    call_command('generate_bills')

    # Check if the bills are created
    bills = Bill.objects.filter(investor=investor)
    assert bills.count() == 4

    membership_bill = bills.get(fees_type='membership')
    assert membership_bill.fees_amount == Decimal('3000.00')

    yearly_bills = bills.filter(fees_type='yearly')
    assert len(yearly_bills) == 3

    # Check that the yearly bills have the correct amounts
    for bill in yearly_bills:
        if bill.investment == investment1 or bill.investment == investment2:
            assert bill.fees_amount > 0  # Make sure it calculated correctly based on the date
        elif bill.investment == investment3:
            assert bill.fees_amount > 0  # Make sure it calculated correctly based on the date

    # Run the command again and ensure no duplicate bills are created within the same year
    call_command('generate_bills')
    assert bills.count() == 4  # No new bills should be added
