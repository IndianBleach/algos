
class basic_stack:
    def __init__(self):
        self.__cursor = 0
        self.__data = []
    
    def size(self):
        return self.__cursor
    
    def top(self):
        if (self.__cursor == 0):
            return None
        return self.__data[self.__cursor-1]

    def pop(self):
        if (self.__cursor > 0):
            t = self.__data.pop()
            self.__cursor -= 1
            return t
        else : return None

    def push(self, value):
        self.__data.append(value)
        self.__cursor += 1
        
    def reverse(self):
        st = basic_stack()
        cur = self.pop()

        while(cur != None):
            st.push(cur)
            cur = self.pop()

        return st
    
    def as_list(self):
        ls = []
        while(self.top() != None):
            ls.append(self.pop())
        
        rev = reversed(ls)
        for el in rev:
            self.push(el)

        return ls

    def sort_by_queue(self):
        q = basic_stack()
        r = basic_stack()
        count = self.size()
        while(count > 0):
            # 5 (4)
            el = self.pop()
            if (r.top() != None and r.top() < el):
                r.push(el)
            else:
                # 3 4 (2)
                while(r.top() != None and
                      r.top() >= el):
                    q.push(r.pop())

                r.push(el) 

                while(q.top() != None):
                    r.push(q.pop())
            
            count -= 1
        
        return r

    def sort_by_min(self):
        t = basic_stack()
        q = self
        ls = []
        while(q.top() != None):
            min = q.top()

            while(q.top() != None):
                cur = q.pop()
                t.push(cur)
                if (cur < min):
                    min = cur

            # there we have min elem in Q
            ls.append(min)
            while(t.top() != None):
                cur_el = t.pop()
                if (cur_el != min):
                    q.push(cur_el)

        return ls


t = basic_stack()
t.push(1)
t.push(6)
t.push(4)
t.push(3)
t.push(7)
t.push(2)


#st = t.sort()
print(t.sort_by_min())
