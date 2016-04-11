import urllib
import os
import urlparse
from BeautifulSoup import BeautifulSoup

board = raw_input("wich board?\n")
image_amount = raw_input("how many images?\n")
folder = raw_input('the destinated path for your images: ')

def get_board_images(board,amount):
        imageUrl = []
        imgs = []
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
                #print(base_url + board +"/"+ str(i))
                result = BeautifulSoup(get_url);
                images = result.findAll('img')
                for tag in images:
                        source = tag['src']
                        clear = source[2:]
                        imageUrl.append(clear);
                print("I found " + str(len(images)) + " images on board " + str(j))
                imgs.append(images)
                i = i+ int(len(images))
                j = j+1
        return imageUrl

def set_board_images(board,amount,folder):
        images =  get_board_images(board,amount)
        memes = []
        print('thats a total of ' + str(len(images)) + ' because math')

        for x in range(0,int(image_amount)):
                #begin = images[x].replace('s.jpg','.jpg')
                memes.append(images[x]);
                #print(memes)
                urllib.urlretrieve("http://"+memes[x], os.path.join(folder, str(x)+".jpg"));
        print('images downloaded!')

set_board_images(board,image_amount,folder);

