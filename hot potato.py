# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:42:25 2017

@author: U002ZXJ
"""
import Queue


def hot_potato(name_list, num):
    sim_q = Queue.Queue()
    for name in name_list:
        sim_q.enqueue(name)
    while sim_q.size()>1:
        for i in range(num):
            sim_q.enqueue(sim_q.dequeue())
        sim_q.dequeue()
    return sim_q.dequeue()
        