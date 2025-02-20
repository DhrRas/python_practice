s = 'hello    world    lol'
# res = s.split(' ')
# res1 = ' '.join(res)

print(s)
for word in s.split(' '):
    r = ''.join(word.capitalize())
    print(r,end=' ')



