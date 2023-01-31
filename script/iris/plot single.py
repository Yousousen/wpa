import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr


# locate and read out log files
logs_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/single_v2/saved_logs/1Msun_LOGS/'
history = mr.MesaData(logs_dir + 'history.data')


# define properties
age = history.star_age
mass = history.star_mass
model_number = history.model_number
luminosity = history.luminosity

log_temperature = history.log_Teff
log_temperature_array = np.array(log_temperature)
temperature_array = 10 ** log_temperature_array
temperature = temperature_array.tolist()


# plot mass over time
plt.plot(age, mass)
plt.title('mass over time')
plt.xlabel('age (years)')
plt.ylabel('mass (solar units)')

plt.savefig('most_recent_mass_over_time.png')
plt.show()


# plot mass over model number
plt.plot(model_number, mass)
plt.title('mass over model number')
plt.xlabel('model number')
plt.ylabel('mass (solar units)')

plt.savefig('most_recent_mass_over_model_number.png')
plt.show()


# plot HR diagrams
plt.plot(temperature, luminosity)
plt.title('HR diagram')
plt.xlabel('effective temperature (K)')
plt.ylabel('luminosity (solar units)')
plt.xscale('log')
plt.yscale('log')
ax = plt.gca()
ax.invert_xaxis()

plt.savefig('most_recent_hr_diagram.png')
plt.show()


# plot age over model_number
plt.plot(age, model_number)
plt.show()
