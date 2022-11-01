# Assignment
# # 1. Implement an abstract class called ProductAbstract to have the following method:
# create_product
# edit_product
# get_product_by_id
# get_all_products
# upload_product_image
# delete_product
# NB: Note to define parameters as needed

# 2. Implement a class called ProductManager to implement ProductAbstract. Do note to add implementation for all the abstract methods of the ProductAbtract class
#

# ------------Solution----------------->
from abc import ABC, abstractmethod


class Product:
    product_name = ''
    product_id = ''


class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: str):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass


class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print("User Information")

    def edit_product(self):
        print("")

    def get_product_by_id(self, product_ id):
        print("Hello world")

    def get_all_products(self):
        print("Hello, dark planet")

    def upload_product_image(self):
        print("")

    def delete_product(self):
        print("")


productmanager = ProductManager()
productmanager.get_all_products()
