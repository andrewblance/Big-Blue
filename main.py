# Welcome to Python on Pokitto!
import upygame as upg
import globalvars as GV
import changeState as CS

if __name__ == "__main__":
    upg.display.init()
    
    GV.init_global()

    while True:
        CS.execute()
