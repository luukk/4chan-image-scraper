import urllib
import os
from BeautifulSoup import BeautifulSoup

board = raw_input("wich board?\n")
image_amount = raw_input("how many images?\n")
folder = raw_input('the destinated path for your images: ')

def get_board_images(board,amount):
        imageUrl = []
        imageSizes = []

        first_character = board[:1]
        if(first_character != '/'):
                board = ''.join(('/',board))

        i = 0
        j = 0;
        while i < int(amount):
                if j == 1:
                        j = j+1
                base_url = 'http://boards.4chan.org';
                get_url = urllib.urlopen(base_url + board +"/"+ str(j));
                result = BeautifulSoup(get_url);
                href = result.findAll('a',{'class':'fileThumb'})
                for tag in href:
                        source = tag['href']
                        clear = source[2:]
                        imagesize = tag.img['alt']
                        imageUrl.append(clear);
                        imageSizes.append(imagesize)
                print("I found " + str(len(href)) + " images on board " + str(j))
                i = i+ int(len(href))
                j = j+1
        return imageUrl,imageSizes

def bytesto(bytes, to, bsize=1024):
    a = {' B': 1,'KB' : 1, 'MB': 2, 'GB' : 3, 'TB' : 4, 'PB' : 5, 'EB' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r * bsize
    return(r)

def set_board_images(board,amount,folder):
        images =  get_board_images(board,amount)
        memes = []
        memsize = [0]
        print('downloading images.... this might take a while')

        for x in range(0,int(image_amount)):
                memes.append(images[0][x]);
                membyte = images[1][x][:-2]
                memto = images[1][x][-2:]
                total = bytesto(membyte,memto) + memsize[0]
                memsize.insert(0,total)
                urllib.urlretrieve("http://"+memes[x], os.path.join(folder, str(x)+".jpg"));
        print('images downloaded!')
        print(str(total)+ ' bytes downloaded')
set_board_images(board,image_amount,folder);


