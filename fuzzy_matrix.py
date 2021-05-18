
least = [0 for i in range(40)]
less = [0 for i in range(40)]
little = [0 for i in range(40)]
normal = [0 for i in range(40)]
much = [0 for i in range(40)]
more =[0 for i in range(40)]
most = [0 for i in range(40)]
car_num = []

# SQL语句文本
context = []

# 车很少
def make_least():
    for i in range(1,3):
        least[i] = 1
    for i in range(3,7):
        least[i] = 0.8
    for i in range(7,10):
        least[i] = 0.4
    for i in range(10,14):
        least[i] = 0.1
    for i in range(14,40):
        least[i] = 0

# 车较少
def make_less():
    for i in range(0,3):
        less[i] = 0.2
    for i in range(3,7):
        less[i] = 0.7
    for i in range(7,10):
        less[i] = 1
    for i in range(10,14):
        less[i] = 0.7
    for i in range(14,40):
        less[i] = 0

# 车少
def make_little():
    for i in range(0,3):
        little[i] = 0
    for i in range(3,7):
        little[i] = 0.2
    for i in range(7,10):
        little[i] = 0.7
    for i in range(10,14):
        little[i] = 1
    for i in range(14,18):
        little[i] = 0.5
    for i in range(18,40):
        little[i] = 0

# 车正常
def make_normal():
    for i in range(0,14):
        normal[i] = 0
    for i in range(14,18):
        normal[i] = 0.5
    for i in range(18,24):
        normal[i] = 1
    for i in range(24,27):
        normal[i] = 0.5
    for i in range(27,40):
        normal[i] = 0

# 车多
def make_much():
    for i in range(0,24):
        much[i] = 0
    for i in range(24,27):
        much[i] = 0.5
    for i in range(27,30):
        much[i] = 1
    for i in range(30,33):
        much[i] = 0.7
    for i in range(33,36):
        much[i] = 0.2
    for i in range(36,40):
        much[i] = 0

# 车较多
def make_more():
    for i in range(0,27):
        more[i] = 0
    for i in range(27,30):
        more[i] = 0.7
    for i in range(30,33):
        more[i] = 1
    for i in range(33,36):
        more[i] = 0.7
    for i in range(36,40):
        more[i] = 0.2

# 车很多
def make_most():
    for i in range(0, 27):
        most[i] = 0
    for i in range(27, 30):
        most[i] = 0.1
    for i in range(30, 33):
        most[i] = 0.4
    for i in range(33, 36):
        most[i] = 0.8
    for i in range(36, 40):
        most[i] = 1


smallest = [0 for i in range(60)]
smaller = [0 for i in range(60)]
small = [0 for i in range(60)]
big = [0 for i in range(60)]
bigger = [0 for i in range(60)]
biggest = [0 for i in range(60)]
light_time = []

# 变化幅度很小
def make_smallest():
    for i in range(0, 5):
        smallest[i] = 1
    for i in range(5, 10):
        smallest[i] = 0.8
    for i in range(10, 15):
        smallest[i] = 0.4
    for i in range(15, 20):
        smallest[i] = 0.1
    for i in range(20, 60):
        smallest[i] = 0

# 变化幅度较小
def make_smaller():
    for i in range(0, 5):
        smaller[i] = 0
    for i in range(5, 10):
        smaller[i] = 0.2
    for i in range(10, 15):
        smaller[i] = 0.7
    for i in range(15, 20):
        smaller[i] = 1
    for i in range(20, 25):
        smaller[i] = 0.7
    for i in range(25, 30):
        smaller[i] = 0.2
    for i in range(30, 60):
        smaller[i] = 0

# 变化幅度小
def make_small():
    for i in range(0, 20):
        small[i] = 0
    for i in range(20, 25):
        small[i] = 0.5
    for i in range(25, 30):
        small[i] = 1
    for i in range(30, 35):
        small[i] = 0.5
    for i in range(35, 60):
        small[i] = 0

# 变化幅度大
def make_big():
    for i in range(0, 25):
        big[i] = 0
    for i in range(25, 30):
        big[i] = 0.5
    for i in range(30, 35):
        big[i] = 1
    for i in range(35, 40):
        big[i] = 0.5
    for i in range(40, 60):
        big[i] = 0

# 变化幅度较大
def make_bigger():
    for i in range(0, 30):
        bigger[i] = 0
    for i in range(30, 35):
        bigger[i] = 0.2
    for i in range(35, 40):
        bigger[i] = 0.7
    for i in range(40, 45):
        bigger[i] = 1
    for i in range(45, 50):
        bigger[i] = 0.7
    for i in range(50, 55):
        bigger[i] = 0.2
    for i in range(55, 60):
        bigger[i] = 0

# 变化幅度很大
def make_biggest():
    for i in range(0, 40):
        biggest[i] = 0
    for i in range(40, 45):
        biggest[i] = 0.1
    for i in range(45, 50):
        biggest[i] = 0.4
    for i in range(50, 55):
        biggest[i] = 0.8
    for i in range(55, 60):
        biggest[i] = 1

fuzzy_matrix = [[0 for i in range(10)] for j in range(10)]

def make_car_num():
    car_num.append(least)
    car_num.append(less)
    car_num.append(little)
    car_num.append(normal)
    car_num.append(much)
    car_num.append(more)
    car_num.append(most)

def make_light_time():
    light_time.append(smallest)
    light_time.append(smaller)
    light_time.append(small)
    light_time.append(big)
    light_time.append(bigger)
    light_time.append(biggest)

def jiaoji(num1 , num2):
    if(num1 >= num2 ):
        return num2
    else:
        return num1

def huoji(num1 , num2):
    if(num1 >= num2):
        return num1
    else:
        return num2

# 计算一个模糊矩阵
def make_fuzzy_matrix(index1 , index2 , index3):

    now_cars1 = car_num[index1]
    last_cars1 = car_num[index2]
    change_time1 = light_time[index3]
    # print(light_time)

    now_cars = []
    last_cars = []
    change_time = []

    # 取离散的十个点用于计算模糊矩阵
    for i in range(0, 40 ,4):
        now_cars.append(now_cars1[i])
    for i in range(0, 40 ,4):
        last_cars.append(last_cars1[i])
    for j in range(0, 60 , 6):
        change_time.append(change_time1[j])

    # print(now_cars , last_cars , change_time)
    for i in range(10):
        for j in range(10):
            temp1 = jiaoji(now_cars[i] , last_cars[i])
            temp2 = 1 - temp1
            temp2 = (int(temp2*10) / 10)
            temp3 = jiaoji(temp1 , change_time[j])

            fuzzy_matrix[i][j] = huoji(temp3 , temp2)
            # print(i, j, temp1, temp2, temp3)
            # 每个模糊矩阵表有很多项，每项行，列，值分别为i j value，插入表中即可
            s = '\t 添加信息，i为行数，j为列数，value为值 \n'
            context.append(s)

    return fuzzy_matrix

# 计算全部知识的模糊矩阵
def caculate_matrix():

    count = 0

    for i in range(len(car_num)):
        for j in range(len(car_num)):
            if( i == j):
                continue
            else:
                k = abs(i - j)
                ma = make_fuzzy_matrix(i , j , k-1)
                count += 1
                print(ma)

                # 每一个模糊矩阵都是一个表，可以就命名为matrix+ij
                s = '\tCREATE TABLE matrix{}{} ( 属性XXX ) \n'.format(i,j)
                context.append(s)
    print(count)

if __name__ == '__main__':
    make_least()
    make_less()
    make_little()
    make_normal()
    make_much()
    make_more()
    make_most()

    make_smallest()
    make_smaller()
    make_small()
    make_big()
    make_bigger()
    make_biggest()

    make_car_num()
    make_light_time()

    # make_fuzzy_matrix(0 , 1 , 0)
    caculate_matrix()


