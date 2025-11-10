x = 5

def outer():
    x = 10
    def inner():
        print(x)
    try:
        inner()
    except UnboundLocalError as e:
        print("Error:", e)
    print("outer x:", x)

outer()
print("global x:", x)