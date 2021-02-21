import random
name= 'Jakub'
question= 'will i win the lottery?'
answer = ""
###part 2
random_number= random.randint(1, 9) 
print(random_number)

### implementing control flow

if random_number==1:
  answer = 'yes definetly.'
elif random_number == 2:
    answer= 'it is decidedly so.'
elif random_number==3:
      answer= 'Without a doubt.'
elif random_number==4:
      answer= 'Reply hazy, try again.'
elif random_number==5:
      answer= 'try again later.'
elif random_number==6:
        answer= 'better not tell you now.'
elif random_number==7:
          answer='my scources say no.'
elif random_number==8:
            answer:' outlook not so good.'
elif random_number==9:
              answer= 'very doubtful.'
else:
      answer= 'Eroor'


print(name + ' asks: ' + question)
print('Magic 8-Balls answer' + answer)

if name=='':
  print('Question'+question) 

  if question=='':
    print('asks' )


