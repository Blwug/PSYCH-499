def inflation(inflate, years, tot):
    tot = (inflate/100) * years
    print ("total inflation amount is",tot,"given", years, "years")
    return tot

def converted_vals(org_money, moon, new_tot, currency):
    new_tot = org_money * moon 
    new_tot = org_money + new_tot
    new_tot = new_tot * currency 
    print("We changed the original value from", org_money, "to", new_tot)
    return (new_tot)
    

inflate = inflation(4.14, 5, 0)
a_1 = converted_vals(150, inflate, 0, 1.46)
