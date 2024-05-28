import pytest
from rest_framework.test import APIRequestFactory
from billing.serializers import InvestorSerializer, InvestmentSerializer, BillSerializer, CashCallSerializer
from billing.models import Investor, Investment, Bill, CashCall
from decimal import Decimal
from datetime import date

@pytest.fixture
def api_request_factory():
    return APIRequestFactory()

@pytest.fixture
def investor():
    return Investor.objects.create(
        name="Leo Viguier",
        address="Barcelona",
        credit="1234",
        phone="+336438484844",
        email="leo@gmail.com"
    )

@pytest.fixture
def investment(investor):
    return Investment.objects.create(
        investor=investor,
        startup_name="Motion Society",
        invested_amount=Decimal('15000.00'),
        fee_percentage=Decimal('0.100'),
        date_added=date(2022, 1, 1),
        fees_type="yearly"
    )

@pytest.fixture
def bill(investor, investment):
    return Bill.objects.create(
        investor=investor,
        investment=investment,
        fees_amount=Decimal('1500.00'),
        fees_type="yearly"
    )

@pytest.fixture
def cashcall(investor, bill):
    cashcall = CashCall.objects.create(
        investor=investor,
        iban="FR89370400440532013000",
        total_amount=Decimal('1500.00'),
        invoice_status="validated"
    )
    cashcall.bills.set([bill])
    cashcall.save()
    return cashcall

@pytest.mark.django_db
def test_investor_serializer(api_request_factory, investor):
    request = api_request_factory.get('/')

    # Serialize the investor instance
    serializer = InvestorSerializer(investor, context={'request': request})
    serialized_data = serializer.data
    assert serialized_data['name'] == investor.name
    assert serialized_data['address'] == investor.address
    assert serialized_data['credit'] == investor.credit
    assert serialized_data['phone'] == investor.phone
    assert serialized_data['email'] == investor.email
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data

@pytest.mark.django_db
def test_investment_serializer(api_request_factory, investment):
    request = api_request_factory.get('/')

    # Serialize the investment instance
    serializer = InvestmentSerializer(investment, context={'request': request})
    serialized_data = serializer.data
    expected_investor_url = f'http://testserver/investor/{investment.investor.id}/'
    assert serialized_data['investor'] == expected_investor_url
    assert serialized_data['investor_name'] == investment.investor.name
    assert serialized_data['startup_name'] == investment.startup_name
    assert serialized_data['invested_amount'] == str(investment.invested_amount)
    assert serialized_data['fee_percentage'] == str(investment.fee_percentage)
    assert serialized_data['date_added'] == str(investment.date_added)
    assert serialized_data['fees_type'] == investment.fees_type
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data

@pytest.mark.django_db
def test_bill_serializer(api_request_factory, bill):
    request = api_request_factory.get('/')

    # Serialize the bill instance
    serializer = BillSerializer(bill, context={'request': request})
    serialized_data = serializer.data
    expected_investor_url = f'http://testserver/investor/{bill.investor.id}/'
    expected_investment_url = f'http://testserver/investment/{bill.investment.id}/'
    assert serialized_data['investor'] == expected_investor_url
    assert serialized_data['investor_name'] == bill.investor.name
    assert serialized_data['investment'] == expected_investment_url
    assert serialized_data['startup_name'] == bill.investment.startup_name
    assert serialized_data['fees_amount'] == str(bill.fees_amount)
    assert serialized_data['fees_type'] == bill.fees_type
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data

@pytest.mark.django_db
def test_cashcall_serializer(api_request_factory, cashcall):
    request = api_request_factory.get('/')

    # Serialize the cash call instance
    serializer = CashCallSerializer(cashcall, context={'request': request})
    serialized_data = serializer.data
    expected_investor_url = f'http://testserver/investor/{cashcall.investor.id}/'
    expected_bills_url = [f'http://testserver/bill/{bill.id}/' for bill in cashcall.bills.all()]
    assert serialized_data['investor'] == expected_investor_url
    assert serialized_data['investor_name'] == cashcall.investor.name
    assert serialized_data['bills'] == expected_bills_url
    assert serialized_data['iban'] == cashcall.iban
    assert serialized_data['total_amount'] == str(cashcall.total_amount)
    assert serialized_data['invoice_status'] == cashcall.invoice_status
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data
