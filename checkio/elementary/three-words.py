def checkio(words):
    test = 0
    for el in words.split(" "):
        if el.isalpha():
            test += 1
            if test == 3:
                return True
        else:
            test = 0

    return False

if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
