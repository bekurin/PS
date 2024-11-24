# 프로그래머스 no.77486 다단계 칫솔 판매
def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100
        current_seller_name = seller[i]
        
        while money > 0 and current_seller_name != "-":
            total[current_seller_name] += money - money // 10
            current_seller_name = parent[current_seller_name]
            money //= 10
    return [total[name] for name in enroll]
