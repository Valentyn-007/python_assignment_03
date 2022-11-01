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
    product_name = 'Dettol'
    product_id = 2566993


class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int):
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
        print(f"Product Name: Dettol")

    def edit_product(self):
        print("Try to edit this product")

    def get_product_by_id(self, product_id):
        print("Product id: 56555")

    def get_all_products(self):
        print("List all products")

    def upload_product_image(self):
        print("Insert Image here")

    def delete_product(self):
        print("Delete product")


productmanager = ProductManager()
productmanager.create_product("Dettol")
productmanager.edit_product()
productmanager.get_product_by_id(product_id=56555)
productmanager.get_all_products()
productmanager.upload_product_image()
productmanager.delete_product()
