import random
from datetime import datetime, timedelta
from django.utils import timezone
from test_app.models import Customer, Merchant, Product, Order, OrderItem
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add sample data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--num_orders",
            type=int,
            default=100,
            help="Total number of sample orders to be created. Default (100)",
        )

    def handle(self, *args, **options):
        # Access the command line arguments
        num_orders = options["num_orders"]

        customers = [
            Customer.objects.create(name=f"Customer_{i}") for i in range(1, 11)
        ]
        products = [
            Product.objects.create(name=f"Product_{i}", price=random.uniform(10, 100))
            for i in range(1, 21)
        ]
        merchants = [Merchant.objects.create(name=f"Merchant_{i}") for i in range(1, 6)]

        for _ in range(num_orders):
            customer = random.choice(customers)
            merchant = random.choice(merchants)
            order_date = timezone.now() - timedelta(days=random.randint(1, 30))

            try:
                order = Order.objects.create(
                    customer=customer, merchant=merchant, order_date=order_date
                )
                num_order_items = random.randint(1, 5)
                selected_products = random.sample(products, num_order_items)

                for product in selected_products:
                    quantity = random.randint(1, 5)
                    OrderItem.objects.create(
                        order=order, product=product, quantity=quantity
                    )
            except IntegrityError:
                # Handle integrity errors if they occur
                pass

        self.stdout.write(self.style.SUCCESS(f"Sample data created"))
