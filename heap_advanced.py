
"""
Advanced Heap Implementations in Python
Includes: heap creation, heapify, min/max heap checks, heap sort, merging heaps.
Academic implementation from Data Structures coursework.
"""
class Array():
    def __init__(self,size,value=None):
        self.size=size
        self.items = list()
        self.items = [None]*size
        self.type = list 
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __iter__(self):
        return iter(self.items)
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, newValue):
            if type(newValue) == self.type:
                self.items[index] = newValue
            else:
                print(f"ERROR!{newValue} is not of type{self.type}!")

def creat_heap(fh,heap):
    i=0
    for lines in fh:
        line=lines.strip().split(',')
        line[2]=int(line[2])
        heap[i]=line
        i+=1
    last_index=i-1
    last_parent_index=(last_index-1)//2
    for k in range(last_parent_index,-1,-1):
        heapify(heap,k,last_index)
    return i
def heapify(heap,parent_index,last_index):
    if parent_index>(last_index-1)//2:
        return
    else:
        right_index=(parent_index*2)+2
        left_index=(parent_index*2)+1
        if right_index>last_index:
            largets_index=find_index_max(heap,parent_index,left_index)
        else:
            largets_index=find_index_max(heap,right_index,left_index)
            largets_index=find_index_max(heap,parent_index,largets_index)
        if largets_index!=parent_index:
            heap[parent_index],heap[largets_index]=heap[largets_index],heap[parent_index]
            heapify(heap,largets_index,last_index)
def find_max(heap,index1,index2):
    if heap[index1][2]>heap[index2][2]:
        return index1
    else:
        return index2
def find_min(heap,index1,index2):
    if heap[index1][2]<heap[index2][2]:
        return index1
    else:
        return index2
def add_student(heap,n_students,target):
    if heap.size<n_students+1:
        return 
    last_index=n_students-1
    n_students+=1
    target_index=last_index+1
    heap[target_index]=target
    while target_index>0 and heap[target_index][2]>heap[((target_index-1)//2)][2]:
        heap[target_index],heap[(target_index-1)//2]=heap[(target_index-1)//2],heap[target_index]
        target_index=(target_index-1)//2
    return n_students
def is_min_heap(heap,n_students):
    if heap[0]==None:
        return True
    last_index=n_students-1
    last_parent=(last_index-1)//2
    for parent_indexes in range(last_parent,-1,-1):
        if (parent_indexes*2)+2>last_index:
            smallest_index=find_min(heap,(parent_indexes*2)+1,parent_indexes)
            if smallest_index!=parent_indexes:
                return False
        else:
            smallest_index=find_min(heap,(parent_indexes*2)+1,(parent_indexes*2)+2)
            smallest_index=find_min(heap,smallest_index,parent_indexes)
            if smallest_index!=parent_indexes:
                return False
    return True
def is_max_heap(heap,n_students):
    if heap[0]==None:
        return True
    last_index=n_students-1
    last_parent=(last_index-1)//2
    for parent_indexes in range(last_parent,-1,-1):
        if (parent_indexes*2)+2>last_index:
            largest_index=find_max(heap,(parent_indexes*2)+1,parent_indexes)
            if largest_index!=parent_indexes:
                return False
        else:
            largest_index=find_max(heap,(parent_indexes*2)+1,(parent_indexes*2)+2)
            largest_index=find_max(heap,largest_index,parent_indexes)
            if largest_index!=parent_indexes:
                return False
    return True
def is_empty(heap):
    if heap[0]==None:
        return True
    else:
        return False
def peek(heap):
    if heap[0]==None:
        return None
    else:
        return heap[0]
def serve_urgent(heap,n_students):
    if heap[0]==None:
        return None
    else:
        n_students-=1
        served=heap[0]
        heap[0]=heap[n_students-1]
        heapify(heap,0,n_students-1)
        return served,n_students
def heap_sort(heap,n_students):
    if heap[0]==None:
        return
    heap2=Array(n_students)
    for i in range(n_students):
        heap2[i]=heap[i]
    while n_students!=0:
        served,n_students=serve_urgent(heap,n_students)
        print(served,end='')
def print_heap(heap,N):
    
    for i in range(N):
        print("\n\t\t",heap[i])
        print("\n\t\t----------------")
def merge_heaps(H1, n1, H2, n2):
    for i in range(n2):
        n1 = add_student(H1, n1, H2[i])
    return n1          
