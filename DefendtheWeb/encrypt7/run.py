from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

imo = Image.open("DSWii6x_ori.png")
im = Image.open("DSWii6x.png")

rgb_imo = imo.convert('RGB')
rgb_im = im.convert('RGB')

index_row = 0
while index_row < 176:
    index_col = 0
    while index_col < 873:
        ro, go, bo = rgb_imo.getpixel((index_col, index_row))
        r, g, b = rgb_im.getpixel((index_col, index_row))
        if(ro != r or go != g or bo != b):
            print('unmatch: ',index_row,index_col)
        index_col = index_col + 1
    index_row = index_row + 1
    