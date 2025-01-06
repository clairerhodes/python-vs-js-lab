# Convert the following to Python from JavaScript


# ================================ Problem 1 ================================
# Write a method that accepts a name from the user and then returns it:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

def getName():
    user_input = input("what is your name?")
    print("Hello, " + user_input + "!")

getName()









# ================================ Problem 2 ================================
# Write a method that reverses a string:

# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverseIt():
    string = "a man, a plan, a canal, fremeies!"
    reverse = ""
    for i in range(len(string)):
        reverse += string[len(string) - (i + 1)]
    print(reverse)
reverseIt()









# ================================ Problem 3 ================================
# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swapEm():
    a = 10
    b = 30
    temp = b
    b = a
    a = temp
    
    print("a is now " + str(a) + ", and b is now " + str(b) )
swapEm()










# ================================ Problem 4 ================================
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#    // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

def multipleArray(ary):
    if len(ary) == 0:
        print(1)
    else:
        total = 1
        for num in ary:
            # total = total * num
            total *= num
        print(total)
multipleArray([11, 22, 33])










# ================================ Problem 5 ================================
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
    if x%(3*5) == 0:
        print('fizzbuzz')
    elif x%3 == 0:
        print('fizz')
    elif x%5 == 0:
        print('buzz')
    else:
        print('archer')

fizzbuzzer(30)









# ================================ Problem 6 ================================
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nthFib():
    fibs = [1, 1]
    num = input("which fibonacci number do you want?")

    while (len(fibs) < int(num)):
        length = len(fibs)
        nextFib = fibs[-2] + fibs[-1]
        fibs.append(nextFib)
    
    print("{fibs[-1]} is the fibonacci number at position" + num)
    # print("{fibs[-1]} is the fibonacci number at position {num}")
nthFib()











# ================================ Problem 7 ================================
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def searchArray(array, value):
    for item in array:
        if item == value:
            return True
    return -1
searchArray([22, 11, 44, 88], 11)










# ================================ Problem 8 ================================
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def isPalindrome(str):
    for i in range(len(str) / 2):
        if str(i) != str[len(str) - i - 1]:
            return False
    return True
isPalindrome("pookianna") 










# ================================ Problem 9 ================================
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def hasDupes(arr):
    obj = {}
    for i in arr:
        if i in obj:
            return True
        else:
            obj[i] = True
    return False
hasDupes([1, 4, 11, 22, 4, 420, 69])
















