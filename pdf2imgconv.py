from pdf2image import convert_from_path
import cv2
import os
import numpy as np
import os
# images = convert_from_path('/home/selva/Selva/Products/Task/Datas/IEEEConforence.pdf')
 
# for i in range(len(images)):
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')


def convert_bytes(size, unit=None):
    if unit == "KB":
        return (round(size / 1024, 3), str(round(size / 1024, 3)) + ' Kilobytes')
    elif unit == "MB":
        return (round(size / (1024 * 1024), 3), str(round(size / (1024 * 1024), 3)) + ' Megabytes')
    elif unit == "GB":
        return ( round(size / (1024 * 1024 * 1024), 3), str(round(size / (1024 * 1024 * 1024), 3)) + ' Gigabytes')
    else:
        return ( str(size) + ' bytes')
 




def img_read(img_root,img_cnt):
    for i in range(img_cnt):
        root=os.path.join(img_root, str(i) + '.jpg')
        rgb=cv2.imread(root)

        ## IMAGE FILE SIE CHECK LIST IF NEEDED TO USE 
        size = os.path.getsize(root) 
        inp_img_sz=convert_bytes(size, "KB")
        print('file size',inp_img_sz[0],inp_img_sz[1])
        if 1000<inp_img_sz[0]:
            print('above 1mb ')
        else:

            print('below 1 Mb image size')    
        # cv2.imwrite('compress_img2.jpeg', rgb,[cv2.IMWRITE_JPEG_QUALITY,100])
        # [cv2.IMWRITE_JPEG_QUALITY, 0]   [cv2.IMWRITE_PNG_COMPRESSION, 9]


        print(np.shape(rgb))

    # root=os.path.join(img_root, str(i) + '.jpg')
    # rgb=cv2.imread(root)
    # print(np.shape(rgb))
    return rgb
    

def pdimg(pdf_root,out_root):
    images = convert_from_path(pdf_root)
    for i in range(len(images)):
        # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        pth2=os.path.join(out_root, str(i) + '.jpg')
        images[i].save(pth2)
        image=images[i]
    return i

## Mk dir for images store
import sys
sk_cwd=sys.path[0]
directory = "ihritik"
config_path = os.path.join(sk_cwd,str("ihritik"))
isdir = os.path.isdir(config_path)  
outst=str(isdir)
if outst=='False':
    print('no folder name ihritik,now created')
    new=os.mkdir(directory)
else:
    print('Always folder ihritik is there')


out_root=r'/home/selva/Selva/Products/Task/Datas/ihritik'
pdf_root=r'/home/selva/Selva/Products/Task/Datas/IEEEConforence.pdf'
img_cnt=pdimg(pdf_root,out_root)  
img_read(out_root,img_cnt)


# if strans="False":
    
#     new=os.mkdir(directory)

# else strans="True":
#     print('remove old images folder')
    
