
def wrap(str, width):
    if str == None:
        return ""
    if len(str) <= width:
        return str
    else:
        brkpoint = str.rfind(' ', 0, width + 1)
        if brkpoint == -1:
            brkpoint = width;
        return str[0:brkpoint] + "\n" + wrap(str[brkpoint:].strip(), width)

class Wrapper(object):

    def __init__(self):
        pass




