print({n for n in range(10)})
print((tuple(n for n in range(10))))
text = 'Hello'
print([ (n,text[n] )for n in range(len(text))])