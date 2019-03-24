# changeState.py
import globalvars as GV
import MainMenuState as MMS
from PlayState import playState

def state(S, L):
    GV.state = S
    GV.level = L

def execute():    
    if GV.state == 0:
        mainMenu = MMS.mms()
        mainMenu.updateAndRender()
    if GV.state == 1:
        playstate = playState()
        playstate.updateAndRender()
    if GV.state == 2:
        deadState = MMS.ds()
        deadState.updateAndRender()
    if GV.state == 3:
        gameOver = MMS.gos()
        gameOver.updateAndRender()
    if GV.state == 4:
        betweenLevel = MMS.bl()
        betweenLevel.updateAndRender()
    if GV.state == 5:
        pauseState = MMS.pause()
        pauseState.updateAndRender()
    if GV.state == 6:
        titleScreen = MMS.ts()
        titleScreen.updateAndRender()