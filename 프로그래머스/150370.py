# 프로그래머스 No.150370 개인정보 수집 유효기간
def convert_date_to_number(date, separator="."):
  return map(int, date.split(separator))


def get_term_dict(terms):
  term_dict = {}
  for term in terms:
    key, duration = term.split(" ")
    term_dict[key] = duration
  return term_dict


def get_inroll_date_and_term_duration(privacy, term_dict):
  inroll_date, term = privacy.split(" ")
  return inroll_date, term_dict[term]


def get_privacy_expire_date(inroll_date, duration):
  year, month, day = convert_date_to_number(inroll_date)
  month = month + duration

  if (month % 12 == 0):
    expire_year = year + (month // 12) - 1
    expire_month = 12
    return "{}.{}.{}".format(expire_year, expire_month, day)

  expire_year = year + (month // 12)
  expire_month = month % 12
  return "{}.{}.{}".format(expire_year, expire_month, day)


def is_expired(today, expire_date):
  t_year, t_month, t_day = convert_date_to_number(today)
  e_year, e_month, e_day = convert_date_to_number(expire_date)

  if (t_year > e_year):
    return True

  if ((t_year == e_year) and (t_month > e_month)):
    return True

  if ((t_year == e_year) and (t_month == e_month) and (t_day >= e_day)):
    return True
  return False


def solution(today, terms, privacies):
  answer = []
  year, month, day = today.split(".")
  term_dict = get_term_dict(terms)

  for idx, privacy in enumerate(privacies):
    inroll_date, duration = get_inroll_date_and_term_duration(
      privacy, term_dict)
    expire_date = get_privacy_expire_date(inroll_date, int(duration))
    if (is_expired(today, expire_date)):
      answer.append(idx + 1)
  return answer


print(
  solution("2022.05.19", ["A 6", "B 12", "C 3"],
           ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2021.12.08", ["A 18"], ["2020.06.08 A"]))
