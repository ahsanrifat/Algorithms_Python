from typing import List
class MaxHeap:
    
    def __init__(self,input_list:List=[]):
        if not input_list:
            self.heapified_dict={}
        else:
            self.heapified_dict=self.hepify_list(input_list)
            
    def get_left_child_index(self,child_index):
        return (2*child_index)+1
    
    def get_right_child_index(self,parent_index):
        return (2*parent_index)+2
    
    def get_parent_index(self,parent_index):
        return (parent_index-1)//2
    
    def hepify_list(self,input_list:List):
        self.heapified_dict={}
        for i in input_list:
            self.insert(i)
        return self.get_heap()
    
    def swap(self,ind1,ind2):
        temp=self.heapified_dict[ind1]
        self.heapified_dict[ind1]=self.heapified_dict[ind2]
        self.heapified_dict[ind2]=temp
    
    def heapify_down(self):
        index=0
        left_index=self.get_left_child_index(index)
        right_index=self.get_right_child_index(index)
        smaller_index=None
        while self.heapified_dict.get(left_index):
            if self.heapified_dict.get(left_index)>self.heapified_dict.get(index):
                smaller_index=left_index
            if self.heapified_dict.get(right_index):
                if self.heapified_dict.get(right_index)>self.heapified_dict.get(index):
                    if self.heapified_dict.get(left_index)<self.heapified_dict.get(right_index):
                        smaller_index=right_index
            if not smaller_index:
                break
            else:
                self.swap(index,smaller_index)
                index=smaller_index 
                left_index=self.get_left_child_index(index)
                right_index=self.get_right_child_index(index)
                smaller_index=None
        
    
    def pop(self):
        val=self.heapified_dict.get(0)
        if val:
            self.swap(0,len(self.heapified_dict)-1)
            del self.heapified_dict[len(self.heapified_dict)-1]
            self.heapify_down()
        return val
    
    def hepify(self):
        # keep hepifying until the parent exists and parent is smaller than the child
        current_index=len(self.heapified_dict)-1
        parent_index=self.get_parent_index(current_index)
        while self.heapified_dict.get(parent_index) and (self.heapified_dict.get(parent_index)<self.heapified_dict.get(current_index)):
            self.swap(parent_index,current_index)
            current_index=parent_index
            parent_index=self.get_parent_index(current_index)
    
    def insert(self,val):
        if len(self.heapified_dict)==0:
            # its an empty heap 
            self.heapified_dict[0]=val
        else:
            self.heapified_dict[len(self.heapified_dict)]=val
        self.hepify()
    
    def get_heap(self):
        return [self.heapified_dict[key] for key in self.heapified_dict]
            