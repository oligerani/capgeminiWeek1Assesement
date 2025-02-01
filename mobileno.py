mobile_no=input("enter your mobile no")
digit_to_word = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
}
for i in mobile_no:
    print(digit_to_word[i],end=" ")
    
    