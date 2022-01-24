from logpy import *
from logpy.core import lall

people = var()
rules = lall(
    # There are 4 people
    (eq, (var(), var(), var(), var()), people),
    # Steve's car is blue
    (membero, ('Steve', var(), 'blue', var()), people),
    # Person who has a cat lives in Canada
    (membero, (var(), 'cat', var(), 'Canada'), people),
    # Matthew lives in USA
    (membero, ('Matthew', var(), var(), 'USA'), people),
    # The person who has a black car lives in Australia
    (membero, (var(), var(), 'black', 'Australia'), people),
    # Jack has a cat
    (membero, ('Jack', 'cat', var(), var()), people),
    # Alfred lives in Australia
    (membero, ('Alfred', var(), var(), 'Australia'), people),
    # Person who owns the dog lives in France
    (membero, (var(), 'dog', var(), 'France'), people),
    # Who has a rabbit?
    (membero, (var(), 'rabbit', var(), var()), people)
)

solutions = run(0, people, rules)

output = ''
for house in solutions[0]:
    if 'rabbit' in house:
        output = house[0]


print('\nThe owner of the rabbit : ' + output)
attributes = ['Name', 'Pet', 'Color', 'Country']
print('\n' + '\t'.join(attributes))
print('_' * 40)
for item in solutions[0]:
    print('')
    print('\t'.join([str(x) for x in item]))
