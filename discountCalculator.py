import json
from modules.campaignValidity import campaignValidity
from modules.couponDiscount import couponDiscount
from modules.onTopDiscount import onTopDiscount
from modules.seasonalDiscount import seasonalDiscount

f = open('shoppingList.json')
data = json.load(f)
# total = 0
#
# for item in data["cart"]:
#     total = total + item["price"]
#
# print(total)
discount_check = campaignValidity(data)
response = discount_check.valid()
print(response)

if discount_check.validity:
    itemList = data["cart"]
    discountList = data["campaigns"]
    zero = False

    while discount_check.coupon + discount_check.onTop + discount_check.seasonal > 0 and not zero:
        for discount in discountList:
            # coupon
            free = ""
            if discount["category"] == "coupon":
                coupon = couponDiscount(itemList, discount)
                itemList = coupon.apply()
                discount["category"] = "used"
                if coupon.percent == 1:
                    zero = True
                    free = " The total price is covered."
                print(discount["name"] + " (" + discount["type"] + ") is used."+free)
                discount_check.use_coupon()

            # on top
            if discount["category"] == "onTop" and discount_check.coupon == 0:
                onTop = onTopDiscount(itemList, discount)
                itemList = onTop.apply()
                discount["category"] = "used"
                if discount["type"] == "byPoints":
                    point = ", with " + str(int(onTop.point)) + " points,"
                    promo_item = ""
                else:
                    point = ""
                    promo_item = ", " + discount["item"]
                print(discount["name"] + " (" + discount["type"] + promo_item + ")" + point + " is used.")
                discount_check.use_on_top()

            # seasonal
            if discount["category"] == "seasonal" and discount_check.coupon == 0 and discount_check.onTop == 0:
                seasonal = seasonalDiscount(itemList, discount)
                itemList = seasonal.apply()
                discount["category"] = "used"
                print(discount["name"] + " (" + discount["type"] + ") is used.")
                discount_check.use_seasonal()

    total = 0
    for item in itemList:
        total = total + item["price"]

    print("\nTotal price: " + str(round(total, 2)) + " Baht")
