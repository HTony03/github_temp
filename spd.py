import matplotlib.pyplot as plt
import matplotlib.colors as colors


def calc(name, p, a0, m, pos1, pos2, col, ifa=0):
    vm = 0
    vkm = 0
    s = 0
    tc = 0.1
    vl = []
    sl = []
    al = []
    tl = []
    vs1 = []
    vs2 = []
    t0 = 0
    while vkm < 200:
        pa = p * vkm / 170 if vkm <= 170 else p
        if vkm == 0:
            a = a0 / 3.6
        elif 0 < vkm < pos1:
            a = pa * 0.4 / (m * vm)
        elif pos1 <= vkm < pos2:
            a = pa * 0.6 / (m * vm)
        elif vkm >= pos2:
            a = pa * 1 / (m * vm)

        s += vm * tc + 1 / 2 * a * tc ** 2
        vm += a * tc
        vkm = vm * 3.6
        print("vkm:%s s:%s a：%s" % (vkm, s, a), end="\n")
        vl.append(vkm)
        sl.append(s)
        al.append(a)
        vs1.append(pos1)
        vs2.append(pos2)
        t0 += tc
        tl.append(t0)

    plt.plot(sl, vl, c=col, label=name)
    if ifa == 1:
        plt.plot(sl, vs1, c="r", lw=0.3, label=" pwr cnge 1")
        plt.plot(sl, vs2, c="r", lw=0.3, label=" pwr cnge 2")


"""https://www.china-emu.cn/Trains/ALL/"""

"""






"""
if __name__ == "__main__":
    pass

#####
calc("CRH380A", 9120, 1.4, 430, 80, 120, colors.to_rgb((0, 0.3, 150 / 255)))
calc("CRH380B", 9200, 1.44, 480, 80, 120, colors.to_rgb((0, 0.3, 250 / 255)))
calc("CRH2A", 4560, 1.296, 400, 80, 120, colors.to_rgb((0, 0, 150 / 255)))
calc("CR200J-1", 5600, 1.26, 608, 80, 120, colors.to_rgb((0, 0, 250 / 255)), 1)
plt.title("spd line")
plt.legend(loc='lower right')
plt.show()
