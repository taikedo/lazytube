import sys
import helpers

# take file (first argument) and split into list
try:
    file = helpers.txttolist(sys.argv[1])
except IndexError as e:
    sys.exit(helpers.errormsg("No file specified"))
except IOError as e:
    sys.exit(helpers.errormsg("File not found"))
except Exception as e:
    sys.exit(helpers.errormsg(e))

# seperate list into groups of header and body
i = 0
slidedata = [[]]
for line in file:
    if line != "":
        slidedata[i].append(line)
        continue
    i += 1
    slidedata.append([])

# check if format and length is correct + add img and durration elements
slides = []
for slide in slidedata:
    slide = slide[:2]
    slide[0] = slide[0][:25]
    slide[1] = slide[1][:140]
    slide.append("path")
    slide.append(0)
    slides.append(slide)
