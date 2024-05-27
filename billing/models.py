from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    credit = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Investment(models.Model):
    investor = models.ForeignKey(Investor, related_name='investments', on_delete=models.CASCADE)
    startup_name = models.CharField(max_length=255)
    invested_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=3)
    date_added = models.DateField()
    fees_type = models.CharField(
        max_length=10,
        choices = [
            ('upfront', 'Upfront'),
            ('yearly', 'Yearly'),
        ]
    )

    def __str__(self):
        return f"Investment id: {self.id} in {self.startup_name} by {self.investor.name}"

class Bill(models.Model):
    investor = models.ForeignKey(Investor, related_name='bills', on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, related_name='bills', on_delete=models.CASCADE, null=True, blank=True)
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    fees_type = models.CharField(
        max_length=10,
        choices = [
            ('membership', 'Membership'),
            ('upfront', 'Upfront'),
            ('yearly', 'Yearly'),
        ]
    )

    def __str__(self):
        return f"Bill id: {self.id} of ${self.fees_amount} for {self.investor.name}"

class CashCall(models.Model):
    investor = models.ForeignKey(Investor, related_name='cash_calls', on_delete=models.CASCADE)
    bills = models.ManyToManyField(Bill)
    iban = models.CharField(max_length=34)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(
        max_length=10,
        choices = [
            ('validated', 'Validated'),
            ('sent', 'Sent'),
            ('paid', 'Paid'),
            ('overdue', 'Overdue'),
        ]
    )

    def __str__(self):
        return f"CashCall id: {self.id} of ${self.total_amount} for {self.investor.name}"
