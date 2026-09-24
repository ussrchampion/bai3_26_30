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
