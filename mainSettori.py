import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

test = ff1.get_session(2020, 'testing', '5')

laps = test.load_laps()
fast_hamilton = laps.pick_driver('STR').pick_fastest()

prova = fast_hamilton.Sector1Time
rova = fast_hamilton.Sector2Time
ova = fast_hamilton.Sector3Time

print("Settore 1 {0} - {1} - {2}".format(prova, rova, ova))
#th = fast_hamilton.telemetry['Time']
#vCarh = fast_hamilton.telemetry['Speed']

#fast_vettel = laps.pick_driver('VET').pick_fastest()
#tv = fast_vettel.telemetry['Time']
#vCarv = fast_vettel.telemetry['Speed']
"""
# The rest is just plotting
fig, ax = plt.subplots()
plotting.laptime_axis(ax, axis='xaxis')
ax.plot(th.dt.total_seconds(), vCarh, color='cyan')
ax.plot(tv.dt.total_seconds(), vCarv, color='red')
ax.set_xlabel('Time')
ax.set_ylabel('Speed')
ax.set_title('Stroll / Vettel Test 5 Giro Veloce')
plt.show()"""