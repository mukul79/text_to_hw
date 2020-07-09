import os
from PIL import Image

page = Image.open('page.png').convert('L')
#text=input("Enter text: ")

path_font = 'myfont/'#

    
width,length = Image.open(path_font +os.listdir(path_font)[0]).size
fp = open('text.txt','r')
text = fp.read()

line_num=0
let_num=0
para_list=text.split('\n')
for para in para_list:
    word_list = para.split(' ')
    for word in word_list:
        wsize = len(word)
        if(wsize*width >= 2480 - let_num*width):
            line_num+=1
            let_num=0
        for i in range(wsize):
            letter = word[i]
            name = letter
            if(name.isupper()):
                name=name.lower()+'upper'
            elif(name=='?'):
                name='question'
            print(name,end='')
            let_image = Image.open(path_font + name + '.png').convert('L')
            rect=(let_num*width,line_num*length)
            page.paste(let_image,rect)
            let_num+=1
        rect=(let_num*width,line_num*length)
        let_image = Image.open(path_font+'space.png').convert('L')
        page.paste(let_image,rect)
        let_num+=1
        print(" ",end='')
page.save('result.png')
            
        