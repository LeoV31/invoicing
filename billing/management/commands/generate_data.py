import random
from django.core.management.base import BaseCommand
from billing.models import Investor, Investment
from decimal import Decimal
from datetime import date

class Command(BaseCommand):
    help = 'Generate investors and their investments'

    investor_names = [
        "Laurent Dassault",
        "Nicolas Motelay",
        "Philippe Carle",
        "Stéphane Carvile",
        "Christiane Marcellier",
        "Fabrice Domange",
        "Laurence Bret",
        "Jean-Luc Allavena",
        "Alain Pourcelot",
        "David Amsellem",
    ]

    startup_names = [
        "moso", "Groover", "Jellysmack", "HOMA", "hive", "stokelp",
        "Pickme", "sonio", "ekie", "look sider", "PhantomBuster",
        "hellosafe", "shotgun", "benefiz", "Glose", "choose"
    ]

    def handle(self, *args, **kwargs):
        for investor_name in self.investor_names:
            investor = Investor.objects.create(
                name=investor_name,
                address="C/ de Rosa Sensat, 9, Sant Martí, 08005 Barcelona",
                credit="Mastercard 5594099635534392 05/25 CVV: 553",
                iban=self.generate_iban(),
                phone=self.generate_phone(),
                email=self.generate_email(investor_name)
            )
            self.create_investments(investor)
            self.stdout.write(self.style.SUCCESS(f'Successfully created investor: {investor.name} and his/her investments.'))

    def create_investments(self, investor):
        for year in range(2017, 2025):
            for _ in range(random.randint(0, 1)):
                Investment.objects.create(
                    investor=investor,
                    startup_name=random.choice(self.startup_names),
                    invested_amount=self.generate_invested_amount(),
                    fee_percentage=self.generate_fee_percentage(),
                    date_added=self.generate_date(year),
                    fees_type=random.choice(['upfront', 'yearly'])
                )

    def generate_iban(self):
        return 'FR76' + ''.join([str(random.randint(0, 9)) for _ in range(18)])

    def generate_phone(self):
        return '+33' + ''.join([str(random.randint(0, 9)) for _ in range(9)])

    def generate_email(self, name):
        return f"{name.replace(' ', '').lower()}@example.com"

    def generate_invested_amount(self):
        return Decimal(random.choice(range(10000, 110000, 10000)))

    def generate_fee_percentage(self):
        return Decimal(random.uniform(0.10, 0.15)).quantize(Decimal('0.001'))

    def generate_date(self, year):
        if year == 2024:
            month = random.randint(1, 4)
            day = random.randint(1, 28)
        else:
            month = random.randint(1, 4)
            day = random.randint(1, 28)
        return date(year, month, day)
