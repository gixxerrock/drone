RollInc = 0.05
PitchInc = 0.05
LiftInc = 0.05

def Initialize():

    params = {}

    #use keyboard to mimic flight controller
    params['roll'] = 0.0
    params['pitch'] = 0.0
    params['lift'] = 0.0

    #manual control of motors
    params['m1_manual'] = 0.0
    params['m2_manual'] = 0.0
    params['m3_manual'] = 0.0
    params['m4_manual'] = 0.0

    params['exit'] = 1.0

    return params

def Update(params, wnd):
    
    c = wnd.getch()
    if c == ord('a'):
        params['roll'] -= RollInc

    if c == ord('d'):
        params['roll'] += RollInc

    if c == ord('s'):
        params['pitch'] -= PitchInc

    if c == ord('w'):
        params['pitch'] += PitchInc

    if c == ord('q'):
        params['lift'] -= LiftInc
        if params['lift'] < 0.0:
            params['lift'] = 0.0
    
    if c == ord('e'):
        params['lift'] += LiftInc
        
    if c == ord(' '):
        params['pitch'] = 0.0
        params['roll'] = 0.0
        params['lift'] = 0.0    

    if c == ord('x'):
        params['exit'] = -1.0