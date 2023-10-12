

def test_init(phone1):
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
