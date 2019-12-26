import accelerometer
import inputdevice
import control
import motor
import dashboard

m_params = motor.Initialize()
a_params = accelerometer.Initialize()
i_params = inputdevice.Initialize()
c_params = control.Initialize()
d_params = dashboard.Initialize()

while(i_params['exit'] > 0.0):
     #input   
    inputdevice.Update(i_params, d_params["screen"])
    accelerometer.Update(a_params)

    #run control system
    control.Update(i_params, a_params, m_params, c_params)

    #output
    motor.Update(m_params)
    dashboard.Update(d_params, i_params, a_params, m_params, c_params)

dashboard.Shutdown(d_params["screen"])
    