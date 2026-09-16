

fruits=['apple','orange','pear']
count=[10,3,4]
for f,c in zip(fruits,count):
    match f,c:
        case 'apple',10:
            print('10个apple')
        case 'orange',3:
            print('3个orange')
        case 'pear',4:
            print('4个pear')