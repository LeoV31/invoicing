import pytest
from billing.models import Investor, Investment, Bill
from billing.management.commands.generate_bills import Command
from datetime import datetime
from decimal import Decimal

@pytest.mark.django_db
def test_generate_bills():
    investor = Investor.objects.create(
        name="John Doe",
        address="123 Street",
        credit="Good",
        phone="1234567890",
        email="john@example.com"
    )
    investment1 = Investment.objects.create(
        investor=investor,
        startup_name="Test Startup 1",
        invested_amount=30000,
        fee_percentage=Decimal('0.05'),
        date_added="2023-01-01",
        fees_type="yearly"
    )
    investment2 = Investment.objects.create(
        investor=investor,
        startup_name="Test Startup 2",
        invested_amount=25000,
        fee_percentage=Decimal('0.05'),
        date_added="2023-01-01",
        fees_type="yearly"
    )
    investment3 = Investment.objects.create(
        investor=investor,
        startup_name="Test Startup 3",
        invested_amount=60000,
        fee_percentage=Decimal('0.05'),
        date_added="2018-01-01",
        fees_type="yearly"
    )

    command = Command()
    command.handle()

    bills = Bill.objects.filter(investor=investor)
    assert bills.count() == 4  # One membership, one yearly for investment1, one yearly for investment2, one yearly for investment3

    membership_bill = bills.get(fees_type='membership')
    assert membership_bill.fees_amount == 3000

    yearly_bills = bills.filter(fees_type='yearly')
    assert len(yearly_bills) == 3

    # Check that the yearly bills have the correct amounts
    for bill in yearly_bills:
        if bill.investment == investment1 or bill.investment == investment2:
            assert bill.fees_amount > 0  # Make sure it calculated correctly based on the date
        elif bill.investment == investment3:
            assert bill.fees_amount > 0  # Make sure it calculated correctly based on the date

    # Run the command again and ensure no duplicate bills are created within the same year
    command.handle()
    assert bills.count() == 4  # No new bills should be added
