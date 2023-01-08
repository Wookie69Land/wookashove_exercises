class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        if isinstance(price, (int, float)):
            self.price = price
        if isinstance(name, str):
            self.name = name
        self.products.append([self.price, self.name])

    def summary(self):
        return self.products

class Discount20PercentCart(Cart):

    def summary(self):
        products_no_discount = super().summary()
        for (p, n) in products_no_discount:
            self.products.append([0.8 * p, n])
        return self.products


class Above3ProductsCheapestFreeCart(Cart):

    def summary(self):
        if len(self.products) > 3:
            product_prices = []
            for i in self.products:
                product_prices.append(i[0])
            min_price = min(product_prices)
            for i in self.products:
                if i[0] == min_price:
                    i[0] = 0
                    return self.products


if __name__ == '__main__':
    c = Above3ProductsCheapestFreeCart()
    c.add(30, 'Piornik')
    c.add(30, 'Piornik')
    c.add(30, 'Piornik')
    c.add(10, 'Kredka')
    print(c.products)
    print(c.summary())