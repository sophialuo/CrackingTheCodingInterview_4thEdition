#8.7
#Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and 
#pennies (1 cent), write code to calculate the number of ways representing n cents
def n_cents(num):
    if num == 0:
        return 0
    coin = 25
    if coin > num:
        coin = 10
    if coin > num:
        coin = 5
    if coin > num:
        coin = 1
        
    return n_cent_helper(0, coin, num) 
    
def n_cent_helper(current, coin, num):
    if current > num:
        return 0
    if current == num:
        return 1
        
    if coin == 25:
        return n_cent_helper(25+current, 25, num) + \
        n_cent_helper(10+current, 10, num) + \
        n_cent_helper(5+current, 5, num) + \
        n_cent_helper(1+current,1,num)
    elif coin == 10:
        return n_cent_helper(10+current, 10, num) + \
        n_cent_helper(5+current, 5, num) + \
        n_cent_helper(1+current,1,num)
    elif coin == 5:
        return n_cent_helper(5+current, 5, num) + \
        n_cent_helper(1+current,1,num)
    else:
        return n_cent_helper(1+current, 1, num)

#dynamic programming version
def n_cents_dp(num):
    coins = [25, 10, 5, 1]
    return n_cents_dp_helper(coins, len(coins), num)

def n_cents_dp_helper(coins, coin_types, num):
    if num == 0: 
        return 1
    if num < 0:
        return 0
    if coin_types <= 0 and num >= 1: 
        return 0
    #exclude the coin S[coin_types-1] or include the coin S[coin_types-1]
    return n_cents_dp_helper(coins, coin_types-1, num) + \
    n_cents_dp_helper(coins, coin_types, num-coins[coin_types-1])
    

