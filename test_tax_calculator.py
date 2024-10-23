#The test that asserts no tax is applied if earnings are less than 12,000. It'll give an error since the calculate_tax function doesn’t exist yet.
def test_no_tax_below_12000():
     from tax_calculator import calculate_tax
     assert calculate_tax(11000) == 0
     
def test_20_percent_tax_between_12000_and_36000():
    from tax_calculator import calculate_tax
    assert calculate_tax(20000) == (20000 - 12000) * 0.20
#The above test fails because the calculate_tax function for earnings in that range don't exist yet.

def test_40_percent_tax_above_36000():
    from tax_calculator import calculate_tax
    assert calculate_tax(40000) == (36000 - 12000) * 0.20 + (40000 - 36000) * 0.40
#The above test  first fails because the calculate_tax function for earnings in that range don't exist yet.