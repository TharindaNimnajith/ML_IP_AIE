#Default Argument Type Functions

def func(a = 0, b = 0, c = 'N', d = 'EMPTY'):
    print(a, b, c, d)

func(d = 10, a = 20.56, b = 'X')
func()
func(10, 20, 30)

#No need to pass values for all the parameters
#The default value is used for the parameters which don't have values been passed
