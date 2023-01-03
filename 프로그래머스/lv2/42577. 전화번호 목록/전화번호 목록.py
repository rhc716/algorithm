def solution(phone_book):
    phone_book.sort()
    for i, v in enumerate(phone_book):
        if i+1 < len(phone_book) and phone_book[i+1][:len(v)] == v:
            return False
    return True