import sys
import re
import os

PATH = os.path.abspath(sys.stdin.read()[:-1])
NEW_PATH = '/mnt/datos/Camila/A-nowcasting-model-for-Medellin-city/train/images/'

#'/mnt/datos/Camila/A-nowcasting-model-for-Medellin-city/train/images/train/'

mode = 'test' if 'test' in PATH else 'train'

fil = open(PATH, 'r').read()

reg1 = re.compile('<folder>.*?</folder>')
reg2 = re.compile('<path>.*?</path>')
reg3 = re.compile('<filename>.*?</filename>')

fil = reg1.sub('<folder>%s</folder>' % mode, fil)

rr = '<path>' + NEW_PATH + mode + '/' \
     + os.path.basename(PATH)[:-3] + 'jpg</path>'

fil = reg2.sub(rr, fil)

file_name = re.search(reg3, fil).group(0)[10:][:-15]
if file_name != PATH.split('/')[-1][:-4]:
    fil = reg3.sub('<filename>' + PATH.split('/')[-1][:-4] + '.jpg</filename>',
                   fil)

print(fil)
