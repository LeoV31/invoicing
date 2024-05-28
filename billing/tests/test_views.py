import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from billing.models import Investor, Investment, Bill, CashCall
from decimal import Decimal
from datetime import date

@pytest.fixture
def api_client():
    return APIClient()

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
        fee_percentage=Decimal('0.1'),
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
def test_investor_list(api_client, investor):
    url = reverse('investor-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == investor.name

@pytest.mark.django_db
def test_investor_detail(api_client, investor):
    url = reverse('investor-detail', args=[investor.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == investor.name

@pytest.mark.django_db
def test_investment_list(api_client, investment):
    url = reverse('investment-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['startup_name'] == investment.startup_name

@pytest.mark.django_db
def test_investment_detail(api_client, investment):
    url = reverse('investment-detail', args=[investment.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['startup_name'] == investment.startup_name

@pytest.mark.django_db
def test_bill_list(api_client, bill):
    url = reverse('bill-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['fees_amount'] == str(bill.fees_amount)

@pytest.mark.django_db
def test_bill_detail(api_client, bill):
    url = reverse('bill-detail', args=[bill.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['fees_amount'] == str(bill.fees_amount)

@pytest.mark.django_db
def test_cashcall_list(api_client, cashcall):
    url = reverse('cashcall-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['total_amount'] == str(cashcall.total_amount)

@pytest.mark.django_db
def test_cashcall_detail(api_client, cashcall):
    url = reverse('cashcall-detail', args=[cashcall.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['total_amount'] == str(cashcall.total_amount)
