'''
WIP
Given a string and a maximum line length, wrap the text at the max length
'''


def wrap(string, max_width):
    strList = list(string)
    for i in range(len(string)):
        if(i%(max_width+1) == 0):
            strList.insert(i,'\n')
    strList.insert(i+max_width+1,'\n')
    wrappedString = ''.join(strList)
    return wrappedString

def main(string,max_width):
    wrap(string,max_width)

#print(main())
