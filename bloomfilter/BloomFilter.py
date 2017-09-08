#coding:utf-8
#author:jay

from mmh3 import hash
from bitarray import bitarray

#简易布隆过滤器,采用mmh3算法进行哈希(速度快,且均匀)

class BloomFilter(object):
    def __init__(self,BIT_SIZE=5000000):
        #初始化过滤器
        self.bit_size = BIT_SIZE
        self.bit_array = bitarray(self.bit_size)

    def slotlist(self,element):
        #获取哈希过后的哈希值列表
        element = str(element)
        slot1 = hash(element, 41) % self.bit_size
        slot2 = hash(element, 41) % self.bit_size
        slot3 = hash(element, 41) % self.bit_size
        slot4 = hash(element, 41) % self.bit_size
        slot5 = hash(element, 41) % self.bit_size
        slot6 = hash(element, 41) % self.bit_size
        slot7 = hash(element, 41) % self.bit_size
        return [slot1,slot2,slot3,slot4,slot5,slot6,slot7]
    
    def getpostion(self,arr1,arr2):
        return [arr2[i] for i in arr1]

    def add_one(self,element):
        #向过滤器里面添加一个元素
        try:
            slotarry = self.slotlist(element)
            for slot in slotarry:
                self.bit_array[slot] = 1
            return True
        except Exception as e:
            raise e
            return False

    def add_many(self,elearr):
        #向过滤器里添加一组元素
        for ele in elearr:
            self.add_one(ele)
        return True
        
    def query(self,element):
        #查询
        slotarry = self.slotlist(element)
        if 0 in self.getpostion(slotarry,self.bit_array):
            return False
        else:
            return True

if __name__ == '__main__':
    boolfilter = BloomFilter()
    boolfilter.add_many(range(0,10000,2))
    print boolfilter.query(3)
    print boolfilter.query(1000)
    print boolfilter.query(1051)