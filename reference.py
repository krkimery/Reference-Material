"""
    The various functions contained here-in are examples, and demos of sundry tools, ideas, etc.
"""
import pytz
import datetime

def demonstrate_python_timezones():
    """
        Python doesn't play very nice with timezones.
        You can (of course) work with timezones and daylight savings information,
        but it is a bit of a hassle.
    """
    print("Simple datetime date:")
    print(datetime.date(2019, 4, 5))
    print("Simple datetimes know nothing about hours, minutes, etc nor about timezones nor DST\n")

    print("Timezone-naive datetime.datetime:")
    print(datetime.datetime(2019, 4, 5, 23, 7, 55))

    print("Now (tz naive):")
    print(datetime.datetime.now())

    print("UTC now (also tz naive!!!)")
    print(datetime.datetime.utcnow())

    print("\nYou can use pytz to apply timezone and dst information to a datetime")
    print("This creates a timezone aware datetime:")
    tz_aware_time = pytz.timezone("US/Central").localize(datetime.datetime(2019, 4, 5, 23, 7, 55))
    print(tz_aware_time)

    print("Which you can convert to other timezones:")
    print(tz_aware_time.astimezone(pytz.timezone("UTC")))

    #timedeltas
    #pytz.timezone.normalize( datetime timedelta math over dst barrier )
    #more dst stuff
    


if __name__ == "__main__":
    print("************************")
    print("BEGIN DEMOS")
    print("************************")
    demonstrate_python_timezones()
