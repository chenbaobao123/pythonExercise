'''单链表的代码定义'''

class Node(object):
    '''单链表的节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self,node=None):
        '''指向头节点的head'''
        self._head = node
    def is_empty(self):
        ''' 链表是否为空'''
        return self._head == None
    def length(self):
        ''' 链表长度'''
        #创建cur指针(游标),使指针初始时指向头节点
        cur = self._head
        count = 0
        #尾节点的next指向None,当cur的next指向None则表示指向尾节点
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        ''' 遍历整个链表'''
        cur = self._head
        while cur != None:
            print(cur.elem,end=' ')
            print('')
            cur = cur.next
    def add(self,item):
        ''' 链表头部添加元素'''
        #先创建一个保存item值的节点
        node = Node(item)
        node.next = self._head
        self._head = node
    def append(self,item):
        ''' 链表尾部添加元素'''
        #先创建一个保存item值的节点
        node = Node(item)
        #先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        else:
        #若不为空，则找到尾部，将尾节点的next指向新节点
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self,pos,item):
        ''' 指定位置添加元素'''
        #若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        #若指定位置pos超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self._head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
    def remove(self,item):
        ''' 删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if pre == None:
                    #如果第一个就是删除的节点
                    self._head = cur.next
                else:
                    #将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    def search(self,item):
        ''' 查找节点是否存在'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False
if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2,4)
    ll.add(3)
    print('长度：',ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print('长度：',ll.length())
    ll.travel()
