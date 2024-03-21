from django.test import TestCase
from.models import product

# Create your tests here.

class productTest(TestCase):
    def setUp(self):
        product.pm.create(product_name="Testproduct",product_description="product has been created for testing".product_Brand="TestBrand",product_price=500)
    
    def test_create_product(self):
        product.pm.get(product_name="Testproduct")
        self.assertEqual(product.id,self.product.id)

    def test_update_product(self):
        product.pm.get(product_name="Testproduct")
        product.product_price=5000
        product.save()

        self.assertNotEqual(product.product.price,self.product.product_price)

    def test_fetch_product(self):
        products=product.pm.all()
        count=len(products)
        self.assertGreater(count,0)
