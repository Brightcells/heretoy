#!/usr/bin/env python
# coding=utf-8

import os
try:
    from PIL import Image, ImageFont, ImageDraw
except ImportError:
    import Image, ImageFont, ImageDraw


def make_thumb(path, w, h):
    base, ext = os.path.splitext(path)
    try:
        im = Image.open(path)
    except IOError:
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255 - x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255, 255, 255), None, bgmask)
        else:
            im = im.convert('RGB')

    width, height = im.size
    if width / float(height) > w / float(h):
        d = (width - height * w / h) / 2
        box = (d, 0, width - d, height)
    else:
        d = (height - width * h / w) / 2
        box = (0, d, width, height - d)
    region = im.crop(box)

    filename = base + '_' + '%sx%s' % (str(w), str(h)) + (ext or '.jpeg')
    thumb = region.resize((w, h), Image.ANTIALIAS)
    thumb.save(filename, quality=100)  # 默认 JPEG 保存质量是 75, 不太清楚。可选值(0~100)
    return filename


def make_pic(text, path, w, h):
    im = Image.new('RGB', (w, h), (255, 220, 64))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simsun.ttc'), 55)
    dr.text((10, 5), text, font=font, fill="#000000")
    im.save(path)
