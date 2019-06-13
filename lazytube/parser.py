import helpers

# take file and split into list
filename = "example.txt"
file = helpers.txttolist(filename)

# seperate list into groups of header and body
i = 0
slides = [[]]
for line in file:
    if line != "":
        slides[i].append(line)
        continue
    i += 1
    slides.append([])

# check if format and length is correct
for slide in slides:
    slide[0] = slide[0][:25]
    slide[1] = slide[1][:140]
