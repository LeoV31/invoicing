import pytest
from billing.models import Investor, Investment, Bill, CashCall
from datetime import date
from decimal import Decimal
from django.utils import timezone

@pytest.mark.django_db
def test_investor_creation():
    investor = Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )
    assert investor.name == "Leo Viguier"
    assert investor.address == "Barcelona"
    assert investor.credit == "1234"
    assert investor.phone == "+336438484844"
    assert investor.email == "leo@gmail.com"
    assert investor.created_at is not None
    assert investor.updated_at is not None
    assert investor.created_at <= timezone.now()
    assert investor.updated_at <= timezone.now()

@pytest.mark.django_db
def test_investment_creation():
    investor = Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )
    investment = Investment.objects.create(
        investor=investor,
        startup_name="Motion Society",
        invested_amount=Decimal('15000.00'),
        fee_percentage=Decimal('0.1'),
        date_added=date(2022, 1, 1),
        fees_type="yearly"
    )
    assert investment.investor == investor
    assert investment.startup_name == "Motion Society"
    assert investment.invested_amount == Decimal('15000.00')
    assert investment.fee_percentage == Decimal('0.1')
    assert investment.date_added == date(2022, 1, 1)
    assert investment.fees_type == "yearly"
    assert investment.created_at is not None
    assert investment.updated_at is not None
    assert investment.created_at <= timezone.now()
    assert investment.updated_at <= timezone.now()

@pytest.mark.django_db
def test_bill_creation():
    investor = Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )
    investment = Investment.objects.create(
        investor=investor,
        startup_name="Motion Society",
        invested_amount=Decimal('15000.00'),
        fee_percentage=Decimal('0.1'),
        date_added=date(2022, 1, 1),
        fees_type="yearly"
    )
    bill = Bill.objects.create(
        investor=investor,
        investment=investment,
        fees_amount=Decimal('1500.00'),
        fees_type="yearly"
    )
    assert bill.investor == investor
    assert bill.investment == investment
    assert bill.fees_amount == Decimal('1500.00')
    assert bill.fees_type == "yearly"
    assert bill.created_at is not None
    assert bill.updated_at is not None
    assert bill.created_at <= timezone.now()
    assert bill.updated_at <= timezone.now()

@pytest.mark.django_db
def test_cashcall_creation():
    investor = Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )
    investment = Investment.objects.create(
        investor=investor,
        startup_name="Motion Society",
        invested_amount=Decimal('15000.00'),
        fee_percentage=Decimal('0.10'),
        date_added=date(2022, 1, 1),
        fees_type="yearly"
    )
    bill1 = Bill.objects.create(
        investor=investor,
        investment=investment,
        fees_amount=Decimal('1500.00'),
        fees_type="yearly"
    )
    bill2 = Bill.objects.create(
        investor=investor,
        fees_amount=Decimal('3000.00'),
        fees_type="membership"
    )
    cashcall = CashCall.objects.create(
        investor=investor,
        iban="FR89370400440532013000",
        total_amount=Decimal('4500.00'),
        invoice_status="validated"
    )
    cashcall.bills.set([bill1, bill2])
    cashcall.save()

    assert cashcall.investor == investor
    assert cashcall.iban == "FR89370400440532013000"
    assert cashcall.total_amount == Decimal('4500.00')
    assert cashcall.invoice_status == "validated"
    assert list(cashcall.bills.all()) == [bill1, bill2]
    assert cashcall.created_at is not None
    assert cashcall.updated_at is not None
    assert cashcall.created_at <= timezone.now()
    assert cashcall.updated_at <= timezone.now()
