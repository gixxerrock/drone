def Initialize():
    params = {}

    #motor set points
    params['m1_set'] = 0.0
    params['m2_set'] = 0.0
    params['m3_set'] = 0.0
    params['m4_set'] = 0.0

    #actual motor value
    params['m1_act'] = 0.0
    params['m2_act'] = 0.0
    params['m3_act'] = 0.0
    params['m4_act'] = 0.0

    return params

def Update():
    #TODO take motor set points and send commands to controller
    x=5