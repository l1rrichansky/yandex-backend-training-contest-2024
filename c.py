
class Node:
    mas = {}

    def __init__(self, n, iter=1, p=None):
        self.parent = p
        self.value = iter
        if self.value == n:
            self.left = None
            self.right = None
        else:
            if self.value * 2 > n:
                self.left = None
            else:
                self.left = Node(n, self.value * 2, self)
            if self.value * 2 + 1 > n:
                self.right = None
            else:
                self.right = Node(n, (self.value * 2) + 1, self)
        self.mas[self.value] = self



    def change_elem(self, n):
        if self.value == n:
            if self.parent is None:
                pass
            else:
                if self.parent.right and self.parent.right.value == self.value:
                    [sv, sl, sp, spv, spl, s] = [self.value, self.left, self.parent, self.parent.value,
                                                 self.parent.left, self]
                    self.value = spv
                    self.parent.value = sv
                    self.left = spl
                    self.parent.left = sl
                    if self.left:
                        self.left.parent = s
                    if self.parent.left:
                        self.parent.left.parent = sp
                elif self.parent.left and self.parent.left.value == self.value:
                    [sv, sr, sp, spv, spr, s] = [self.value, self.right, self.parent, self.parent.value,
                                                 self.parent.right, self]
                    self.value = spv
                    self.parent.value = sv
                    self.right = spr
                    self.parent.right = sr
                    if self.right:
                        self.right.parent = s
                    if self.parent.right:
                        self.parent.right.parent = sp
                self.mas[self.value] = self
                self.mas[self.parent.value] = self.parent
        else:
            if self.left:
                self.left.change_elem(n)
            if self.right:
                self.right.change_elem(n)

    def lvr(self):
        global s
        if self.left:
            self.left.lvr()
        s.append(self.value)
        if self.right:
            self.right.lvr()


s = []

a = input().split()
nd = Node(int(a[0]))

for i in input().split():
    nd.mas[int(i)].change_elem(int(i))

nd.lvr()
print(*s)
