import sys
from . import helpers

def filetolist(filepath):
    """Takes file (first argument) and split into list"""
    try:
        return helpers.txttolist(filepath)
    except IndexError as e:
        sys.exit(helpers.errormsg("No file specified"))
    except IOError as e:
        sys.exit(helpers.errormsg("File not found"))
    except Exception as e:
        sys.exit(helpers.errormsg(e))

def listtogroups(filelist):
    """Seperates list into groups of header and body"""
    i = 0
    slidedata = [[]]
    for line in filelist:
        if line != "":
            slidedata[i].append(line)
            continue
        i += 1
        slidedata.append([])
    return slidedata

def listtoslides(data):
    """Checks if format is correct + adds img and durration elements"""
    slides = []
    for slide in data:
        slide = slide[:2]
        slide[0] = slide[0][:25]
        slide[1] = slide[1][:180]
        slide.append("imgpath")
        slide.append(0)
        slides.append(slide)
    return slides

def parsefile(file):
    """Parses file into slides"""
    return listtoslides(listtogroups(filetolist(file)))
