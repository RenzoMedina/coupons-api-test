from app.coupons import applyCoupon, getFinalPrice

def test_discount_sales10():
    assert applyCoupon(100, "SALES10") == 90.0

def test_discount_super20():
    assert applyCoupon(200, "SUPER20") == 160.0

def test_discount_welcome():
    assert applyCoupon(100, "WELCOME") == 85.0

def test_final_price_with_tax_rate():
    assert getFinalPrice(100, "SALES10") == 107.1

def test_invalid_coupon():
    assert applyCoupon(990, "NOT-FOUND") == 990