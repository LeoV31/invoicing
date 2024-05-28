"""
from django.core.management.base import BaseCommand
from billing.models import Investor, Investment, Bill
from datetime import date
import random

class Command(BaseCommand):
    help = 'Create test data for investors, investments, and bills'

    def handle(self, *args, **kwargs):
        # Create a dozen investors
        for i in range(1, 13):
            investor = Investor.objects.create(
                name=f"Investor {i}",
                address=f"{i} Main Street",
                credit="Good",
                phone=f"555-010{i:02d}",
                email=f"investor{i}@example.com"
            )

            # Create a few investments for each investor
            for j in range(1, 4):  # 3 investments per investor
                investment = Investment.objects.create(
                    investor=investor,
                    startup_name=f"Startup {j}",
                    invested_amount=random.uniform(10000, 100000),
                    fee_percentage=random.uniform(1, 5),
                    date_added=date(2023, random.randint(1, 12), random.randint(1, 28)),
                    fees_type=random.choice(['upfront', 'yearly'])
                )

        self.stdout.write(self.style.SUCCESS('Successfully created test data'))
"""
