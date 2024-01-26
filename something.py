def func(a, b, c,*, d=6,  **kwargs):
    print(a, b, c, d, args, kwargs)

if __name__ == '__main__':
    func(1,2,3,5,6,7,7,  r=4, q="Hallo")
