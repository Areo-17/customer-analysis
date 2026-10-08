from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    customer_id: int
    customer_name: str
    customer_email: str
    customer_birthday: datetime
    customer_state: str
    signup_ts: datetime

@dataclass
class Product:
    product_id: int
    product_name: str
    product_price: float
    product_category: str

@dataclass
class Seller:
    seller_id: int
    seller_name: str
    seller_state: str
    seller_commission_rate: float
    seller_rating: float

@dataclass
class Promotion:
    promo_id: int
    promo_name: str
    promo_start_ts: datetime
    promo_end_ts: datetime
    promo_discount_pct: int
    promo_scope: str