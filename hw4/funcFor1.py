def salary(working_out, rate_per_hour, bonus):
    try:
        return (working_out*rate_per_hour) + bonus
    except TypeError:
        return