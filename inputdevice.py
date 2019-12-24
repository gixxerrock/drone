RollInc = 0.05
PitchInc = 0.05

def DumpCmds():
    print("ASDW : roll pitch")
    print("<space> : zero")
    print("Ctrl-C : exit")

def Initialize():

    DumpCmds()
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

    return params

def Update(params):
    #TODO read keyboard

    params['roll'] += 0.1
    