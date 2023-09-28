import json
from modules.campaignValidity import campaignValidity

f = open('shoppingList.json')
data = json.load(f)
total = 0

for item in data["cart"]:
    total = total + item["price"]

print(total)
discount_check = campaignValidity(data)
response = discount_check.valid()
print(response)

if discount_check.validity:
    itemList = data["cart"]
    discountList = data["campaigns"]

    while discount_check.coupon + discount_check.onTop + discount_check.seasonal > 0:
        for discount in discountList:
            if discount["category"] == "coupon":
                discount["category"] = "used"
                print(discount["type"] + " is used.")
                discount_check.use_coupon()
            if discount["category"] == "onTop" and discount_check.coupon == 0:
                discount["category"] = "used"
                print(discount["type"] + " is used.")
                discount_check.use_on_top()
            if discount["category"] == "seasonal" and discount_check.coupon == 0 and discount_check.onTop == 0:
                discount["category"] = "used"
                print(discount["type"] + " is used.")
                discount_check.use_seasonal()
