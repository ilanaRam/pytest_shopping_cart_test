
# https://docs.pytest.org/en/stable/

# the name of test file name must start with 'test_': test_shopping_cart.py
# test func must start with 'test_': def test_can_add_item_to_cart()
from shopping_cart import ShoppingCart
import pytest
from item_db import Item_DB
from unittest.mock import Mock


# fixture will be called each test 
# this fixture creates new cart, per test
@pytest.fixture
def cart2(): 
    return ShoppingCart(2)

@pytest.fixture
def cart1(): 
    return ShoppingCart(1)



def test_can_add_item_to_cart(cart1):
    exit()
    # cart = ShoppingCart(1)
    cart1.add('apple')
    assert cart1.size() == 1 # assert if not correct !!

def test_cart_contains_item_previously_added(cart1):
    # cart = ShoppingCart(1)
    exit()
    cart1.add('apple')
    assert 'apple' in cart1.get_items()

"""
    Test adds more items to cart than expected to see that assert is caused !!
    When assert caused - test passes
    Test should fail if assert isnt happenning 
    
    negative logic - test passes if function it tests failes - because it is what we expect - we expect to fail !!

    with comes to assert that something has happend 
    להצהיר על כך שמשהו קרה !!

    with pytest.raises(OverflowError) - means:
        what ever runs within 'with' - I expect to through OverflowError error 
        and if it throughs OverflowError error - the test passes @@
        If it does not though OverflowError (or it throughs different error) - the test fails ##
"""
def test_add_more_than_max_amount_of_items_to_cart(cart2):
    # cart = ShoppingCart(2)
    # I first add maximum amount of items
    exit()
    for _ in range(2):
        cart2.add('apple')
    # then I expect for exception on one more item added !!
    with pytest.raises(OverflowError):
        cart2.add('apple')

def test_get_total_price(cart2):
    print("Test to check total price of all items in cart")
    # cart = ShoppingCart(2)
    cart2.add('apple')
    cart2.add('orange')
   
    # way1: create the price_map 

    # price_map = {'apple': 1.0,
    #              'orange': 2.0
    #             }
    #assert cart2.get_total_price(price_map) == 3

    # way2: I created a class to moke th price_map db
    item_db = Item_DB()
    # item_db.get = Mock(return_value = 1.0)     # now .get will return only 1.0 (each time we call it and we call it per item in cart)    
    # assert cart2.get_total_price(item_db) == 3 # we will fail, we added 2 items (per item get will return 1, 1+1 = 2 whicj !-3) 
    
    # we need that each item will have different prices
    # for this we need to work with mock_side_effect, lets create it
    
    # inner function knows about all outer function variables and can access them 
    def mock_get_item(item: str):
        if item == 'apple': 
            return 1.0
        elif item == 'orange':
            return 2.0
        elif item == 'lemon': 
            return 3.0
    
    item_db.get = Mock(side_effect= mock_get_item)   

    assert cart2.get_total_price(item_db) == 3

    
                      

    
        
        
        
   


    