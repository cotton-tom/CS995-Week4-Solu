import Week4Problem
import unittest
from Week4Problem import Customer 
from Week4Problem import Purchase

class Test_Customer(unittest.TestCase):
    def test_amount_paid(self):
        customer = Customer('20','Thomas','Cotton')
        p1 = Purchase('20',65,100)
        p2 = Purchase('20',78,10)

        customer.purchase_list.append(p1)
        customer.purchase_list.append(p2)

        self.assertEqual(110,customer.customer_total())

if __name__ == "__main__":
    unittest.main()