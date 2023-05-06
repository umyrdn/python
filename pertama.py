class Goldar:
    def __init__(self, darah):
        self.darah = darah

    def cek_goldar(self):
        goldar = ["a", "b", "o", "ab"]
        if self.darah in goldar:
            print(self.darah, "termasuk golongan darah manusia")
        else:
            print(self.darah, "tidak termasuk golongan darah manusia")

#x = Goldar("masukkan huruf goldar")
x = Goldar("a")
x.cek_goldar()
