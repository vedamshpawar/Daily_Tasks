def top_3_performers(employees):
    sales = []
    marketing = []
    it = []
    for tup in employees:
        if tup[2] == 'Sales':
            sales.append(tup)
        if tup[2] == 'Marketing':
            marketing.append(tup)
        if tup[2] == 'IT':
            it.append(tup)
    
    sort_bysales = sorted(sales, key=lambda x : x[3], reverse=True)
    sort_bymarket = sorted(marketing, key=lambda x : x[3], reverse=True)
    sort_byit = sorted(it, key=lambda x : x[3], reverse=True)
    print("                    ")
    print("Sales department: ")
    num = 1
    for tup in sort_bysales[:3]:
        name = tup[1]
        salary = tup[3]
        print(f'{num}.{name}, {salary}')
        num += 1
    print("                    ")
    print("Marketing Department: ")
    num = 1
    for tup in sort_bymarket[:3]:
        name = tup[1]
        salary = tup[3]
        print(f'{num}.{name}, {salary}')
        num += 1
    print("                    ")
    print('IT Department')
    num = 1
    for tup in sort_byit[:3]:
        name = tup[1]
        salary = tup[3]
        print(f'{num}.{name}, {salary}')
        num += 1
    
        

def average_rating(employees):
    sales = []
    marketing = []
    it = []
    for tup in employees:
        if tup[2] == 'Sales':
            sales.append(tup)
        if tup[2] == 'Marketing':
            marketing.append(tup)
        if tup[2] == 'IT':
            it.append(tup)

    sum_sales = 0
    sum_marketing = 0
    sum_it = 0
    avg_sales = 0
    avg_marketing = 0
    avg_it = 0
    for tup in employees:
        if tup[2] == 'Sales':
            sum_sales += tup[4]
            avg_sales += sum_sales / len(sales)
        if tup[2] == 'Marketing':
            sum_marketing += tup[4]
            avg_marketing += sum_marketing / len(marketing)
        if tup[2] == 'IT':
            sum_it += tup[4]
            avg_it += sum_it / len(it)
    print("            ")
    print("Department Average Rating: ")
    print(f'Sales : {avg_sales}')
    print(f'Marketing : {avg_marketing}')
    print(f'IT : {avg_it} ')
    print("                ")
    print('Employees Needing Improvement (Rating < 3.0):')
    

def emp_need_performance_rating(employees):
    rating = 3.0
    for tup in employees:
        if tup[4] < rating:
            name = tup[1]
            dept = tup[2]
            rating = tup[4]
            print(f'{name}({dept}): Rating {rating}')
    
    print("                 ")
    print('Performance Ranking (Sales × Rating):')

def performance_ranking(employees):
    # sales = 0
    # emp = 0
    num = 1
    for tup in employees:
        sales = tup[3] * tup[4]
        emp = tup[1]
        print(f'{num}. {emp} : {sales}')
        num += 1
        
def count_of_specific_dept(employees):
    sales = 0
    marketing = 0
    IT = 0
    for tup in employees:
        if tup[2] == 'Sales':
            sales += 1
        if tup[2] == 'Marketing':
            marketing += 1
        if tup[2] == 'IT':
            IT += 1
    
    # print(f'Sales :{sales},Marketing: {marketing}, IT : {IT} ')
   

def average_of_each_dept(employees):
    sales = []
    len_sales = 0
    marketing = []
    len_marketing = 0
    it = []
    len_IT = 0
    sum_of_sales = 0
    sum_of_market = 0
    sum_of_it = 0
    avg_sales = 0
    avg_market = 0
    avg_it = 0
    sum_of_rate_sales = 0
    sum_of_rate_market = 0
    sum_of_rate_it = 0
    avg_rating_sales = 0
    avg_rating_market = 0
    avg_rating_it = 0

    for tup in employees:
        if tup[2] == 'Sales':
            sales.append(tup)
            len_sales += 1
            sum_of_sales += tup[3]
            sum_of_rate_sales += tup[4]
            avg_sales += sum_of_sales / len(sales)
            avg_rating_sales += sum_of_rate_sales / len(sales)
            

        if tup[2] == 'Marketing':
            marketing.append(tup)
            sum_of_market += tup[3]
            len_marketing += 1
            sum_of_rate_market += tup[4]
            avg_market += sum_of_market / len(marketing)
            avg_rating_market += sum_of_rate_market / len(marketing)
            
        if tup[2] == 'IT':
            it.append(tup)
            len_IT += 1
            sum_of_it += tup[3]
            sum_of_rate_it += tup[4]
            avg_it += sum_of_it / len(it)
            avg_rating_it += sum_of_rate_it / len(it)
    
    print("                 ")
    print("Department Performance Sales: ")
    print(f'Sales employees:{len_sales}, sum of sales: $ {sum_of_sales}, average of sales :$ {avg_sales}, average rate of sales: {avg_rating_sales}')
    print(f'Marketing employees: {len_marketing}, sum of market: $ {sum_of_market}, average of market:$ {avg_market}, average of rate market: {avg_rating_market}')
    print(f'IT employees: {len_IT}, sum of IT: $ {sum_of_it}, average of IT:$ {avg_it}, average rate of IT: {avg_rating_it}')
            
    


employees = [ (1001, "Alice Johnson", "Sales", 15000, 4.2),
(1002, "Bob Smith", "Sales", 12000, 3.8),
(1003, "Carol Davis", "Marketing", 8000, 4.5),
(1004, "David Brown", "Sales", 18000, 4.0),
(1005, "Eva Wilson", "Marketing", 9500, 3.2),
(1006, "Frank Miller", "IT", 11000, 3.9),
(1007, "Grace Lee", "Sales", 13500, 2.1),
(1008, "Henry Taylor", "IT", 10500, 4.1),
(1009, "Ivy Chen", "Marketing", 7800, 3.7),
(1010, "Jack Davis", "IT", 12500, 3.5) ]

top_3_performers(employees)
average_rating(employees)
emp_need_performance_rating(employees)
performance_ranking(employees)
count_of_specific_dept(employees)
average_of_each_dept(employees)