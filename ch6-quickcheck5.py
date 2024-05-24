'''
Quick Check: Modifying strings
What would be a quick way to change all punctuation in a string to spaces?
'''
x = 'q,w.e:r;t"y-u?i!o_p[a]s)d(f\'g'

table = x.maketrans('.,?;:!"-_][)(\'',' '*14)
y = x.translate(table)

print(y)