import random as rd 

def inflation(inflate, years, tot):
    tot = (inflate/100) * years
    #print ("total inflation amount is",tot,"given", years, "years")
    return tot

def converted_vals(org_money, moon, new_tot, currency):
    new_tot = org_money * moon 
    new_tot = org_money + new_tot
    new_tot = new_tot * currency 
    #print("We changed the original value from", org_money, "to", new_tot)
    return (new_tot)


def staircase_A(A, mi = 0, ma = 10, c = 0): 
    c = rd.randint(mi, ma)
    if c <= 5:
        A = A * 1.5
        #print(c, A)
        return A
    else:
        #print("No")
        return A 

        
def staircase_B(B):
    #p(getting money) = 1 
    B = B * 0.5
    #print("You chose B, the new value is", B)
    return (B)

def persons_choice (init_money,A,B,C,D,E, tot = 0):
    if A == 1:
        A = staircase_A(init_money) 
    elif A == 0:
        A = staircase_B(init_money)
    if B == 1:
        B = staircase_A(A)
    elif B == 0:
        B = staircase_B(A)
    if C == 1:
        C = staircase_A(B)
    elif C == 0:
        C = staircase_B(B)
    if D == 1:
        D = staircase_A(C)
    elif D == 0:
        D = staircase_B(C)
    if E == 1:
        E = staircase_A(D)
    elif E == 0:
        E = staircase_B(E)
    tot = E 
    return(tot) 



inflate = inflation(4.14, 5, 0)
print(inflate)

#AAAAA
initial= converted_vals(160, inflate, 0, 1.46)
print(initial)

initial1 = persons_choice(initial, 1, 1, 1, 1, 1)
initial2 = persons_choice(initial, 1, 1, 1, 0, 1)
initial3 = persons_choice(initial, 1, 1, 0, 1, 1)
initial4 = persons_choice(initial, 1, 1, 0, 0, 1)
initial5 = persons_choice(initial, 1, 0, 1, 1, 1)
initial6 = persons_choice(initial, 1, 0, 1, 0, 1)
initial7 = persons_choice(initial, 1, 0, 0, 1, 1)
initial8 = persons_choice(initial, 1, 0, 0, 0, 1)
initial9 = persons_choice(initial, 0, 1, 1, 1, 1)
initial10 = persons_choice(initial, 0, 1, 1, 0, 1)
initial11 = persons_choice(initial, 0, 1, 0, 1, 1)
initial12 = persons_choice(initial, 0, 1, 0, 0, 1)
initial13 = persons_choice(initial, 0, 0, 1, 1, 1)
initial14 = persons_choice(initial, 0, 0, 1, 0, 1)
initial15 = persons_choice(initial, 0, 0, 0, 1, 1)
initial16 = persons_choice(initial, 0, 0, 0, 0, 1)
initial17 = persons_choice(initial, 0, 1, 1, 1, 1)
initial18 = persons_choice(initial, 0, 1, 1, 0, 1)
initial19 = persons_choice(initial, 0, 1, 0, 1, 1)
initial20 = persons_choice(initial, 0, 1, 0, 0, 1)
initial21 = persons_choice(initial, 0, 1, 1, 1, 1)
initial22 = persons_choice(initial, 0, 1, 1, 0, 1)
initial23 = persons_choice(initial, 0, 1, 0, 1, 1)
initial24 = persons_choice(initial, 0, 1, 0, 0, 1)
initial25 = persons_choice(initial, 0, 0, 1, 1, 1)
initial26 = persons_choice(initial, 0, 0, 1, 0, 1)
initial27 = persons_choice(initial, 0, 0, 0, 1, 1)
initial28 = persons_choice(initial, 0, 0, 0, 0, 1)
initial29 = persons_choice(initial, 0, 1, 1, 1, 1)
initial30 = persons_choice(initial, 0, 1, 1, 0, 1)
initial31 = persons_choice(initial, 0, 1, 0, 1, 1)
initial32 = persons_choice(initial, 0, 1, 0, 0, 1)

print(initial1, initial32)
print("HAHAHA")