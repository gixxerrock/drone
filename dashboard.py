import curses

def DumpCmds(scr):
    scr.addstr(0,45, "ASDW    : roll pitch")
    scr.addstr(1,45, "<space> : zero")
    scr.addstr(2,45, "x       : exit")
    
def Initialize():
    params = {}

    params["screen"] = curses.initscr()
    
    params["screen"].clear()
    params["screen"].nodelay(True)
    curses.echo(False)

    DumpCmds(params["screen"])
    return params

def DumpInput(scr, i_params):
    scr.addstr(0, 0, "Roll : {:f}".format(i_params['roll']))
    scr.addstr(1, 0, "Pitch: {:f}".format(i_params['pitch']))  
    scr.addstr(2, 0, "Lift : {:f}".format(i_params['lift']))  

def DumpMotor(scr, m_params):
    scr.addstr(4, 0, "Motor1 : {:f}".format(m_params['m1_set']))
    scr.addstr(5, 0, "Motor2 : {:f}".format(m_params['m2_set']))
    scr.addstr(6, 0, "Motor3 : {:f}".format(m_params['m3_set']))
    scr.addstr(7, 0, "Motor4 : {:f}".format(m_params['m4_set']))
 
def Update(d_params, i_params, a_params, m_params, c_params):
    
    # Update the buffer, adding text at different locations
    DumpInput(d_params["screen"], i_params)
    DumpMotor(d_params["screen"], m_params)

    d_params["screen"].refresh()

def Shutdown(scr):
    curses.nocbreak()
    scr.keypad(False)
    curses.echo(True)

    curses.endwin()