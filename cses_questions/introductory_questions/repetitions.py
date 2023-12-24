def repetitions(chain):
    chain = chain + 'E' # append an extra character to the end so if the chain is all one base, its still added to the list
    current_base = chain[0]
    repetition = 0
    repetitions = []
    for base in chain:
        if current_base == base:
            repetition += 1
        else:
            repetitions.append(repetition)
            repetition = 1
        current_base = base

    print(max(repetitions))

repetitions(input())