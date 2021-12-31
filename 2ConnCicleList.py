class Node:
    def __init__(self, value, next_ptr=None, prev_ptr=None):
        self.value = value
        self.next_ptr = next_ptr
        self.prev_ptr = prev_ptr

    def set_value(self, value):
        self.value = value

    def set_next_ptr(self, next_ptr):
        self.next_ptr = next_ptr


class CycleList:
    def __init__(self, head):
        self.head = head
        # self.tail=head
        if self.head is not None:
            self.len = 1
            self.tail = self[0]
            self.head.next_ptr = self.tail
            self.tail.next_ptr = self.head
            self.head.prev_ptr = self.tail
            self.tail.prev_ptr = self.head
        else:
            self.len = 0

    def __len__(self):
        return self.len

    def append(self, value):
        if len(self) == 0:
            self.head = Node(value)
            self.tail = self.head
            self.len += 1
            self.head.next_ptr = self.tail
            self.head.prev_ptr = self.tail
            self.tail.prev_ptr = self.head
            self.tail.next_ptr = self.head

        elif len(s) == 1:
            self.tail = Node(value)
            self.head.next_ptr = self.tail
            self.tail.next_ptr = self.head
            self.head.prev_ptr = self.tail
            self.tail.prev_ptr = self.head
            self.len += 1
        else:
            self[len(self) - 1].next_ptr = Node(value)
            self.len += 1
            self.tail = self[len(self) - 1]
            self.tail.next_ptr = self.head
            self.tail.prev_ptr = self[len(self) - 2]
            self[len(self) - 2].next_ptr = self.tail
            self.head.prev_ptr = self.tail

    def pop_last(self):
        if len(self) > 1:
            self.tail = self[len(self) - 2]
            self.tail.next_ptr = self.head
            self.head.prev_ptr = self.tail
            self.len -= 1
        elif len(self) == 1:
            self.head = None
            self.len -= 1
        else:
            raise KeyError()

    def pop_2_last(self):
        if len(self) > 2:
            self.pop_last()
            self.pop_last()
            self.len -= 2


        elif len(self) == 2:
            self.head = None
            self.len = 0
        else:
            raise KeyError

    def pop_first(self):
        if len(self) > 0:
            self.head = self.head.next_ptr
            self.len -= 1
            self.tail.next_ptr = self.head
            self[len(self) - 2].next_ptr = self.tail
            self.head.prev_ptr = self.tail
            self.tail.prev_ptr = self[len(self) - 2]
        elif len(self) == 1:
            self.head = None
        else:
            raise KeyError()

    def prepend(self, value):
        if len(self) == 0:
            self.head = Node(value)
            self.tail = self.head
            self.len += 1
            self.head.next_ptr = self.tail
            self.head.prev_ptr = self.tail
            self.tail.prev_ptr = self.head
            self.tail.next_ptr = self.head
            return
        node = Node(value, self.head)
        self.head = node
        self.head.next_ptr.prev_ptr = self.head
        self.len += 1
        self[len(self) - 2].next_ptr = self.tail
        self.tail = self[len(self) - 1]
        self.tail.prev_ptr = self[len(self) - 2]
        self.tail.next_ptr = self.head
        self.head.prev_ptr = self.tail

    def delete_2_first(self):
        if len(self) > 2:
            self.pop_first()
            self.pop_first()
        elif len(self) == 2:
            self.head = None
            self.len = 0
        else:
            self.head = None
            self.len = 0

    def del_by_ind(self, index):
        if index == 0:
            self.pop_first()
        elif index == len(self) - 1:
            self.pop_last()
        else:
            temp = self.__getitem__(index - 1)
            temp.next_ptr = self.__getitem__(index + 1)
            temp.next_ptr.prev_ptr=temp
            self.len-=1


    def insert(self, value, index):
        if index == 0:
            self.prepend(value)

        elif index == len(self):
            self.append(value)
        else:
            temp = self.__getitem__(index - 1)
            temp.next_ptr = Node(value, temp.next_ptr, temp)
            self.len += 1

    def __getitem__(self, index):
        i = 0
        temp = self.head
        while i < index and temp.next_ptr != self.head:
            temp = temp.next_ptr
            i += 1

        if i == index:
            return temp
        else:
            raise KeyError()

    def print_list(self):
        temp = self.head
        while temp != self.tail:
            print(temp.value)
            temp = temp.next_ptr
        print(self.tail.value)

    def indexy(self, elem):
        index = 0
        if self.head.value == elem:
            return 0
        else:
            for i in range(len(s)):
                if s[i].value == elem:
                    return index
                index += 1
        return -1

    def find_2_equal(self):
        for i in range(len(self)):
            for j in range(len(self)):
                if i!=j and self[i].value==self[j].value:
                    return self[i].value
        return -1

    def post_to_beg_neg(self):
        chet=0
        templ=len(self)
        for i in range(templ):
            if self[i].value<0:
                temp=self[i]
                self.del_by_ind(i)
                self.prepend(temp.value)
                chet+=1
        return chet


def Maxy(s):
    if len(s) == 1:
        return s.head.value
    elif len(s) == 0:
        raise KeyError()
    else:
        max = s.head.value
        for i in range(1, len(s)):
            if s[i].value > max:
                max = s[i].value
        return max


# 2. Добавить в список L1 за первым вхождением элемента Е все элементы списка L2, вернуть длину нового списка.

def Add_l2_after_e(l1, l2, e):
    tempind = l1.indexy(e)
    print(tempind,"темпинд")
    if tempind == -1:
        raise KeyError()
    else:
        for i in range(len(l2)):
            print(f"что {l2[i].value} куда {tempind+1+i}")
            l1.insert(l2[i].value, tempind + i + 1)
        return len(l1)


s = CycleList(Node(0))
s.append(1)
s.append(2)
s.append(3)
s.append(-4)
s.append(-5)
s.append(6)
s.append(7)
print(s.post_to_beg_neg(),"перенесено отриц")

print("-------перенос отриц------------")
s.print_list()
print("_____________________")


# b = CycleList(Node(10))
# b.append(11)
# b.append(12)


# Add_l2_after_e(s,b,3)
# s.print_list()
for i in range(len(s)):
    print(f"значение-{s[i].value}")
    print(f"следующее-{s[i].next_ptr.value}")
    print(f"предыдущее-{s[i].prev_ptr.value}")

# print("----------------------------")

print(s.find_2_equal(),"одинаковые")
