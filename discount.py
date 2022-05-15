class Discount_counter:

    def price(self, price):
        num_book = len(price)
        each_book_count = [0,0,0,0,0]

        if num_book == 0:
            return 0
        if num_book == 1:
            return 8

        tmp = sum(i==0 for i in price)
        if(tmp == 4):
            return 8 * num_book
