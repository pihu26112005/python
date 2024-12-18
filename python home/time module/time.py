import time

time1 = time.perf_counter()

time.sleep(4)

t2 = time.strftime('%H:%M:%S')
print(t2)
t = int (time.strftime('%H')) 
print(t)
b = int (time.strftime('%M'))
print(b)
c = int (time.strftime('%S'))
print(c)
a = (time.strftime('%a')) # %a = for day name
print(a)
b = (time.strftime('%b')) # %b = for month name
print(b)
c = (time.strftime('%c')) # %c = for everything
print(c)

'''
%Y: Year with century as a decimal number (e.g., 2023).
%y: Year without century as a zero-padded decimal number (e.g., 23 for 2023).
%m: Month as a zero-padded decimal number (01-12).
%d: Day of the month as a zero-padded decimal number (01-31).
%H: Hour (24-hour clock) as a zero-padded decimal number (00-23).
%M: Minute as a zero-padded decimal number (00-59).
%S: Second as a zero-padded decimal number (00-59).
%a: Weekday abbreviated name (e.g., 'Mon').
%A: Weekday full name (e.g., 'Monday').
%b: Month abbreviated name (e.g., 'Jan').
%B: Month full name (e.g., 'January').
%c: Locale's date and time representation (e.g., 'Mon Jan 1 00:00:00 2023').
%x: Locale's appropriate date representation (e.g., '01/01/23' for January 1, 2023).
%X: Locale's appropriate time representation (e.g., '00:00:00' for midnight).
%Z: Time zone name (e.g., 'UTC', 'EST', 'PST').
%%: A literal '%' character
'''