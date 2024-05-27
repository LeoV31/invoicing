# Generated by Django 5.0.6 on 2024-05-27 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=255)),
                ('invested_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateField()),
                ('fees_type', models.CharField(choices=[('upfront', 'Upfront'), ('yearly', 'Yearly')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('credit', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('fees_type', models.CharField(choices=[('membership', 'Membership'), ('upfront', 'Upfront'), ('yearly', 'Yearly')], max_length=10)),
                ('investment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='billing.investment')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='billing.investor')),
            ],
        ),
        migrations.AddField(
            model_name='investment',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='billing.investor'),
        ),
        migrations.CreateModel(
            name='CashCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', models.CharField(max_length=34)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_status', models.CharField(choices=[('validated', 'Validated'), ('sent', 'Sent'), ('paid', 'Paid'), ('overdue', 'Overdue')], max_length=10)),
                ('bills', models.ManyToManyField(to='billing.bill')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_calls', to='billing.investor')),
            ],
        ),
    ]