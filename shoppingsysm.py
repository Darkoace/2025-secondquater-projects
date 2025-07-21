def change(total):
    quaterdollar = 25
    dollar = 10
    nickle = 5
    dime = 1

    coins = 0

    quaterdollars = 0
    dollars = 0
    dimes = 0
    nickles = 0

    m=float(total)

    if m < 0 :
        breakpoint
    else :

        while m > quaterdollar :
            m = m - quaterdollar 
            quaterdollars = quaterdollars +  1
            
        if m == quaterdollar:
            m = m - quaterdollar
            quaterdollars = quaterdollars + 1

        print(f"quaterdollar:{quaterdollars}")
        
        
        while m > dollar :
            m = m - dollar 
            dollars = dollars +  1
        if m == dollar:
            m = m - dollar
            dollars = dollars + 1
        print(f"dollars:{dollars}")

        while m > nickle :
            m = m - nickle
            nickles = nickles +  1
        if m == nickle:
            m = m - nickle
            nickles = nickles + 1
        print(f"nickle:{nickles}")
        
        while m > dime :
            m = m - dime 
            dimes = dimes +  1
        if m == dime:
            m = m - dime
            dimes = dimes + 1
        print(f"dime:{dimes}")

    coins = quaterdollars + dollars + dimes + nickles
    print(f"Total coins:{coins}")







