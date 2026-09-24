class Perceptron:
    def fit(self, x, y, lr=0.01, ep=100):
        self.w = [0.0] * len(x[0])
        self.b = 0.0
        for _ in range(ep):
            for i in range(len(x)):
                val = sum(x[i][j] * self.w[j] for j in range(len(self.w))) + self.b
                pred = 1 if val >= 0 else -1
                yi = 1 if y[i] == 1 else -1
                if pred != yi:
                    for j in range(len(self.w)):
                        self.w[j] += lr * yi * x[i][j]
                    self.b += lr * yi

    def predict(self, x):
        res = []
        for xi in x:
            val = sum(xi[j] * self.w[j] for j in range(len(self.w))) + self.b
            res.append(1 if val >= 0 else 0)
        return res

xtr = [
    [2, 0], [5, 1], [3, 0], [1, 1], [4, 0],
    [50, 4], [80, 5], [70, 3], [90, 6], [100, 5]
]
ytr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

xts = [
    [3, 1], [2, 0], [60, 4], [85, 5]
]
yts = [0, 0, 1, 1]

m = Perceptron()
m.fit(xtr, ytr)

pred = m.predict(xts)

tp = sum(1 for p, y in zip(pred, yts) if p == 1 and y == 1)
fp = sum(1 for p, y in zip(pred, yts) if p == 1 and y == 0)
fn = sum(1 for p, y in zip(pred, yts) if p == 0 and y == 1)
tn = sum(1 for p, y in zip(pred, yts) if p == 0 and y == 0)

acc = (tp + tn) / len(yts)
pre = tp / (tp + fp) if tp + fp > 0 else 0
rec = tp / (tp + fn) if tp + fn > 0 else 0
f1 = 2 * pre * rec / (pre + rec) if pre + rec > 0 else 0

print("acc:", acc)
print("pre:", pre)
print("rec:", rec)
print("f1 :", f1)
