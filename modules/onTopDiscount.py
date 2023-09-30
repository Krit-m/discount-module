class onTopDiscount:
    def __init__(self, itemList, onTop):
        self.itemList = itemList
        self.onTop = onTop
        self.percent = 0
        self.point = 0

    def apply(self):
        total = 0
        for item in self.itemList:
            total = total + item["price"]

        if self.onTop["type"] == "byItem":
            self.percent = self.onTop["amount"] / 100
            price_factor = 1 - self.percent
            for item in self.itemList:
                if item["category"] == self.onTop["item"]:
                    item["price"] = item["price"] * price_factor

        else:  # by points
            limit = round(total / 5)
            self.point = self.onTop["amount"]
            if self.point > limit:
                self.point = limit
            self.percent = self.point / total
            price_factor = 1 - self.percent
            for item in self.itemList:
                item["price"] = item["price"] * price_factor

        return self.itemList
