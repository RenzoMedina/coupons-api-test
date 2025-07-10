def applyCoupon(price, coupon):
    discounts ={
        "SALES10":0.10,
        "SUPER20": 0.20,
        "WELCOME": 0.15
    }
    if coupon in discounts:
        return round(price * (1 - discounts[coupon]),2)
    return price

def getFinalPrice(basePrice, coupon, taxRate=0.19):
    desPrice = applyCoupon(basePrice, coupon)
    return round(desPrice * (1 + taxRate), 2 )