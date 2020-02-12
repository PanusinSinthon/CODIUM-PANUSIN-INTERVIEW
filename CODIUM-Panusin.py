import redis
def todo_list():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    db_name = 'to-do-list'
    def view_all_task():
        try:
            for i in range(0, r.llen(db_name)):
                print(r.lindex(db_name, i))
        except:
            print('To-do list is not found!')
    def add_task():
        print('Enter your tasks, Enter \' \' when you\'re finished!')
        while True:
            todo = input('--> ')
            if todo == ' ' or todo == 'q':
                break
            else:
                r.lpush(db_name,str(todo))
    def delete_task():
        if r.llen(db_name) == 0:
            print('To-Do list is empty!')
            return None
        while True:
            print('Enter task\'s' ' index you want to delete or q to quit')
            try:
                id = input('index ->')
                if id == 'q':break
                r.lrem(db_name,1,r.lindex(db_name,int(id)))
                view_all_task()
                if r.llen(db_name) == 0:
                    print('To-Do list is empty!')
                    break
            except Exception as ex:
                print(ex,'Invalid index')
    while True:
        print('Select operation, 1 view all tasks, 2 enter new task, 3 Delete task')
        operation = input('Number -> ')
        if operation == '1':
            view_all_task()
        elif operation == '2':
            add_task()
        elif operation == '3':
            delete_task()
        else:
            print('Quit!')
            break

#todo_list()

def easy_1():
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBizz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Bizz')
        else:
            print(x)
easy_1()

def easy_2(y):
    y = int(y)
    if int(y) % 400 == 0:
        print(str(y) + ' -> true')
    elif int(y) % 100 != 0 and int(y) % 4 == 0:
        print(str(y) + ' -> true')
    else:
        print(str(y) + ' -> false')
easy_2(1600)
easy_2(2000)
easy_2(1500)
easy_2(2004)
easy_2(2008)
easy_2(2010)

def easy_3_1(n):
    print('n ='+ str(n))
    for l in range(0, int(n)):
        star = ''
        m = -1
        while m < l:
            star += '*'
            m += 1
        print(star)

easy_3_1(3)
easy_3_1(4)
easy_3_1(6)


def easy_3_2(n):
    print('n =' + str(n))
    m = int(n)
    for l in range(0, int(n)):
        star = ''
        for g in range(0, int(n)):
            if g >= m - 1:
                star += '*'
            else:
                star += ' '
        print(star)
        m -= 1

easy_3_2(3)
easy_3_2(4)
easy_3_2(6)

def easy_3_3(n):
    print('n=' + str(n))
    n = int(n)
    m = 0
    for l in range(0, n):
        star = ''
        for g in range(0, (n * 2)):
            if g == (n - 1) - m or g == (n - 1) + m:
                star += '*'
            else:
                star += ' '
        print(star)
        m += 1

easy_3_3(1)
easy_3_3(2)
easy_3_3(3)
easy_3_3(4)
easy_3_3(5)

def medium_prime(n):
    result = (str(n) + '-> ')
    for num in range(2, n + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            result += str(num) + ' '

    print(result)



# Question 4
#In exception handling 'else' statement within any particular try-exception
#will be executed if only the exception does not thrown any exception(error occur!)
#whereas 'finally' statement must be executed either exception dose/dose not thrown an exception

medium_prime(20)