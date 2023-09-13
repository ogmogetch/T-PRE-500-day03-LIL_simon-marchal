a = 'This is a test. Is it possible to fly? Good things come to those who never give up.'
def phrase(x):
    b = x.replace('?', '.').split('. ')
    l=[]
    for i in b:
        l.append(i.split(' ')[0])
    print (l)


phrase(a)