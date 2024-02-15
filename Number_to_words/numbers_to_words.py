# Define lists for one-digit, teens, tens, and thousands
ONES = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
TEENS = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
THOUSANDS = ['', 'Thousand', 'Million', 'Billion']

def convert_group_to_words(group):
    # Extract hundreds, tens, and ones from the three-digit group
    hundred, ten, one = map(int, list(str(group).zfill(3)))
    
    words = ''
    
    # Convert hundreds place to words
    if hundred > 0:
        words += ONES[hundred] + ' Hundred '
    
    # Convert tens and ones places to words
    if ten == 1:
        words += TEENS[one] + ' '
    else:
        words += TENS[ten] + ' ' + ONES[one] + ' '
    
    return words.strip()

def convert_to_words(number):
    # Handle the case when the input number is 0
    if number == 0:
        return 'Zero'
    
    result = ''
    group_index = 0

    # Process the number in groups of three digits
    while number > 0:
        group = number % 1000
        if group != 0:
            # Convert the three-digit group to words and append the appropriate suffix
            result = convert_group_to_words(group) + ' ' + THOUSANDS[group_index] + ' ' + result
        group_index += 1
        number //= 1000

    return result.strip()

if __name__ == '__main__':
    # Take user input for a number and print the corresponding words
    number = int(input('Enter any number: '))
    print(f'{number} in words is: {convert_to_words(number)}')
