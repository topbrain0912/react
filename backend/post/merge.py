from PIL import Image

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_v_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    if im1.width == im2.width:
        _im1 = im1
        _im2 = im2
    elif (((im1.width > im2.width) and resize_big_image) or
          ((im1.width < im2.width) and not resize_big_image)):
        _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
    dst = Image.new("RGBA", (_im1.width, _im1.height + _im2.height))
    dst.paste(_im1, (0,0) )
    dst.paste(_im2, (0,_im1.height))
    return dst

def customer(im1, im2):
    _im1 = im1
    _im2 = im2
    dst = Image.new("RGBA", (_im2.width, _im1.height + _im2.height))
    dst.paste(_im1, ((_im2.width-_im1.width)//2 +60 ,0) )
    dst.paste(_im2, (0,_im1.height))
    return dst

def get_concat_v_cut_center(im1, im2):
    dst = Image.new('RGBA', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, ((im1.width - im2.width) // 2, im1.height))
    return dst


                # final2 = Image.new("RGBA", im1.size)
                # final2 = Image.alpha_composite(final2, im1)
                # final2 = Image.alpha_composite(final2, im2).save('media/merge/human.png')
# get_concat_h(im1, im1).save('media/merge/pillow_concat_h.jpg')
# get_concat_v(im1, im1).save('media/merge/pillow_concat_v.jpg')s