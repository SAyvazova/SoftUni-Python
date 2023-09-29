nr_pages_in_book = int(input())

pages_read_per_hour = int(input())

days_to_read_the_book = int(input())

hours_per_day = (nr_pages_in_book//pages_read_per_hour)//(days_to_read_the_book)

print (hours_per_day)
