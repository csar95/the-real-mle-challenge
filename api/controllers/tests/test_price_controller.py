import pytest
from api.controllers.price_controller import calculate_price


@pytest.mark.parametrize("body",
                         [({"id": 1001,"accommodates": 4,"room_type": "Entire home/apt","beds": 2,"bedrooms": 1,"bathrooms": 2,"neighbourhood": "Brooklyn","tv": 1,"elevator": 1,"internet": 0,"latitude": 40.71383,"longitude": -73.9658}),
                          ({"id": 1001,"accommodates": 2,"room_type": "Private room","beds": 1,"bedrooms": 1,"bathrooms": 1,"neighbourhood": "Brooklyn","tv": 1,"elevator": 0,"internet": 1,"latitude": 40.72780,"longitude": -73.94797})])
def test_calculate_price(body):
    response = calculate_price(body)
    assert response['id']==body['id'] and response['price_category'] in ['Low','Mid','High','Luxury']
