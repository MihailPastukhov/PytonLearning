def arrays_difference():
    base = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
    subtrahend = ["Dima", "Ivan", "Kate"]

    print base
    print subtrahend

    for item in subtrahend:
        if item in base:
            base.remove(item)
    print base


arrays_difference()
