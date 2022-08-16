def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and sum([yourLeft, yourRight]) == sum([friendsLeft, friendsRight]):
        return True
    return False
