"""
Json practice
"""
import json
from dataclasses import dataclass
from typing import Optional, AnyStr

user_json = """{
  "name": "John",
  "age": 30,
  "married": true,
  "divorced": false,
  "children": ["Ann","Billy"],
  "pets": null,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
"""


@dataclass
class Car:
    model: str = None
    mpg: float = None


@dataclass
class User:
    name: str = None
    age: int = None
    married: bool = None
    divorced: bool = None
    children: list[str] = None
    pets: Optional[str] = None
    cars: list[Car] = None


from_json = json.loads(user_json)
car = [Car(**car) for car in from_json["cars"]]
user = User(name=from_json["name"],
            age=from_json["age"],
            married=from_json["married"],
            divorced=from_json["divorced"],
            children=from_json["children"],
            pets=from_json["pets"],
            cars=car)
print(user)

print("\n-------------- Product -------------------")
order = """
{
  "orderId": 12345,
  "customer": {
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "address": {
      "street": "123 Main St",
      "city": "Lahore",
      "zip": "54000"
    }
  },
  "items": [
    {
      "productId": 101,
      "name": "Laptop",
      "price": 1200.50,
      "quantity": 1
    },
     {
        "productId": 102, 
        "name": "Keyboard", 
        "price": 80.00, 
        "quantity": 1
    },
    {
      "productId": 103,
      "name": "Mouse",
      "price": 25.75,
      "quantity": 2
    }
  ],
  "payment": {
    "method": "Credit Card",
    "paid": true
  },
  "shipping": null
}

"""


@dataclass
class Address:
    street: str = None
    city: str = None
    zip: str = None


@dataclass
class Customer:
    id: int = None
    name: str = None
    email: str = None
    address: Address = None


@dataclass
class Items:
    productId: int = None
    name: str = None
    price: float = None
    quantity: int = None


@dataclass
class Payment:
    method: str = None
    paid: bool = None


@dataclass
class Shipping:
    address: str = None
    status: str = None


@dataclass
class Order:
    orderId: int
    customer: Customer
    items: list[Items]
    payment: Payment
    shipping: Shipping = None


order_json = json.loads(order)
print(order_json)
customer = Customer(id=order_json["customer"]["id"],
                    name=order_json["customer"]["name"],
                    email=order_json["customer"]["email"],
                    address=Address(**order_json["customer"]["address"]))

items = [Items(**i) for i in order_json["items"]]
payment = Payment(**order_json["payment"])
shipping = order_json.get("shipping", None)
if shipping:
    shipping = Shipping(**shipping)
else:
    shipping = None

order = Order(orderId=order_json["orderId"], customer=customer, items=items, payment=payment, shipping=shipping)
print(f"Json to model => {order}")
print("\n-------------- Filter items by price -------------------")
expensive_items = [item for item in order.items if item.price > 100]
print(f"Expensive items => {expensive_items}")

print("\n-------------- Filter items by quantity -------------------")
quantity = [item for item in order.items if item.quantity > 1]
print(quantity)

print("\n-------------- calculate total order amount -------------------")
price = sum(item.price * item.quantity for item in order.items)
print(price)

print("\n-------------- Find customer by city -------------------")
if order.customer.address.city == "Lahore":
    print(f"Customer from Lahore: {order.customer}")

print("\n-------------- Filter orders paid by credit card -------------------")
if order.payment.method == "Credit Card" and order.payment.paid :
    print("This order was paid with a Credit Card")

print("\n-------------- Most expensive product -------------------")
exp = max(order.items,key= lambda item:item.price)
print(exp)

print("\n-------------- Items where (price > 50) AND (quantity >= 2) -------------------")
items = [item for item in order.items if item.price > 50 and item.quantity >= 1]
print(f"Items with combine filter => {items}")

print("\n-------------- Group items by total cost per item  -------------------")
item_costs = {item.name: item.price * item.quantity for item in order.items}
print(item_costs)
