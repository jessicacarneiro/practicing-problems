r_day,r_month,r_year = map(int, raw_input().split())
e_day,e_month,e_year = map(int, raw_input().split())
fine = 0

if r_year == e_year:
    if r_month == e_month:
        if r_day <= e_day:
            fine = 0
        else:
            fine = (r_day - e_day) * 15
    elif r_month > e_month:
        fine = (r_month - e_month) * 500
elif r_year > e_year:
    fine = 10000

print fine