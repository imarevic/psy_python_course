# task: create a Settings class and adopt this module accordingly
# keep in mind to move relevant imports here as wel
# import ordered dict
from collections import OrderedDict


settings = {
    "bgColor" : (180, 180, 180), # bg is light grey
    "blackColor" : (0, 0, 0), # text is black
    "redColor" : (255, 0, 0), # red color
    "greenColor" : (0, 255, 0), # blue color
    "circlePos" : None, # position of circles
    "radius" : 60, # radius of cricle
    "stimcolor" : None, # placeholder for stimulus color
    "screenSize" : (1200, 800), # set screen size
    "verPoints" : None, # placeholder for vert. points of fixcross
    "horPoints" : None, # placeholder for hor. points of fixcross
    "lineLength" : 40, # line length of fixcross
    "lineWidth" : 5, # line width of fixcross
    "FPS" : 60, # frames per second
    "screen" : None, # placeholder for screen instance
    "screenRect" : None, # placeholder for screen rectangle
    "instFont" : None, # placeholder for instructions font
    "instWidth" : None, # placeholder for instruction width
    "instHeight" : None, # placeholder for instruction height
    "absPath" : None, # placeholder for absolute path
    "instPath" : None, # placeholdr for relative path
    "stimuliPath" : None, # placeholder for stimuli path
    "dataPath" : None, # pöaceholder for data path
    "continue" : 0, # boolean value to control continue events
    "starter" : 0, # boolean value to control task start events
    "quit" : 0, # boolean value to control closing experiment at end
    "response" : None, # variable holding temporary response
    "filename" : None # placeholder for filename
}

# instructions dict
instructions = {
    "welcome" : None, # placeholder for welcome text
    "intro1" : None, # placeholder for intro 1 text
    "intro2" : None, # placeholder for intro 2 text
    "startTask" : None, # placeholder for starting task text
    "endTask" : None, # placeholder for end task text
    "goodbye" : None # placeholder for goodbye text
}

# results dict
results = OrderedDict([("id", []),
                       ("age", []),
                       ("gender", []),
                       ("major", []),
                       ("stimlist", []),
                       ("responses", []),
                       ("rts", []),
                       ])
