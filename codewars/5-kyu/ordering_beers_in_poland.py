NUMBERS_0_TO_9 = {
    0: "zero",
    1: "jeden",
    2: "dwa",
    3: "trzy",
    4: "cztery",
    5: "piec",
    6: "szesc",
    7: "siedem",
    8: "osiem",
    9: "dziewiec"
}

NUMBERS_10_TO_19 = {
    10: "dziesiec",
    11: "jedenascie",
    12: "dwanascie",
    13: "trzynascie",
    14: "czternascie",
    15: "pietnascie",
    16: "szesnascie",
    17: "siedemnascie",
    18: "osiemnascie",
    19: "dziewietnascie"
}


def pick_quantifier(n):
    if n == 1:
        return "piwo"
    if n in [12, 13, 14]:
        return "piw"

    digits = len(str(n))
    if digits == 1:
        if n in [2, 3, 4]:
            return "piwa"

    if digits == 2:
        last_digit = str(n)[-1]
        if int(last_digit) in [2, 3, 4]:
            return "piwa"

    return "piw"


def ordering_beers(beers):
    digits = len(str(beers))

    if digits == 1:
        if beers == 0:
            return "Woda mineralna poprosze"
        if beers == 1:
            return "Jedno piwo poprosze"
        else:
            return f'{NUMBERS_0_TO_9[beers]} {pick_quantifier(beers)} poprosze'.capitalize()
    elif digits == 2:
        if int(str(beers)[0]) == 1:
            return f'{NUMBERS_10_TO_19[beers]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 2:
            if int(str(beers)[1]) == 0:
                return f'dwadziescia {pick_quantifier(beers)} poprosze'.capitalize()

            return f'dwadziescia {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 3:
            if int(str(beers)[1]) == 0:
                return f'trzydziesci {pick_quantifier(beers)} poprosze'.capitalize()

            return f'trzydziesci {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 4:
            if int(str(beers)[1]) == 0:
                return f'czterdziesci {pick_quantifier(beers)} poprosze'.capitalize()

            return f'czterdziesci {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 5:
            if int(str(beers)[1]) == 0:
                return f'piecdziesiat {pick_quantifier(beers)} poprosze'.capitalize()

            return f'piecdziesiat {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 6:
            if int(str(beers)[1]) == 0:
                return f'szescdziesiat {pick_quantifier(beers)} poprosze'.capitalize()

            return f'szescdziesiat {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 7:
            if int(str(beers)[1]) == 0:
                return f'siedemdziesiat {pick_quantifier(beers)} poprosze'.capitalize()

            return f'siedemdziesiat {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 8:
            if int(str(beers)[1]) == 0:
                return f'osiemdziesiat {pick_quantifier(beers)} poprosze'.capitalize()

            return f'osiemdziesiat {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
        if int(str(beers)[0]) == 9:
            if int(str(beers)[1]) == 0:
                return f'dziewiecdziesiat {pick_quantifier(beers)} poprosze'.capitalize()

            return f'dziewiecdziesiat {NUMBERS_0_TO_9[int(str(beers)[-1])]} {pick_quantifier(beers)} poprosze'.capitalize()
    else:
        raise Exception("Out of range! (0-99)")
