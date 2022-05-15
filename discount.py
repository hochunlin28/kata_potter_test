class Discount_counter:
    

    def price(self, price):
        num_book = len(price)
        each_book_count = [0,0,0,0,0]
        total_discount = 0
        last_is_five = 0

        for i in range(num_book):
            each_book_count[price[i]] = each_book_count[price[i]] + 1

        if num_book == 0:
            return 0
        if num_book == 1:
            return 8

        zero_cnt = sum(i==0 for i in each_book_count)        
        while zero_cnt != 5 :

            if(zero_cnt == 4):
                total_discount = total_discount + 8 * 1
            elif(zero_cnt == 3):
                total_discount = total_discount + 8 * 0.95 * 2
            elif(zero_cnt == 2):
                if last_is_five == 1:
                    total_discount = total_discount - 8 * 0.75* 5 + 2 * (8 * 0.8* 4)
                else:
                    total_discount = total_discount + 8 * 0.9 * 3
            elif(zero_cnt == 1):
                total_discount = total_discount + 8 * 0.8* 4
            elif(zero_cnt == 0):
                total_discount = total_discount + 8 * 0.75* 5
                last_is_five = 1

            for i in range(5):
                if each_book_count[i] > 0:
                    each_book_count[i] = each_book_count[i] - 1

            zero_cnt = sum(i==0 for i in each_book_count)

        return total_discount