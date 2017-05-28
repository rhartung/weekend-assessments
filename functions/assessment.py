"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def robyn_town(home_town):
    """Function my_town takes a string as input and evaluates to boolean value
    True if it is Robyn Lundin's hometown of San Diego, and will evaluate to
    boolean value False otherwise"""

    # Used .lower() method in case input case is not consistent
    if home_town.lower() == "san diego":
        return True
    else:
        return False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def first_and_last_name(first_name, last_name):
    """Takes two strings, first name and last name, as input and returns the
    concatenation of the two names in one string with a space between the two"""

    return first_name + " " + last_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def our_towns(your_home_town, first_name, last_name):
    """Takes input of 3 strings: a town, a first name, and a last name.
    Evaluates if the input town is equivalent to Robyn Lundin's home town
    of San Diego.  If input is San Diego, program greets user by name and
    prints 'we're from the same place!' as a string.  Other towns will greet
    user by name and print 'I'd like to visit (home_town)!' as a string."""

    full_name = first_and_last_name(first_name, last_name)

    if robyn_town(your_home_town):
        print "Hi, %s, we're from the same place!" % (full_name)
    else:
        print "Hi, %s, I'd like to visit %s!" % (full_name, your_home_town)





###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if fruit == "strawberry":
        return True

    elif fruit == "blackberry":
        return True

    elif fruit == "raspberry":
        return True

    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    # calls is_berry function that determines if the fruit is a berry
    if is_berry(fruit):
        return 0

    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    # converted num input to a list and concatenated lst and num
    # assigned new_list variable to avoid mutating original list
    new_lst = lst + [num]

    return new_lst


def calculate_price(base_price, state_abr, tax_percent=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    # this will be full price for all states without extra fees
    full_price = base_price + (base_price * tax_percent)

    if state_abr == "CA":
        # California requires additional recycling fee
        recycle_fee = full_price * 0.03
        full_price = full_price + recycle_fee

    elif state_abr == "PA":
        # PA requires $2 highway safety fee
        full_price = full_price + 2

    elif state_abr == "MA":
        # MA requires commonwealth fund fee
        if base_price < 100:
            # Fee $1 if base price < $100
            full_price = full_price + 1
        else:
            # Fee $3 if base price >= $100
            full_price = full_price + 3
    # not sure if I need an 'else' statement here
    # left code without an 'else' statement because it passes the doctest
    # code also works if I add 'else: full_price = full_price'

    return full_price



###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.


def append_many_items(your_list, *items):
    """append_many_items function takes 2 arguments: a list and any number of
    additional arguments.  Will append additional arguments to original list
    and returns mutated list"""

    # '*items' method in function parameters found on multiple threads in
    # stack overflow

    your_list.extend(items)

    return your_list

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def word_plus_words_times_three(a_word):
    """words_times_three function will take one word as an argument and
    print a tuple containing two strings - the original word and the
    original word repeated three times without spaces."""

    # inner function returns a string that repeats input word three times
    def words_times_three(a_word):
        return a_word * 3

    three_words = words_times_three(a_word)

    print (a_word, three_words)
    # if return value desired uncomment line 261
    # return (a_word, three_words)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
