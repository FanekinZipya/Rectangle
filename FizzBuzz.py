def fizz_buzz(self,n):
    self.number=n

n=int(input('Number: '))

if (n%3==0):
    print('Fizz')
if (n%5==0):
    print('Buzz')
if ((n%3==0) & (n%5==0)):
    print('FizzBuzz')
