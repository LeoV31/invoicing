from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Investor(TimestampedModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    credit = models.TextField()
    iban = models.CharField(max_length=34)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Investment(TimestampedModel):
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

class Bill(TimestampedModel):
    investor = models.ForeignKey(Investor, related_name='bills', on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, related_name='bills', on_delete=models.CASCADE, null=True, blank=True)
    fees_amount = models.DecimalField(max_digits=10, decimal_places=2)
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

class CashCall(TimestampedModel):
    investor = models.ForeignKey(Investor, related_name='cash_calls', on_delete=models.CASCADE)
    bills = models.ManyToManyField(Bill)
    iban = models.CharField(max_length=34)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(
        max_length=10,
        choices = [
            ('created', 'Created'),
            ('validated', 'Validated'),
            ('sent', 'Sent'),
            ('paid', 'Paid'),
            ('overdue', 'Overdue'),
        ]
    )

    def __str__(self):
        return f"CashCall id: {self.id} of ${self.total_amount} for {self.investor.name}"
