import re
 1
 text_to_search = '''
# ab abbb abbbbbb a abbbbbbb
# '''
pattern = re.compile(r'a[b]*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


2 
text_to_search = '''
ab abbb abb a acb
'''
pattern = re.compile(r'a[b]{2,3}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)



3 
text_to_search = '''
a_b_c_d_e abcde a_b_b_a q_w_e_E
'''
pattern = re.compile(r'[a-z]+_[a-z]+')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

4 
text_to_search = '''
SDGSDGSDffsghjf ndndsdvvf, okdfmdsfkmL,SL,D,S SAKMSFKMF949875949094
'''
pattern = re.compile(r'[A-Z]+[a-z]+')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

5
text_to_search = '''
asdflmsdmmkdsfb  ab adskmkmsdB 213242 
'''
pattern = re.compile(r'a.*b\b')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
6
text_to_sub = "anc, fedsd , hey."
pattern = r'[ ,.]'
new_text = re.sub(pattern, ':' , text_to_sub)
print(new_text)
7 
def snake_to_camel(s):
    words = s.split('_')
    up_words = [words[0]] + [w.capitalize() for w in words[1:]]
    ans = ''.join(up_words)
    return ans
snake_str = 'pop_gop_top_sop'
camel_str = snake_to_camel(snake_str)
print(camel_str)  
8


def split_at_uppercase(string):
    
    return re.findall('[A-Z][^A-Z]*', string)

string = 'AbcdeFghUywePoiuKfd'
result = split_at_uppercase(string)
print(result) 
9


def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

text = 'AbcdeFghUywePoiuKfd'
ans = insert_spaces(text)
print(ans)
10
def camel_to_snake(camel_str):
    split_str = re.sub('([A-Z][a-z]+)', r' \1', camel_str).split()
    snake_str = '_'.join([s.lower() for s in split_str])
    return snake_str
camel_str = 'PopGopTopSop'
snake_str = camel_to_snake(camel_str)
print(snake_str)