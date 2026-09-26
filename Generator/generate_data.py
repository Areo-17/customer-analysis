from faker import Faker
import random
import numpy as np

class Generator:

    def __init__(self, my_seed: int):
        Faker.seed(my_seed)
        self.fake = Faker('es_MX')

    def user(self):
        user_info = {
            'user_id': None,
            'user_name': self.fake.name(),
            'user_age': random.randint(15, 90),
            'user_state': self.fake.administrative_unit(),
            'user_email': self.fake.email(domain = 'contoso.com')
        }
        
        return user_info

    def product(category: str, products: list[dict], existing_products: list[dict] = []):
        """ Takes a product category and inserts a list of dictionaries that contain the product's name with its respective brands.
        * products: List of dictionaries that contain the keys ```'name'(str)```, ```'price'(float)``` and ```'brands'(list)```. ```'brands'``` is a list of tuples that contain the name of the brand and a multiplier for the base price.
        ```
        products = [{
        'name': 'laptop',
        'price': 100,
        'brands': [('Great Brand', 1.5), ('New Brand', 1.1)]
        }]
        ```
        """
        #brands = ['ACME', 'AwesomeChoice', 'People Co.', 'The Vanguard', 'OnPoint', 'JustGreat']
        if existing_products == []:
            product_id = 1
        else:
            product_id = existing_products[-1]['product_id'] + 1
        final_products = []
        for product in products:
            for brand in product['brands']:
                product_info = {
                    'product_id': product_id,
                    'product_name': product['name'],
                    'product_brand': brand[0],
                    'product_price': product['price'] * brand[1],
                    'discount': False,
                    'discount_amount': 0,
                    'product_category': category
                }
                product_id += 1
                final_products.append(product_info)
                
        return final_products

    def create_offer(products: list[dict], existing_offers: list[dict] = [], init_date = None):
        if existing_offers == []:
            offer_id = 1
        else:
            offer_id = existing_offers[-1]['offer_id'] + 1
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
        if activity_records == []:
            event_id = 1
        else:
            event_id = activity_records[-1]['event_id'] + 1
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
        return activity_record

    def orders(event):
        pass

    def initialize():
        pass