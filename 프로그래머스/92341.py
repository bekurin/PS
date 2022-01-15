# 프로그래머스 No.92341 주차 요금 계산
"""
1. record를 공백을 기준으로 분리한다.
2. car_id를 key로 check_time을 value로 car_dict에 저장한다.
3. car_dict를 순환한다. value 배열의 길이가 2보다 작은지 확인한다.
4. 3의 결과가 참이라면 in_time = value.pop(0), out_time = "23:59"로 설정한다.
5. 3의 결과가 거짓이라면 in_time, out_time을 value.pop(0)로 설정한다.
6. in_time과 out_time을 기준으로 주차 요금을 계산하여 answer_dict에 주차 요금을 저장해준다.
7. answer_dict.items를 저장해주고, 주차 요금만 결과로 반환한다.
"""
import math
import datetime

def sub_time(in_time: str, out_time: str) -> int:
  time_format = "%H:%M"
  in_time = datetime.datetime.strptime(in_time, time_format)
  out_time = datetime.datetime.strptime(out_time, time_format)
  return (out_time - in_time).seconds // 60

def calc_fees(value: int, fees: list) -> int:
  if value <= fees[0]:
    return fees[1]
  else:
    return int(fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3])

def get_calc_fees_by(values: list, fees: list) -> int:
  minute = 0
  while values:
    out_time = "23:59"
    in_time = values.popleft()
    if values:
      out_time = values.popleft()
    minute += sub_time(in_time, out_time)
  return calc_fees(minute, fees)

def solution(fees: list, records: list) -> list:
  answer_dict = {}
  car_dict = {}
  records = [record.split() for record in records]

  for check_time, car_id, _ in records:
    if car_id in car_dict:
      car_dict[car_id].append(check_time)
    else:
      answer_dict[car_id] = 0
      car_dict[car_id] = []

  for key, values in car_dict.items():
    answer_dict[key] = get_calc_fees_by(values, fees)
  
  return [item[-1] for item in sorted(answer_dict.items())]

# 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))