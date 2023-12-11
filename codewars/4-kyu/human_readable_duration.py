def format_duration(seconds):
    times = ["year", "day", "hour", "minute", "second"]

    if seconds == 0:
        return "now"
    else:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)

        time = [years, days, hours, mins, secs]

        duration = []

        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {times[x]}")
            elif i > 1:
                duration.append(f"{i} {times[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]