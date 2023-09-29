class seasonalDiscount:
    def __init__(self, itemList, seasonal):
        self.itemList = itemList
        self.seasonal = seasonal
        self.percent = 0

    def apply(self):
        total = 0
        for item in self.itemList:
            total = total + item["price"]

        times = total // self.seasonal["forEvery"]
        discount = times * self.seasonal["discount"]
        self.percent = discount / total
        price_factor = 1-self.percent

        for item in self.itemList:
            item["price"] = item["price"] * price_factor

        return self.itemList
