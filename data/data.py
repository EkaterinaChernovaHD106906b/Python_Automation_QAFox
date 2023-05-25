from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    e_mail: str = None
    tel: str = None
    address: str = None
    city: str = None
    post_code: str = None
    password: str = None



