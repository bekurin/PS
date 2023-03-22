# 프로그래머스 No.155651 호텔 대실
minute_for_one_day = 1440


def get_hour_to_minutes(time):
  hour, minute = list(map(int, time.split(":")))
  return hour * 60 + minute


def fill_reservation_time_to(rooms, reservation_time):
  start, end = reservation_time
  for idx in range(start, end + 10 if end + 10 < minute_for_one_day else end):
    rooms[idx] += 1
  return rooms


def solution(book_time):
  rooms = [0 for _ in range(minute_for_one_day)]
  for start, end in book_time:
    rooms = fill_reservation_time_to(
      rooms, (get_hour_to_minutes(start), get_hour_to_minutes(end)))
  return max(rooms)


book_times = [[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
               ["14:10", "19:20"], ["18:20", "21:20"]],
              [["09:10", "10:10"], ["10:20", "12:20"]],
              [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]]
for book_time in book_times:
  print(solution(book_time))
