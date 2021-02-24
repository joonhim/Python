def bintodec(bin):
    dec = 0
    bin = list(str(bin)) #convert binary to a list
    bin = bin[::-1]      #reverse the list
    power = 0   #declare power variable (for 1st elem == 0)
    for numb in bin:
        if numb == '1':
            dec += 2**power
        power += 1 #increase power by 1
    return dec
#enter >>> binary_string ='XXXX'
#enter >>> int(binary_string,2)