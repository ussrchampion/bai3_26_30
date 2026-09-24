w = [-2, 1, 0]
x = [2, 3, 1]
y = 1

wtx = w[0]*x[0] + w[1]*x[1] + w[2]*x[2]
pred = 1 if wtx >= 0 else -1
print("1. bi sai:", pred != y)

if pred != y:
    w = [w[0] + y*x[0], w[1] + y*x[1], w[2] + y*x[2]]
    wtx2 = w[0]*x[0] + w[1]*x[1] + w[2]*x[2]
    print("2. w moi:", w)
    print("3. wTx moi:", wtx2)
