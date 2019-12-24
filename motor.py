def Initialize():
    params = {}

    #motor set points (what control system wants)
    params['m1_set'] = 0.0
    params['m2_set'] = 0.0
    params['m3_set'] = 0.0
    params['m4_set'] = 0.0

    #actual motor value (read from motor controller)
    params['m1_act'] = 0.0
    params['m2_act'] = 0.0
    params['m3_act'] = 0.0
    params['m4_act'] = 0.0

    return params

def Update(params):
    #TODO take motor set points and send commands to controller
    x=5