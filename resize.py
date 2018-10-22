import os, sys
from PIL import Image as img

size = 28, 28

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0]
    if infile != outfile:
        try:
            im = img.open(infile)
            im.thumbnail(size, img.ANTIALIAS)
            im.save(outfile + ".png")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
