# 프로그래머스 No.42627 디스크 컨트롤러
from queue import PriorityQueue

def calc_answer_time(time, answer, ready_start, ready_task):
  if time > ready_start:
    time += ready_task
    answer += abs(time - ready_start)
  else:
    time = ready_task + ready_start
    answer += ready_task
  return [answer, time]

def SJFS(jobs):
  time, answer = jobs[0][0], 0
    
  ready_queue = PriorityQueue()
  for start, task in jobs:
    if start <= time:
      ready_queue.put((task, start))
    else:
      while start > time and not ready_queue.empty():
        ready_task, ready_start = ready_queue.get()
        answer, time = calc_answer_time(time, answer, ready_start, ready_task)
      ready_queue.put((task, start))

  while not ready_queue.empty():
    ready_task, ready_start = ready_queue.get()
    answer, time = calc_answer_time(time, answer, ready_start, ready_task)
  return answer

def solution(jobs):
  sorted_jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
  return SJFS(sorted_jobs) // len(jobs)

jobs = [[0,1],[100,2],[200,3],[300,4]]
print(solution(jobs))