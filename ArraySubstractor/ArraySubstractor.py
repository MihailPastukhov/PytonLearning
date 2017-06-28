def arrays_difference():
    base = {"Alex", "Dima", "Kate", "Galina", "Ivan"}
    subtrahend = {"Dima", "Ivan", "Kate"}

    print base
    print subtrahend

    difference = list(set(base) - set(subtrahend))
    print difference


arrays_difference()
