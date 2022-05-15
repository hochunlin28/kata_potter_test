class Discount_counter:

    def price(self, price):
        num_book = len(price)
        each_book_count = [0,0,0,0,0]
        for i in range(num_book):
            each_book_count[price[i]] = each_book_count[price[i]] + 1

        if num_book == 0:
            return 0
        if num_book == 1:
            return 8

        tmp = sum(i==0 for i in each_book_count)

        if(tmp == 4):
            return 8 * num_book
