def validate_emp_cred_dept(employees, access_logs):
    employee = {}
    for emp in employees:
        emp_id, emp_name, dept, role = emp.split(":")
        employee[emp_id] = {
            "emp_name" : emp_name,
            "dept" : dept,
            "role" : role
        }
    print("Employee DataBase: ")
    print("             ")
    emp = employee
    for e in emp:
        print(f"{e} : {emp[e]['emp_name']} ({emp[e]['dept']} - {emp[e]['role']})")

    access = {}
    for acc in access_logs:
        emp_id, areas, result, time, minutes = acc.split(":")
        access[emp_id] = {
            "areas" : areas,
            "result" : result,
            "time" : time,
            "minutes" : minutes
        }
    print("             ")
    print(access)
    print("Access Summary: ")
    print("             ")
    print(f"Total Access Attempts: {len(access_logs)}")


def track_access_attempts(access_logs):
    succ = 0
    fail = 0
    for acc in access_logs:
        res = acc.split(":")
        print(res)
        for ele in res:
            if ele == 'SUCCESS':
                succ += 1
            if ele == 'FAILED':
                fail += 1
    print(f'Successful Access: {succ}')
    print(f'Failed Access: {fail}')


def security_violation(employees, department_access_rights, access_logs):
    employee = {}
    for emp in employees:
        emp_id, emp_name, dept, role = emp.split(":")
        employee[emp_id] = {
            "emp_name" : emp_name,
            "dept" : dept,
            "role" : role
        }
    print(employee)
    emp = employee
    for acc in access_logs:
        res = acc.split(":")
        print(res)
        for ele in res:
            if ele == "SERVER_ROOM" or ele == "Failed":
                print(f'{acc}')

    for e in emp:
        if emp[e]['dept'] == 'Finance' :
            print(f"{e} ({emp[e]['emp_name']} - {emp[e]['dept']}): Attempted access to SERVER_ROOM")
        if emp[e]['dept'] == 'HR':
            print(f"{e} ({emp[e]['emp_name']} - {emp[e]['dept']}): Attempted access to SERVER_ROOM")

def department_wise_access_reports(employees, access_logs):

    employee = {}
    for emp in employees:
        emp_id, emp_name, dept, role = emp.split(":")
        employee[emp_id] = {
            "emp_name" : emp_name,
            "dept" : dept,
            "role" : role
        }
    print(employee)

    Eng = 0
    hr = 0
    fin = 0
    sec = 0
    for acc in access_logs:
        emp_id, area, result, time, minutes = acc.split(":")
        
        dept = employee[emp_id]['dept']
        if dept == 'Engineering' and result == 'SUCCESS':
            Eng += 1
        if dept == 'HR' and result == 'SUCCESS':
            hr += 1
        if dept == 'Finance' and result == 'SUCCESS':
            fin += 1
        if dept == 'Security' and result == 'SUCCESS':
            sec += 1
    print(Eng)
    print(hr)
    print(fin)
    print(sec)
        
    


employees = [ 
"EMP001:John_Smith:Engineering:SENIOR", 
"EMP002:Sarah_Johnson:HR:MANAGER", 
"EMP003:Mike_Brown:Finance:JUNIOR", 
"EMP004:Lisa_Davis:Engineering:MANAGER", 
"EMP005:Tom_Wilson:Security:SENIOR" 
]

department_access_rights = { 
"Engineering": {"LAB", "SERVER_ROOM", "OFFICE", "PARKING"}, 
"HR": {"HR_OFFICE", "OFFICE", "PARKING", "MEETING_ROOM"}, 
"Finance": {"FINANCE_OFFICE", "OFFICE", "PARKING"}, 
"Security": {"ALL_AREAS"} 
} 

access_logs = [ 
"EMP001:LAB:SUCCESS:09:15", 
"EMP002:HR_OFFICE:SUCCESS:09:30", 
"EMP003:SERVER_ROOM:FAILED:10:00", 
"EMP001:SERVER_ROOM:SUCCESS:10:15", 
"EMP004:LAB:SUCCESS:11:00", 
"EMP005:FINANCE_OFFICE:SUCCESS:11:30",
"EMP002:SERVER_ROOM:FAILED:12:00", 
"EMP003:FINANCE_OFFICE:SUCCESS:14:00" 
]


validate_emp_cred_dept(employees, access_logs)
track_access_attempts(access_logs)
security_violation(employees, department_access_rights, access_logs)
department_wise_access_reports(employees, access_logs)