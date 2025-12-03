
def lhuns_algo(no):
    # Lhun's algorithm checks if a credit card number is valid
    
    # just in case the user provides the number as an integer, we need it to be a string
    if isinstance(no,int):
        no = str(no)

    # the card number is now a list with each digit at a specific index position
    card_no = list(no)
    odd_sum = 0
    even_sum = 0
    double_list = []
    # use enumerate to keep the index values
    for (idx, val) in enumerate(card_no):
        # first we take the numbers with odd indexes and sum those numbers
        if idx % 2 != 0:
            odd_sum += int(val)
        # then we take the numbers with even indexes and multiply them by 2 and append them to a seperate list
        else:
            double_list.append(int(val) * 2)

    # the next step in the algorithm is if a number in the doubles list is 2 digit, we sum the two digits. Otherwise, we keep the single digit
     # converting list into string
    double_string = ""
    for x in double_list:
        double_string += str(x)
    
    # converting string back to list so they are split up
    double_list = list(double_string)

    # now we add the numbers with even integers
    for x in double_list:
        even_sum += int(x)
    
    # finally add the odd sum and even sum 
    net_sum = odd_sum + even_sum

    # we want to check if the remainder is 0, that means the credit card number is valid
    if net_sum % 10 == 0:
        print('Valid card number')
    else:
        print('Invalid card number')


    
lhuns_algo(5610591081018250)

    