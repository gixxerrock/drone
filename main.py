import accelerometer
import inputdevice
import control
import motor
import dashboard

m_params = motor.Initialize()
a_params = accelerometer.Initialize()
i_params = inputdevice.Initialize()
c_params = control.Initialize()

while(True):
     #input   
    inputdevice.Update(i_params)
    accelerometer.Update(a_params)

    #run control system
    control.Update(i_params, a_params, m_params, c_params)

    #output
    motor.Update(m_params)
    dashboard.Update(i_params, a_params, m_params, c_params)
    