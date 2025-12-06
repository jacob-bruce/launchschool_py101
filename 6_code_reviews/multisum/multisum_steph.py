def multisum(x):
    result = 0
    nums = list(range(1, x))
    for y in nums:
        if y % 3 == 0:
            result += y
        elif y % 5 == 0:
            result += y
    return result

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

"""
Hi Stephanie,

Thanks for taking the time to submit your code for review. 

I've got good news and bad news for you. The bad news is that currently your code does not meet the problem requirements,
which were to return "True" for the following:

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

As it is, your code returns "False" for these.

The good news is that the fix is easy. What is happening now in your code is that it is not looping through all of the 
numbers it needs to loop through due to the arguments you've passed to the range object. The "Stop" number you put into
a range object is not inclusive, which just means that range (1, 20), for example, is going to give us numbers only through
19. The fix here is easy—we just add a "+ 1" to the "x" you currently have as the end point. 

The other interesting thing about range objects is that you can actually iterate over them directly. So there is no need to 
first convert your range into a list. Rather, you can jump right into the iterating with code like:

for num in range(1, x + 1):

Iterating directly over range communicates intent and avoids an unnecessary temporary variable.

We can also save some lines by consolidating your if statements. Right now you have two separate if statements:

        if y % 3 == 0:
            result += y
        elif y % 5 == 0:
            result += y

But these can be combined to a single line using an "or" operator:

        if y % 3 == 0 or y % 5 == 0:
            result += y

This makes the code more succinct and easaier to read.

Overall the code was readable and easy to understand. One small tweak you could consider is using more descriptive variable
names. For instance, instead of "x" and "y" you could use names like "max_value" and "number." Small changes like this will 
make it easier for your future self and others to interpret your code.

While not strictly necessary for a problem like this, it could be useful practice to separate out discrete operations into 
helper functions. For example in this problem we could separate out the task of looking for multiples of 3 and 5 using a 
helper function like this:

def is_multiple(number, divisor):
    return number % divisor == 0

Then in your code you would use something like this to pass it to the helper function:

for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number

Getting into this habit early on in your coding journey will be beneficial in the long term.

Overall great job!

"""