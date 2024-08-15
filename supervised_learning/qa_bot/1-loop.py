#!/usr/bin/env python3

prompt = "Q: "
loop = True
answer = None


def is_farewell(judgeme):
    """
    returns whether or not the input is a farewell phrase
    """
    farewells = ["exit", "quit", "goodbye", "bye"]
    # make input case insensitive
    if isinstance(judgeme, str):
        judgeme = judgeme.casefold()
    return judgeme in farewells


def reply(say_this=None):
    """
    puts a prefix in front of say_this
    prints the result
    """
    if not say_this:
        print("A:")
    # below will never happen in task 1
    # exists for transferability
    else:
        print("A:", say_this)


while loop:
    # Get user input
    user_said = input(prompt)
    # mission complete
    if is_farewell(user_said):
        # redundancy just in case
        loop = False

        answer = "Goodbye"
        reply(answer)
        continue
    reply(answer)
