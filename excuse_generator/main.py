import random

def excuse_generator():
    excuse = input("What's the reason you need an excuse today? ")
    who = ["The dog","The cat","My sister","My neighbour","The japanese mafia"]
    what = ["burnt", "lost", "took away", "dissapeared", "pissed"]
    when = ["just 5 minutes ago", "yesterday", "this morning", "last sunday", "last night"]
    print(random.choice(who) + " " +  random.choice(what) + " " + excuse + " " + random.choice(when))

excuse_generator()