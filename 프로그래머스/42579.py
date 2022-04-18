# 프로그래머스 No.42579 베스트앨범
def get_music_dict(genres, plays):
  music_dict = {}
  for idx, item in enumerate(list(zip(genres, plays))):
    if item[0] not in music_dict:
      music_dict[item[0]] = [(idx, item[1])]
    else:
      music_dict[item[0]].append((idx, item[1]))
  return music_dict

def get_best_genre(music_dict):
  best_genre = []
  for key, value in music_dict.items():
    temp = 0
    for item in value:
      temp += item[-1]
    best_genre.append((key, temp))
  return sorted(best_genre, key = lambda x: x[-1], reverse = True)

def solution(genres, plays):
  answer = []
  music_dict = get_music_dict(genres, plays)
  best_genre = get_best_genre(music_dict)

  for key, value in music_dict.items():
    music_dict[key] = sorted(value, key = lambda x: x[-1], reverse = True)
    
  for genre, count in best_genre:
    if len(music_dict[genre]) == 1:
      answer.append(music_dict[genre][0][0])
    else:
      for item in music_dict[genre][:2]:
        answer.append(item[0])
  return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))