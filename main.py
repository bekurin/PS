# 프로그래머스 No.42627 디스크 컨트롤러
from queue import PriorityQueue

def SJFS(jobs):
  start, task = 0, 0
  time, answer = 0, 0
    
  ready_queue = PriorityQueue()
  for start, task in jobs:
    if time >= start:
      print("[1] put ready_queue task = {}, start = {}".format(task, start))
      ready_queue.put((task, start))
    else:
      # not proccessed start, task is remain
      while start >= time and not ready_queue.empty():
        ready_task, ready_start = ready_queue.get()
        print("[2] get ready_queue task = {}, start = {}".format(ready_task, ready_start))
        
        time += ready_task
        answer += abs(time - ready_start)
        print("[3] change time = {}, answer = {}".format(time, answer))
        
      if not ready_queue.empty():
        if ready_start < time:
          time += ready_task
          answer += abs(time - ready_start)
          print("[4] change time = {}, answer = {}".format(time, answer))
      else:
          time = ready_task + ready_start
          answer += ready_task
          print("[5] change time = {}, answer = {}".format(time, answer))
  return answer + task

def solution(jobs):
  sorted_jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
  return SJFS(sorted_jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))