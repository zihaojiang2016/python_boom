# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:48:23 2017

@author: U002ZXJ
"""

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None
            
    def busy(self):
        return self.current_task != None
    
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages()*60/self.page_rate

import random, Queue                                               
class Task:
    def __init__(self,time) :
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def get_stamp(self):
        return self.timestamp
    
    def get_pages(self):
        return self.pages
    
    def wait_time(self,current_time):
        return current_time - self.timestamp
    

def new_print_task():
    num = random.randrange(1,181)
    return num == 180


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue.Queue()
    waiting_time = []
    
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_time.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        
        lab_printer.tick()
    average_wait = sum(waiting_time)/len(waiting_time)
    return average_wait                    
        
    
    
    
    
    
    
    