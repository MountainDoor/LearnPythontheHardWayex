print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "What is your feeling today(happy/sad)?",
feeling = raw_input()
print "How many coins do you carry?"
coins = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "I knwo you are feeling %r today, because you have %r coins."% (
    feeling, coins)
