import random
print('wlocome to the magic eight ball! enter to start!')
q = input('what would you like to ask?')
answer = random.randint(1,4)
if answer == 1:
    print('the answer is yes.')
elif answer == 2:
    print('the answer is no.')
elif answer == 3:
    print('cannot predict now')
else:
    print('ask again later')