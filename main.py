def overtime(params):
    start_of_day = params[0]  
    end_of_day = params[1]   
    hourly_rate = params[2]   
    overtime_multiplier = params[3]  
    
    regular_start = 9
    regular_end = 17 

    total_pay = 0

    if start_of_day < regular_end:
        regular_hours = min(end_of_day, regular_end) - max(start_of_day, regular_start)
        if regular_hours > 0:
            total_pay += regular_hours * hourly_rate

    if end_of_day > regular_end:
        overtime_hours = end_of_day - max(start_of_day, regular_end)
        if overtime_hours > 0:
            total_pay += overtime_hours * hourly_rate * overtime_multiplier

    return f"${total_pay:.2f}"

params = [13.25, 15, 30, 1.5] 
print(overtime(params)) 
