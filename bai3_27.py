w = [1, 2, -10]
x = [3, 4, 1]
y = -1

wtx = w[0]*x[0] + w[1]*x[1] + w[2]*x[2]
pred = 1 if wtx >= 0 else -1

print("1. wTx =", wtx)
print("2. y_pred =", pred)
print("3. sai khong:", pred != y)
