from faker import Faker
from utils import offers
import random
import numpy as np
from datetime import timedelta

class Generator:

    def __init__(self, my_seed: int):
        Faker.seed(my_seed)
        self.fake = Faker('es_MX')

    def user(self, existing_users: list = []):
        user_id = offers.get_id(existing_users, 'user_id')
        user_info = {
            'user_id': user_id,
            'user_name': self.fake.name(),
            'user_age': random.randint(15, 90),
            'user_state': self.fake.administrative_unit(),
            'user_email': self.fake.email(domain = 'contoso.com')
        }
        
        return user_info

    def brands(self, existing_brands = []):
        brand_id = offers.get_id(existing_brands, 'brand_id')
        brand_info = {
            'brand_id': brand_id,
            'brand_name': self.fake.company(),
            'brand_state': self.fake.administrative_unit(),
            'brand_multiplier': 1 + round(random.random(), 1)}
        return brand_info

    def product(products: dict[str], existing_products: list[dict] = [], new_brands = []):
        """ Takes a product category and inserts a list of dictionaries that contain the product's name with its respective brands.
        * products: Dictionary that contains categories as keys and another dictionary as a value, with the products.
        ```
        products = {
        "technology": {
            "products": [
                    {
                    "name": "laptop",
                    "price": 150.50
                    },
                    {
                    "name": "laptop",
                    "price": 150.50
                    }
                ],
            }
        }
        ```
        """
        categories = list(products.keys())
        for category in categories:
            products[category]['brands'] = []
        for brand_item in new_brands:
            category_name = random.choice(categories)
            products[category_name]['brands'].append(brand_item)
        # Change to another approach. Change products parameter to a pre-built dict that includes categories as keys and the list of products as value. Get the new brands previously generated, select randomly one and get that brand out of the list with pop. Assign the poped brand to a random category.
        product_id = offers.get_id(existing_products, 'product_id')
        final_products = []
        for category in categories:
            for product in products[category]['products']:
                product_info = {
                    'product_id': product_id,
                    'product_name': product['name'],
                    'discount': False,
                    'discount_amount': 0,
                    'product_category': category
                }
                if products[category]['brands'] == []:
                    product_info['product_brand_id'] = ''
                    product_info['product_price'] = product['price']
                else:
                    for brand in products[category]['brands']:
                        product_info['product_brand_id'] = brand['brand_id']
                        product_info['product_price'] = product['price'] * brand['brand_multiplier']
        product_id += 1
        final_products.append(product_info)
                
        return final_products

    def create_offer(products: list[dict], existing_offers: list[dict] = [], init_date = None):
        offer_id = offers.get_id(existing_offers, 'offer_id')
        final_offers = []
        for product in products:
            offer = {
                'offer_id': offer_id,
                'product_id': product['product_id'],
                'price': product['product_price'],
                'publication_date': init_date
            }
            final_offers.append(offer)
        return final_offers

    def customer_activity(user_record: dict, offers_records: list, logged_in_date = None, activity_records: list[dict] = []):
        event_id = offers.get_id(activity_records, 'event_id')
        activity_record = {
            'event_id': event_id,
            'customer_id': user_record['user_id'],
            'logged_in_date': logged_in_date,
            'offer_id': '',
            'quantity': '',
            'grand_total': None,
            'transaction_date': None,
            'logged_out_date': ''
        }
        event = random.choice(['VIEW', 'ADD_TO_CART', 'BUY'])
        if event in ['ADD_TO_CART', 'BUY']:
            offer = random.choice(offers_records)
            quantity = np.random.choice(a=[1, 2, 3, 4, 5], p=[0.65, 0.15, 0.1, 0.05, 0.05])
            activity_record['offer_id'] = offer['offer_id']
            activity_record['quantity'] = quantity
            pay = random.choice([True, False])
            if pay:
                activity_record['transaction_date'] = logged_in_date
        if activity_record['transaction_date'] == None:
            activity_record['quantity'] = None
        activity_record['logged_out_date'] = timedelta(logged_in_date) + timedelta(minutes = random.choice(10))
        return activity_record

    def orders(order_records = [], activity_records = []):
        order_id = offers.get_id(order_records, 'order_id')
        orders = []
        for event in activity_records:
            if event['transaction_date'] != None:
                order_info = {
                    'order_id': order_id,
                    'order_date': event['transaction_date'],
                    'delivery_date': event['transaction_date'] + timedelta(minutes=random.choice(5))
                }
                orders.append(order_info)
        return orders

    def initialize():
        pass