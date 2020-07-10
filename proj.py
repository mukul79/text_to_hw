import os
from PIL import Image
from fpdf import FPDF

page = Image.open('page.png')
#text=input("Enter text: ")

path_font = 'myfont/'#

for file in os.listdir('pages/'):
    os.remove('pages/'+file)
    
width,length = Image.open(path_font +os.listdir(path_font)[0]).size
fp = open('text.txt','r')
text = fp.read()

line_num=0
let_num=0
pagenum=0
para_list=text.split('\n')
for para in para_list:

    word_list = para.split(' ')
    
    for word in word_list:
        wsize = len(word)
        
        if(wsize*width >= 2480 - let_num*width):
            line_num+=1
            let_num=0
            
        if((line_num+1)*length>= 3508):
            page.save('pages/result'+str(pagenum)+'.png')
            page=Image.open('page.png')
            pagenum+=1
            line_num=0
            let_num=0
        
        for i in range(wsize):
            letter = word[i]
            name = letter
            
            print(name,end='')
            
            if(name.isupper()):
                name=name.lower()+'upper'
            elif(name=='?'):
                name='question'
            let_image = Image.open(path_font + name + '.png')
            rect=(let_num*width,line_num*length)
            page.paste(let_image,rect)
            let_num+=1
        
        rect=(let_num*width,line_num*length)
        let_image = Image.open(path_font+'space.png')
        page.paste(let_image,rect)
        let_num+=1
        print(" ",end='')
    line_num+=1        
    let_num=0
    print('\n',end='')
page.save('pages/result'+str(pagenum)+'.png')

#for page in os.listdir('pages/'):
#    im=Image.open('pages/'+ page).resize((560,742))
#    im.save('pages/'+ page)
pdf = FPDF('P','pt',(2480,3508))
pdf.set_auto_page_break(0)
for page in os.listdir('pages/'):
    pdf.add_page()
    pdf.image('pages/'+page)
pdf.output('static/handwritten_text.pdf','F')
        