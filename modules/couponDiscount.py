class couponDiscount:
    def __init__(self, itemList, coupon):
        self.itemList = itemList
        self.coupon = coupon
        self.percent = 0

    def apply(self):
        total = 0
        for item in self.itemList:
            total = total + item["price"]

        if self.coupon["type"] == "fixed":
            self.percent = self.coupon["amount"] / total
            if self.percent > 1:
                self.percent = 1
        else:  # percent discount
            self.percent = self.coupon["amount"] / 100

        price_factor = 1 - self.percent

        for item in self.itemList:
            item["price"] = item["price"] * price_factor

        return self.itemList
