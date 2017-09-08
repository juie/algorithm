#coding:utf-8
#author:jay

from math import sqrt
# import sys
# import numpy as np
# import pylab as pl


class KNN(object):
    def __init__(self,cate1,cate2,point,k):
        self._col1 = set(cate1)
        self._col2 = set(cate2)
        self._point = point
        self._repeatpoint = self._col1 & self._col2
        self._other = (self._col1 - self._col2) | (self._col2 - self._col1)
        self.k = k

    def _coredistance(self,point1,point2):
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
        col1count = [point for point in pointlist if point in self._col1]
        col2count = [point for point in pointlist if point in self._col2]
        return col1count,col2count
    
    def separate(self):
        distance = [{i:self._coredistance(i,self._point)} for i in self._other] + [{i:self._coredistance(i,self._point)} for i in self._repeatpoint]
        newdistance = sorted(distance,key=self._get_value)
        return self._get_cate(newdistance,self.k)

if __name__ == '__main__':
    col1 = [(1, 7, 1), (2, 5, 1)]
    col2 = [(2, 5, 1), (5, 6, 1), (8, 8, 1)]
    point = (8,8,2)
    k = 1
    knn = KNN(col1,col2,point,k)
    print knn.separate()
    # pl.plot(col1[0],col1[1],'or')
    # pl.plot(col2[0],col2[1],'ob')
    # pl.plot(point[0],point[1],'og')
    # pl.show()

