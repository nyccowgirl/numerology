import meanings

from datetime import date

import string


def ask_year(who):
    """User input for birth year."""

    if who == "partner":
        year = "\nInput your partner's year of birth: "
    else:
        year = "\nInput your year of birth: "

    while True:
        # verify that input is integer
        raw_year = raw_input(year)
        if not raw_year.isdigit():
            print "Please input the year based on the Gregorian calendar."
        else:
            year = int(raw_year)
            return year


def ask_month(who):
    """User input for birth month."""

    if who == "partner":
        month = "Input your partner's month (1-12) of birth: "
    else:
        month = "Input your month (1-12) of birth: "

    while True:
        # verify that input is integer and between 1 and 12
        raw_month = raw_input(month)
        if not raw_month.isdigit():
            print "Please input the numerical value of the month."
        elif (int(raw_month) < 1) or (int(raw_month) > 12):
            print "That may be a month on Mars, but not on Earth!"
        else:
            month = int(raw_month)
            return month


def ask_day(year, month, who):
    """User input for birth day."""

    if who == "partner":
        day = "Input your partner's day of birth: "
    else:
        day = "Input your day of birth: "

    while True:
        # verify that input is appropriate given days in a specific month
        raw_day = raw_input(day)
        if not raw_day.isdigit():
            print "Please input the numerical value of the day."
        else:
            day = int(raw_day)
            if (month in [1, 3, 5, 7, 8, 10, 12]) and ((day < 1) or (day > 31)):
                print "That may be a day on Jupiter, but not on Earth!"
            elif (month in [4, 6, 9, 11]) and ((day < 1) or (day > 30)):
                print "That may be a day on Saturn, but not on Earth!"
            elif (month == 2) and (((year % 100 == 0) and (year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0))) and ((day < 1) or (day > 29)):
                # for leap year, if divisible by 100 but not 400, then not leap year. otherwise, divisible by 4.
                print "You took a flying leap off of Pluto!"
            elif (month == 2) and ((year % 4 != 0) or ((year % 4 == 0) and (year % 100 == 0))) and ((day < 1) or (day > 28)):
                print "That may be a day on Venus, but not on Earth!"
            else:
                return day


def ask_name(birth_or_nick, name_type):
    """User input for name."""

    if name_type == "last":
        if birth_or_nick == "birth":
            name = "\nInput your family (last) name at birth: "
        elif birth_or_nick == "partner":
            name = "\nInput your partner's family (last) name: "
        else:
            name = "\nInput your family (last) name: "
    elif name_type == "middle":
        if birth_or_nick == "birth":
            name = "Input your middle name at birth: "
        elif birth_or_nick == "partner":
            name = "Input your partner's middle name: "
        else:
            name = "Input your middle name: "
    elif name_type == "first":
        if birth_or_nick == "birth":
            name = "Input your first (given) name at birth: "
        elif birth_or_nick == "partner":
            name = "Input your partner's first name: "
        else:
            name = "Input your first (nick) name: "

    while True:
        # verify that input is not integer
        raw_name = raw_input(name)
        if raw_name.isdigit():
                print "Your parents are so hipster that they named you a number."
        else:
            return raw_name


def clean_name(name):
    """Reformats name for lower case and removal of any special characters."""

    name = name.lower()
    partial_name = ""

    for letter in name:
        if letter in string.ascii_lowercase:
            partial_name += letter

    return partial_name


def single_digit_master(single_digit):
    """Calculates number down to 1-9, 11 or 22."""

    while True:
        if (single_digit <= 9) or (single_digit == 11) or (single_digit == 22):
            single_digit_master = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_master


def single_digit_uno(single_digit):
    """Calculates number down to single digits."""

    while True:
        if single_digit <= 9:
            single_digit_uno = single_digit
            break
        else:
            partial_sum = 0
            for number in str(single_digit):
                partial_sum += int(number)
            single_digit = partial_sum

    return single_digit_uno


def life_path_calc(single_year_master, single_month_master, single_day_master):
    """Calculates life path number."""

    # takes each category of year, month and day after it has been sum to 1-9,
    # 11 or 22 and then adds the three variables together
    life_path_raw = single_year_master + single_month_master + single_day_master

    # the individual digits of the result are then added together until it
    # equals 1-9, 11 or 22
    life_path = single_digit_master(life_path_raw)

    return life_path


def first_chall_calc(single_day_uno, single_month_uno):
    """Calculates first challenge number."""

    # difference between digits of birth month and birth day, individually
    # summed down to 1-9
    first_chall = abs(single_day_uno - single_month_uno)

    return first_chall


def first_chall_meaning(first_chall):
    """Displays meaning based on first challenge number calculation."""

    print """\nYour first challenge number is {}, which is from birth to
            approximately age 35.\n""".format(first_chall)

    meanings.chall_meaning(first_chall)


def sec_chall_calc(single_day_uno, single_year_uno):
    """Calculates second challenge number."""

    # difference between digits of birth year and birth day, individually summed
    # down to 1-9
    sec_chall = abs(single_year_uno - single_day_uno)

    return sec_chall


def sec_chall_meaning(sec_chall):
    """Displays meaning based on second challenge number calculation."""

    print """\nYour second challenge number is {}, which is from approximately
            age 35 to approximately age 60.\n""".format(sec_chall)

    meanings.chall_meaning(sec_chall)


def third_chall_calc(first_chall, sec_chall):
    """Calculates third callenge number."""

    # difference betwen first and second challenge numbers
    third_chall = abs(sec_chall - first_chall)

    return third_chall


def third_chall_meaning(third_chall):
    """Displays meaning based on third challenge number calculation."""

    print """\nYour third challenge number is {}, which represents the primary
        challenge that one faces throughout life.\n""".format(third_chall)

    meanings.chall_meaning(third_chall)


def fourth_chall_calc(single_month_uno, single_year_uno):
    """Calculates fourth challenge number."""

    # difference between digits of birth year and birth month, individually
    # summed down to 1-9
    fourth_chall = abs(single_year_uno - single_month_uno)

    return fourth_chall


def fourth_chall_meaning(fourth_chall):
    """Displays meaning based on fourth challenge number calculation."""

    print """\nYour fourth (and final) challenge number is {}, which from
        approximately age 60 to end of life.\n""".format(fourth_chall)

    meanings.chall_meaning(fourth_chall)


def pers_year_calc(single_day_uno, single_month_uno, single_year_uno, month, day):
    """Calculates personal year number."""

    # calculates current year digits down to single digit 1-9
    single_current_uno = single_digit_uno(date.today().year)

    # takes each category of current year, month and day of birth after it has
    # been sum to 1-9 and then adds the three variables together
    personal_year_raw = single_current_uno + single_month_uno + single_day_uno

    # the individual digits of the result are then added together until it
    # equals 1-9
    personal_year = single_digit_uno(personal_year_raw)

    # pulls today's date and birth day in current year
    birth_raw = date(date.today().year, month, day)

    # if birthday has not occurred yet, then personal year is adjusted to prior
    # personal year number since personal year number is effective from birthday
    # to birthday
    if date.today() < birth_raw:
        personal_year = personal_year - 1

    return personal_year


def name_calc(name):
    """Converts name to number. Each letter is assigned a number from 1-9."""

    # assigns each letter a numerical value from 1-9 using ascii value and
    # calculates the total value of the word
    partial_sum = 0

    for letter in range(len(name)):
        partial_name = ((ord(name[letter]) - ord("a")) % 9) + 1
        partial_sum += partial_name

    name_value = partial_sum

    return name_value


def exp_calc(single_last_master, single_middle_master, single_first_master):
    """Calculates expression/destiny number."""

    # takes each category of last, middle and first names after it has been sum
    # to 1-9, 11 or 22 and then adds the three variables together
    exp_raw = single_last_master + single_middle_master + single_first_master

    # the individual digits of the result are then added together until it
    # equals 1-9, 11 or 22
    exp_dest = single_digit_master(exp_raw)

    return exp_dest


def consonants(name, vowel):
    """Strips name to consonants only."""

    cons_name = name

    for letter in name:
        if letter in vowel:
            cons_name = cons_name.replace(letter, "")

    return cons_name


def vowels(name, vowel):
    """Strips name to vowels only."""

    vow_name = name

    for letter in name:
        if letter not in vowel:
            vow_name = vow_name.replace(letter, "")

    return vow_name


def soul_urge_calc(single_vow_last_master, single_vow_middle_master,
                   single_vow_first_master):
    """Calculates soul urge number."""

    # takes each category of last, middle and first names after it has been sum
    # to 1-9, 11 or 22 based on vowels only and then adds the three variables
    # together
    soul_urge_raw = (single_vow_last_master + single_vow_middle_master +
                     single_vow_first_master)

    # the individual digits of the result are then added together until it
    # equals 1-9, 11 or 22
    soul_urge = single_digit_master(soul_urge_raw)

    return soul_urge


def personality_cal(single_cons_last_master, single_cons_middle_master,
                    single_cons_first_master):
    """Calculates personality number."""

    # takes each category of last, middle and first names after it has been sum
    # to 1-9, 11 or 22 based on consonants only and then adds the three
    # variables together
    personality_raw = (single_cons_last_master + single_cons_middle_master +
                       single_cons_first_master)

    # the individual digits of the result are then added together until it
    # equals 1-9, 11 or 22
    personality = single_digit_master(personality_raw)

    return personality


def pass_calc(name):
    """Calculates hidden passion number."""

    # assigns each letter a numerical value from 1-9 and determines the number
    # that is the most repetitive
    for letter in range(len(name)):
        partial_name = ((ord(name[letter]) - ord("a")) % 9) + 1

    partial_name = str(partial_name)
    hid_pass = int(max(partial_name, key=partial_name.count))

    return hid_pass


def karmic_calc(cons_full_name):
    """Calculates karmic number."""

    # strips full name of consonants only, converts into numerical value based
    # on sum of each individual letter (assigned a numerical value from 1-9),
    # and sum digits down to 1-9
    karmic = single_digit_uno(name_calc(cons_full_name))

    return karmic


def corn_cap(first_name):
    """Displays cornerstone and capstone meanings. Cornerstone is first letter
    in first name. Capstone is last letter in first name."""

    cornerstone = first_name[0]
    capstone = first_name[-1]

    print """\nCornerstone gives insight into how you approach challenges in
            life and how you master situations. Capstone gives insight into how
            you make transitions in your life, how you finish projects or move
            from one thing into another.\n"""

    print """Your cornerstone ({}): """.format(cornerstone.upper())
    meanings.cc_meaning(cornerstone)

    print """Your capstone ({}): """.format(capstone.upper())
    meanings.cc_meaning(capstone)

    return cornerstone, capstone


def ask_partner():
    """User input if specific partner will be included in analysis."""

    while True:
        # asks individual if he/she has a specific partner
        partner_raw = raw_input("""\nDo you currently have a specific partner that
                                    you would like to assess? (Y/N): """)

        partner_raw = partner_raw.lower()

        # verify for edge cases of other inputs
        if not ((partner_raw == "y") or (partner_raw == "n")):
            print "Please input Y or N."
        else:
            return partner_raw


# definition of a function to obtain partner's birthday information and calculate life path number


def partner_life_path(ind_life_path):
    """User input for partner's birthday information. Calculates life path
    number."""

    # asks for partner's birthday
    year = ask_year("partner")
    month = ask_month("partner")
    day = ask_day(year, month, "partner")

    # calculates single digits master for year, month and day
    single_year_master = single_digit_master(year)
    single_month_master = single_digit_master(month)
    single_day_master = single_digit_master(day)

    # calculates life path number
    life_path = (life_path_calc(single_year_master, single_month_master,
                                single_day_master))

    # displays partner's life path number
    print """\nYour and your partner's life path numbers are {} and {},
            respectively.\n""".format(ind_life_path, life_path)

    print """\nFor relationship purposes, life path numbers are reduced to
            single digits (e.g., master numbers 11 and 22 are reduced to 2 and
            4, respectively).\n"""

    # calculates life path number to single digit
    partner_life_path = single_digit_uno(life_path)

    return partner_life_path


def partner_exp_dest(ind_exp_dest):
    """User input for partner's name information. Calculates expresion number."""

    # asks for partner's birthday
    last_name = clean_name(ask_name("partner", "last"))
    middle_name = clean_name(ask_name("partner", "middle"))
    first_name = clean_name(ask_name("partner", "first"))

    # calculate single digits master for first, middle and last names
    single_last_master = single_digit_master(name_calc(last_name))
    single_middle_master = single_digit_master(name_calc(middle_name))
    single_first_master = single_digit_master(name_calc(first_name))

    # calculates expression (destiny) number
    exp_dest = (exp_calc(single_last_master, single_middle_master,
                         single_first_master))

    # displays partner's expression (destiny) number
    print """\nYour and your partner's expression (destiny) numbers are {} and
            {}, respectively.\n""".format(ind_exp_dest, exp_dest)

    print """\nFor relationship purposes, expression (destiny) numbers are
            reduced to single digits (e.g., master numbers 11 and 22 are reduced
            to 2 and 4, respectively).\n"""

    # calculates expression (destiny) number to single digit
    partner_exp_dest = single_digit_uno(exp_dest)

    return partner_exp_dest


# definition of a function to create file output for results of numerology


def numerology_rpt(nick_name, first_name, nick_first_name, year, month, day,
                   last_name, middle_name, clean_first_name, nick_last_name,
                   nick_middle_name, clean_nick_first_name, vowel):
    """Creates file output for results of numerology analysis."""

    import sys
    # keeps copy of original stdout
    stdout_backup = sys.stdout

    # creates file to write various results of numerology calculations
    with open("report.txt", "w") as file:
        # redirecting standard output point to output file so that subsequent
        # calls to print will write to output file
        sys.stdout = file

        # writes to file introduction with individual's name
        if nick_name == "y":
            file.write("{}, the following is your numerology report:\n"
                .format(nick_first_name.title()))
        else:
            file.write("{}, the following is your numerology report:\n"
                .format(first_name.title()))

        # calculates single digits master for year, month and day
        single_year_master = single_digit_master(year)
        single_month_master = single_digit_master(month)
        single_day_master = single_digit_master(day)

        # calculates single digits for year, month and day
        single_year_uno = single_digit_uno(year)
        single_month_uno = single_digit_uno(month)
        single_day_uno = single_digit_uno(day)

        # calculates and display meaning for life path number
        life_path = (life_path_calc(single_year_master, single_month_master,
                                    single_day_master))
        meanings.life_path_meaning(life_path)

        # calculates and display meaning for birth day number
        meanings.birth_day_meaning(single_day_master)

        # calculates and displays meanings for challenge numbers
        meanings.challenge_intro()

        # calculates and displays meaning for first challenge number
        first_chall = first_chall_calc(single_day_uno, single_month_uno)
        first_chall_meaning(first_chall)

        # calculates and displays meaning for second challenge number
        sec_chall = sec_chall_calc(single_day_uno, single_year_uno)
        sec_chall_meaning(sec_chall)

        # calculates and displays meaning for third challenge number (note that
        # since user may not choose option 1 or 2, first and second challenge
        # functions would have to be called here to calculate variabbles used in
        # third challenge number)
        third_chall = third_chall_calc(first_chall, sec_chall)
        third_chall_meaning(third_chall)

        # calculates and displays meaning for fourth challenge number
        fourth_chall = fourth_chall_calc(single_month_uno, single_year_uno)
        fourth_chall_meaning(fourth_chall)

        # calculate and display meaning for personal year number
        personal_year = (pers_year_calc(single_day_uno, single_month_uno,
                                        single_year_uno, month, day))
        meanings.pers_year_meaning(personal_year)

        # concatenates full name (maybe use strip function if "0" used for blank
        # names but it seems to not work)
        full_name = last_name + middle_name + clean_first_name

        # calculates single digits master for first, middle and last names
        single_last_master = single_digit_master(name_calc(last_name))
        single_middle_master = single_digit_master(name_calc(middle_name))
        single_first_master = single_digit_master(name_calc(clean_first_name))

        # separates consonants only of first, middle and last names
        cons_last_name = consonants(last_name, vowel)
        cons_middle_name = consonants(middle_name, vowel)
        cons_first_name = consonants(clean_first_name, vowel)
        cons_full_name = consonants(full_name, vowel)

        # separates vowels only of first, middle and last names
        vow_last_name = vowels(last_name, vowel)
        vow_middle_name = vowels(middle_name, vowel)
        vow_first_name = vowels(clean_first_name, vowel)

        # calculates single digits master of first, middle and last names by
        # consonants only
        single_cons_last_master = single_digit_master(name_calc(cons_last_name))
        single_cons_middle_master = single_digit_master(name_calc(cons_middle_name))
        single_cons_first_master = single_digit_master(name_calc(cons_first_name))

        # calculates single digits master of first, middle and last names by
        # vowels only
        single_vow_last_master = single_digit_master(name_calc(vow_last_name))
        single_vow_middle_master = single_digit_master(name_calc(vow_middle_name))
        single_vow_first_master = single_digit_master(name_calc(vow_first_name))

        # calculates and displays meaning for expression (destiny) number
        exp_dest = (exp_calc(single_last_master, single_middle_master,
                             single_first_master))
        meanings.exp_dest_meaning(exp_dest)

        # calculates and displays meaning for soul urge number
        soul_urge = (soul_urge_calc(single_vow_last_master, single_vow_middle_master,
                                    single_vow_first_master))
        meanings.soul_urge_meaning(soul_urge)

        # calculates and displays meaning for personality number
        personality = (personality_cal(single_cons_last_master, single_cons_middle_master,
                       single_cons_first_master))
        meanings.personality_meaning(personality)

        # calculates and displays meaning for hidden passion number
        hid_pass = pass_calc(full_name)
        meanings.hid_pass_meaning(hid_pass)

        # calculates and displays meaning for karmic number
        karmic = karmic_calc(cons_full_name)
        meanings.karmic_meaning(karmic)

        # displays meanings for cornerstone and capstone
        corn_cap(clean_first_name)

        if nick_name == "y":
            # writes to file introduction that following section relates to the
            # nick name
            file.write("""\nThe following section represents the various numbers
                        as it relates to your common (nick) name.\n\nA common
                        (nick) name introduces energies not present in the birth
                        name. New energies may be compatible or comflicting, and
                        enhance the birth name or restrict its power.\n\nThe
                        energies of the birth name never go away. Common names
                        are a layer over the birth name, similar to the
                        foundation of a house with common name representing the
                        house and any changes to that as new coats of paint.\n""")

            # concatenates full name (maybe use strip function if "0" used for
            # blank names but it seems to not work)
            nick_full_name = (nick_last_name + nick_middle_name +
                              clean_nick_first_name)

            # calculates single digits master for first, middle and last names
            single_nick_last_master = single_digit_master(name_calc(nick_last_name))
            single_nick_middle_master = single_digit_master(name_calc(nick_middle_name))
            single_nick_first_master = single_digit_master(name_calc(clean_nick_first_name))

            # separates consonants only of first, middle and last names
            cons_nick_last_name = consonants(nick_last_name, vowel)
            cons_nick_middle_name = consonants(nick_middle_name, vowel)
            cons_nick_first_name = consonants(clean_nick_first_name, vowel)
            cons_nick_full_name = consonants(nick_full_name, vowel)

            # separates vowels only of first, middle and last names
            vow_nick_last_name = vowels(nick_last_name, vowel)
            vow_nick_middle_name = vowels(nick_middle_name, vowel)
            vow_nick_first_name = vowels(clean_nick_first_name, vowel)

            # calculates single digits master of first, middle and last names by
            # consonants only
            single_cons_nick_last_master = single_digit_master(name_calc(cons_nick_last_name))
            single_cons_nick_middle_master = single_digit_master(name_calc(cons_nick_middle_name))
            single_cons_nick_first_master = single_digit_master(name_calc(cons_nick_first_name))

            # calculates single digits master of first, middle and last names by
            # vowels only
            single_vow_nick_last_master = single_digit_master(name_calc(vow_nick_last_name))
            single_vow_nick_middle_master = single_digit_master(name_calc(vow_nick_middle_name))
            single_vow_nick_first_master = single_digit_master(name_calc(vow_nick_first_name))

            # calculates and displays meaning for expression (destiny) number
            exp_dest = (exp_calc(single_nick_last_master, single_nick_middle_master,
                        single_nick_first_master))
            meanings.exp_dest_meaning(exp_dest)

            # calculates and displays meaning for soul urge number
            soul_urge = (soul_urge_calc(single_vow_nick_last_master,
                         single_vow_nick_middle_master,
                         single_vow_nick_first_master))
            meanings.soul_urge_meaning(soul_urge)

            # calculates and displays meaning for personality number
            personality = (personality_cal(single_cons_nick_last_master,
                           single_cons_nick_middle_master,
                           single_cons_nick_first_master))
            meanings.personality_meaning(personality)

           # calculates and displays meaning for hidden passion number
            hid_pass = pass_calc(nick_full_name)
            meanings.hid_pass_meaning(hid_pass)

            # calculates and displays meaning for karmic number
            karmic = karmic_calc(cons_nick_full_name)
            meanings.karmic_meaning(karmic)

            # displays meanings for cornerstone and capstone
            corn_cap(clean_nick_first_name)

        # calculates life path number to single digit for compatibility purposes
        life_path_uno = single_digit_uno(life_path)
        meanings.comp_gen(life_path_uno)

        sys.stdout = stdout_backup
