def add_time(start, duration, day_of_week=False):
    week_days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    week_days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ampm_flip = {"AM": "PM", "PM": "AM"}

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_tuple_minutes = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_tuple_minutes[0])
    am_pm = start_tuple_minutes[2]

    day_amount = int(duration_hours / 24)

    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes % 60

    amount_ampmflip = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = 12 if end_hours == 0 else end_hours
    if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        day_amount += 1

    am_pm = ampm_flip[am_pm] if amount_ampmflip % 2 == 1 else am_pm

    returntime = str(end_hours) + ":" + str(end_minutes) + " " + am_pm
    if day_of_week:
        day_of_week = day_of_week.lower()
        index = int((week_days_index[day_of_week]) + day_amount) % 7
        new_day = week_days_array[index]
        returntime += ", " + new_day

    if day_amount == 1:
        return returntime + " (next day)"
    elif day_amount > 1:
        return returntime + " (" + str(day_amount) + " days later)"

    return returntime

# Added this in to perform a test of the function - it should print out 9:00 PM
new_time = add_time("10:00 AM", "11:00")
print(new_time)
