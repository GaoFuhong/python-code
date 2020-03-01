# Author:Fuhong Gao
import Image,ImageFont,ImageDraw
import sys
from math import sqrt
#根据字体的像素，处理文本，主要考虑换行因素,将文本化为几段，存储在列表
def handletext(pix,text):
    textlist=[]
    meihangzishu=size[0]/pix
    hangshu=len(text)/meihangzishu
    if hangshu==0:
        textlist.append(text)
    else:
        for i in range(0,hangshu):
            partoftext=text[meihangzishu*i:(i+1)*meihangzishu]
            textlist.append(partoftext)
        if text[(i+1)*meihangzishu:]:
            textlist.append(text[(i+1)*meihangzishu:])
    return textlist


if len(sys.argv)!=2:
    print ('用法：python '+sys.argv[0]+' 图片文件.png')
    sys.exit(0)

try:
    im=Image.open(sys.argv[1])
except:
    print ('无效图片，载入出错。')

size=im.size
print ('输入你想要隐藏的信息：')
text=input()
text=text.strip('\n').decode('utf-8')

pix=int(sqrt((size[0]*size[1])/len(text)))
while len(text)>(size[0]/pix)*(size[1]/pix):
    pix-=1


texttopic=handletext(pix,text)
#print texttopic
# 2 将文字印到图片上，白纸黑字
im2=Image.new('RGB',size,(255,255,255))
dr=ImageDraw.Draw(im2)
font=ImageFont.truetype('./ttf/simsun.ttc',pix)

ny=len(texttopic)
for i in range(0,ny):
    dr.text((0,pix*i),texttopic[i],font=font,fill=(0,0,0))
#im2.show()
#im2.save(sys.argv[1][:-4]+'word.png','PNG')
# 3 将密文像素隐藏到图片里
pixim=im.load()
pixim2=im2.load()
for x in range(0,size[0]):
    for y in range(0,size[1]):
        if pixim2[x,y]==(255,255,255):
            if pixim[x,y][0]%2==0:
                pass
            else:
                pixim[x,y]=(pixim[x,y][0]-1,pixim[x,y][1],pixim[x,y][2])

        else:
            if pixim[x,y][0]%2==0:
                pixim[x,y]=(pixim[x,y][0]+1,pixim[x,y][1],pixim[x,y][2])
            else:
                pass


print ('完成!')
im.save(sys.argv[1][:-4]+'_secret.png','PNG')
print ('已保存到 '+sys.argv[1][:-4]+'_secret.png')