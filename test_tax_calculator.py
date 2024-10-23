#The test that asserts no tax is applied if earnings are less than 12,000. It'll give an error since the calculate_tax function doesn’t exist yet.
def test_no_tax_below_12000():
     from tax_calculator import calculate_tax
     assert calculate_tax(11000) == 0
