#coding:utf-8
#author:jay

#简易的KNN分类算法,point为待分类的元素,k为选取的最近距离的元素的个数,args为分类样本(投票的实体),此算法在类标边界比较整齐的情况下分类的准确率很高

from math import sqrt


class KNN(object):
    def __init__(self,point,k,*args):
        '''初始化:
            _seprepeatpoint:过滤掉重复点之后的所有点集合
        '''
        self._length = len(args)
        self._cates = [set(arg) for arg in args]
        self._point = point
        self._seprepeatpoint = set(reduce(lambda x,y:x+y,args))
        # self._other = (self._col1 - self._col2) | (self._col2 - self._col1)
        self.k = k

    def _coredistance(self,point1,point2):
        '''计算每个点与给定元素的距离,保留3位小数'''
        distance = sum(abs((point1[i]-point2[i]))+abs((point1[i]-point2[i])) for i in xrange(0,len(point1)-1))
        distance = round(sqrt(distance),3)
        return distance

    def _get_value(self,dic):
        if isinstance(dic,dict):
            return dic.values()[0]

    def _get_key(self,dic):
        if isinstance(dic,dict):
            return dic.keys()[0]

    def _get_cate(self,distancelist,k):
        meetspoints = distancelist[0:k]
        pointlist = [self._get_key(point) for point in meetspoints]
        count = [([point for point in pointlist if point in cate]) for cate in self._cates]
        return count
    
    def separate(self):
        '''返回分类结果'''
        # distance = [([{i:self._coredistance(i,self._point)} for i in cate]) for cate in self._cates]
        # distance = reduce(lambda x,y:x+y,distance)
        distance = [{i:self._coredistance(i,self._point)} for i in self._seprepeatpoint]
        newdistance = sorted(distance,key=self._get_value)
        return self._get_cate(newdistance,self.k)

if __name__ == '__main__':
    col1 = [(1, 7, 1), (2, 5, 1)]
    col2 = [(2, 5, 1), (5, 6, 1), (8, 8, 1)]
    col3 = [(5, 5, 6), (6, 6, 6), (8, 8, 2), (8, 8, 1)]
    point = (8,8,2)
    k = 3
    knn = KNN(point,k,col1,col2,col3)
    print knn.separate()