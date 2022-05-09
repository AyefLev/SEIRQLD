import matplotlib.pyplot as plt
from manimlib import *


class wffc(Scene):
    def construct(self):
        tex1 = Tex(
            r"\frac{\mathrm{d}S}{\mathrm{d}t} = -\frac{S(Ib_1r_1+Eb_2r_2)}{N}+oR"
        )
        tex2 = Tex(
            r"\frac{\mathrm{d}E}{\mathrm{d}t} = \frac{S(Ib_1r_1+Eb_2r_2)}{N}-Es_1-E(1-s_1)a"
        )
        tex3 = Tex(
            r"\frac{\mathrm{d}I}{\mathrm{d}t} = E(1-s_1)a-Is_2-IK(1-s_2)"
        )
        tex4 = Tex(
            r"\frac{\mathrm{d}R}{\mathrm{d}t} = IK(1-s_2)Y_1+LKY_2-oR"
        )
        tex5 = Tex(
            r"\frac{\mathrm{d}Q}{\mathrm{d}t} = Es_1-aQ"
        )
        tex6 = Tex(
            r"\frac{\mathrm{d}L}{\mathrm{d}t} = aQ+Is_2-LK"
        )
        tex7 = Tex(
            r"\frac{\mathrm{d}D}{\mathrm{d}t} = IK(1-s_2)d_1+LKd_2"
        )
        G = VGroup(tex1, tex2, tex3, tex4, tex5, tex6, tex7).arrange(DOWN, buff=0.4)
        self.add(G)


# if __name__ == "__main__":
#   system("manimgl X.py wffc")

r1 = 120
r2 = 120
b1 = 0.01
b2 = 0.005
a = 0.1
s1 = 0
s2 = 0
Y1 = 0.970
Y2 = 0.975
d1 = 1 - Y1
d2 = 1 - Y2
K = 0.05
o = 0.005

T = 150
N = 10000
E = [0] * T
I = [2] * T
S = [N - I[0]] * T
R = [0] * T
Q = [0] * T
L = [0] * T
D = [0] * T

DKZ = False  # 是否开始戴口罩
XS = False  # 是否停止线下教学
GL = False  # 是否启用核酸检测及隔离措施

for i in range(T - 1):
    if i % 7 >= 1 or i % 7 <= 5:  # 上课
        r1 = 120
        r2 = 120
    elif i % 7 == 5 or i % 7 == 0:  # 不上课
        r1 = 40
        r2 = 40

    if i >9 :
        if XS:
            r1 = 30
            r2 = 30
        if DKZ:
            b1 = 0.005
            b2 = 0.0025
        if GL:
            s1 = 0.05
            s2 = 0.05

    S[i + 1] = S[i] - (r1 * b1 * I[i] + r2 * b2 * E[i]) * S[i] / N + o * R[i]
    E[i + 1] = E[i] + (r1 * b1 * I[i] + r2 * b2 * E[i]) * S[i] / N - a * E[i] * (1 - s1) - E[i] * s1
    I[i + 1] = I[i] + a * E[i] * (1 - s1) - I[i] * s2 - I[i] * K * (1 - s2)
    R[i + 1] = R[i] + I[i] * K * (1 - s2) * Y1 + L[i] * K * Y2 - o * R[i]
    Q[i + 1] = Q[i] + E[i] * s1 - a * Q[i]
    L[i + 1] = L[i] + a * Q[i] + I[i] * s2 - L[i] * K
    D[i + 1] = D[i] + I[i] * K * (1 - s2) * d1 + L[i] * K * d2

fig, ax = plt.subplots(1)
ax.plot(S, label='S')
ax.plot(E, label='E')
ax.plot(I, label='I')
ax.plot(R, label='R')
ax.plot(Q, label='Q')
ax.plot(L, label='L')
ax.plot(D, label='D')
ax.legend()
#plt.savefig("1")
plt.show()
