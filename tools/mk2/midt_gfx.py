"""
WIP midway t-unit gfrom reader (/writer eventually)
2018, <samuli@tuomola.net>

this was tested with mortal kombat 2 using following steps:
in ipython combine the rom chip images:
 combinefiles(['ug14-vid','uj14-vid','ug19-vid','uj19-vid'], 'u1419.bin')
 combinefiles(['ug16-vid','uj16-vid','ug20-vid','uj20-vid'], 'u1620.bin')
 combinefiles(['ug17-vid','uj17-vid','ug22-vid','uj22-vid'], 'u1722.bin')
then in command shell recreate the gfx memory area:
# cp u1419.bin ujg.bin
# dd if=u1620.bin of=ujg.bin seek=4096 bs=1024
# dd if=u1722.bin of=ujg.bin seek=8192 bs=1024
compile mame with LOG_DMA and dig out relevant offsets for an image from mame logs:
# dd if=ujg.bin of=cdimg.bin iseek=0xAD12E5 bs=1 count=0xCE98
and as the game was showing that image dumped the palette ram in mame debugger:
# save mk2cd.pal, 0x01800000, 0x7ffff
"""
from PIL import Image
import struct

flatten = lambda l: [item for sublist in l for item in sublist]
r16 = lambda b,o: struct.unpack('H', b[o:o+2])[0]
pal5bit = lambda p: ((p&0x1f) <<3) | ((p&0x1f)>>2)

def decodepalette(data):                                
    pal = struct.unpack_from("<%iH" % (len(data)/struct.calcsize('H')), data)                                                        
    for x in pal:                                  
        yield pal5bit(x >> 10), pal5bit(x >> 5), pal5bit(x >> 0)

def combinefiles(infiles, outfile):
    """
    dumb util for restiching interleaved files one byte at a time
    files are assumed to be identical size
    """
    fsz = len(dat[0])
    outdat = bytearray(fsz*len(files))
    datlst = [open(f,'rb').read() for f in files]
    for p in range(fzs):
        for n,d in enumerate(datlst):
            fdat[(p*len(infiles))+n] = d[p]
    open(outfile,'wb').write(fdat)

def midt_read(dst, src, pal, w=88, h=92, skip=1, bpp=8):
    """
    Emulate midway t-unit DMA chip read from gfxrom
    """
    hght=h << 8
    iy=0
    offset = 0
    xstep = 0x100
    mask = (1 << bpp) - 1
    sy=0
    while iy < hght:
        wdth = w<<8
        o = offset
        ix = 0
        tx = 0
        sx = 0
        pre=0
        post=0
        if skip:
            val = (r16(src, o>>3) >>4 ) & 0xff
            o += 8
            pre = (val & 0xf) << 9
            tx = int(pre / xstep)
            ix += (tx * xstep)
            post = ((val>>4) & 0xf) << 9
            wdth -= post
            #print(hex(wdth), hex(o),hex(o>>3),hex(pre),hex(post))
        while ix < wdth:
            d = ( r16(src, o>>3) >>4 ) & mask
            dst[(tx+sx)&0x3ff,sy] = pal[d | 256]
            sx = (sx + 1) & 0x3ff
            ix += xstep
            o += bpp
        sy = (sy+1) & 0x1ff
        iy += 0x100
        wdth = w
        if skip:
            offset += 8
            wdth -= (pre + post) >> 8
            if wdth > 0: offset += wdth * 8


if __name__ == '__main__':
    # run mame -debug mk2, and do: save mk2cd.pal, 0x01800000, 0x7ffff
    pal = list(decodepalette(open('mk2cd.pal','rb').read()))
    srcimg = open('cdimg.bin','rb').read()

    img = Image.new( 'RGB', (800,600), "black")
    pixels = img.load()
    midt_read(pixels, srcimg, pal)
    img.show()
    
