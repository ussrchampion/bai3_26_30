def f(x):
    return x*x - 4*x + 5

def df(x):
    return 2*x - 4

x = 5.0
lr = 0.2

for i in range(4):
    grad = df(x)
    x = x - lr * grad
    print("buoc", i + 1, ": f' =", round(grad, 4), ", x =", round(x, 4), ", f(x) =", round(f(x), 4))

print("nx: x tien dan ve 2, ham so giam ve 1 nen thuat toan hoi tu")
