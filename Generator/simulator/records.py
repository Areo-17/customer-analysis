from datetime import datetime
import numpy as np
from faker import Faker
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import Customer, Product, Seller, Promotion, create_records

class Generator:

    def __init__(self, rng: int):
        self.rng = np.random.default_rng(rng)
        Faker.seed(rng)
        self.fake = Faker('es_MX')

    def customer(self, last_id, signup_ts):
        customer_id = last_id + 1
        return Customer(
            customer_id= customer_id,
            customer_name= self.fake.name(),
            customer_birthday= self.fake.date_between(),
            customer_email= self.fake.email(domain='contoso.com'),
            customer_state=self.fake.administrative_unit(),
            signup_ts= signup_ts
        )

    def product(self, last_id):
        product_id = last_id + 1
        return Product(
            product_id= product_id,
            product_name= None,
            product_price= None,
            product_category= None
        )

    def seller(self, last_id):
        seller_id = last_id + 1
        return Seller(
            seller_id = seller_id,
            seller_name = self.fake.company(),
            seller_commission_rate= self.rng.choice([1,2,3,4,5]) / 10,
            seller_state= self.fake.administrative_unit(),
            seller_rating=None
        )

    def promotion():
        pass

    def write_parquet(self, records: list, table_name: str):
        df = pd.DataFrame(records)
        try:
            parquet_table = pa.Table.from_pandas(df)
            file = pq.write_table(parquet_table, f'../catalog/{table_name}.parquet')
        except:
            "File could not be created."
        return file

    #implement a function generator using yield, which takes a list of records and returns a parquet file from that list.

    def intitialize(self, customers_num: int, sellers_num: int):
        signup_ts = datetime(2024, 1, 1)
        customers = create_records(self.customer, customers_num, signup_ts)
        sellers = create_records(self.seller, sellers_num)
        try:
            self.write_parquet(customers, 'Customers')
            self.write_parquet(sellers, 'Sellers')
            return print("All files saved successfully.")
        except:
            return print("Files could not be saved.")


if __name__ == '__main__':

    gen = Generator(5)
    gen.intitialize(100, 20)
    print(gen)