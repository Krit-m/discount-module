import json


class campaignValidity:
    def __init__(self, shoppingList):
        self.list = shoppingList
        self.validity = False
        self.coupon = 0
        self.onTop = 0
        self.seasonal = 0
        self.proList = []

        f = open('currentPromotion.json')
        data = json.load(f)

        for promotion in data["available"]:
            self.proList.append(promotion["name"])

    def valid(self):
        # coupon = 0
        # onTop = 0
        # seasonal = 0

        response = "Sorry, "

        for discount in self.list["campaigns"]:

            if "name" in discount and discount["name"] in self.proList:
                cat = discount["category"]
                campaign = discount["type"]

                if cat == "coupon":
                    if ((campaign == "fixed" and "amount" in discount and type(discount["amount"]) is int and discount[
                        "amount"] > 0) or
                            (campaign == "percent" and "amount" in discount and type(discount["amount"]) is int and 0 <
                             discount["amount"] < 100)):
                        self.coupon = self.coupon + 1
                    else:
                        discount["category"] = "Invalid"

                elif cat == "onTop":
                    if (campaign == "byItem" and "item" in discount and discount["item"] in ["clothing", "accessories",
                                                                                             "electronics"]
                            and "amount" in discount and type(discount["amount"]) is int and 0 < discount[
                                "amount"] < 100):

                        match = False
                        for item in self.list["cart"]:
                            if item["category"] == discount["item"]:
                                match = True
                        if match:
                            self.onTop = self.onTop + 1
                        else:
                            discount["category"] = "Invalid"

                    elif campaign == "byPoints" and "amount" in discount and type(discount["amount"]) is int and \
                            discount["amount"] > 0:
                        self.onTop = self.onTop + 1
                    else:
                        discount["category"] = "Invalid"

                elif cat == "seasonal" and campaign == "special":
                    if "forEvery" in discount and type(discount["forEvery"]) is int and "discount" in discount and type(
                            discount["discount"]) is int and discount["discount"] < discount["forEvery"]:
                        self.seasonal = self.seasonal + 1
                    else:
                        discount["category"] = "Invalid"
            else:
                discount["category"] = "Invalid"

        if self.coupon == 0 and self.onTop == 0 and self.seasonal == 0:
            response = response + "no valid discount campaigns selected"

        elif self.coupon >= 2 or self.onTop >= 2 or self.seasonal >= 2:
            response = response + "you can use only one discount campaign per category"

        else:
            response = str(self.coupon + self.onTop + self.seasonal) + " valid discounts."
            self.validity = True

        return response

    def use_coupon(self):
        self.coupon = 0

    def use_on_top(self):
        self.onTop = 0

    def use_seasonal(self):
        self.seasonal = 0
