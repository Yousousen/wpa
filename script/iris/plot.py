import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr


# locate and read out log files
single_logs_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/single_v2/saved_logs/2Msun_LOGS/'
single_history = mr.MesaData(single_logs_dir + 'history.data')

binary_logs_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/binary_v2/saved_logs/2Msun/10_year_period/LOGS2/'
binary_history = mr.MesaData(binary_logs_dir + 'history.data')


# define properties single star
single_age = single_history.star_age
single_mass = single_history.star_mass
single_model_number = single_history.model_number
single_luminosity = single_history.luminosity

single_log_radius = single_history.log_R
single_log_radius_array = np.array(single_log_radius)
single_radius_array = 10 ** single_log_radius_array
single_radius = single_radius_array.tolist()

single_log_temperature = single_history.log_Teff
single_log_temperature_array = np.array(single_log_temperature)
single_temperature_array = 10 ** single_log_temperature_array
single_temperature = single_temperature_array.tolist()


# define properties binary accretor
binary_age = binary_history.star_age
binary_mass = binary_history.star_mass
binary_model_number = binary_history.model_number
binary_luminosity = binary_history.luminosity

binary_log_radius = binary_history.log_R
binary_log_radius_array = np.array(binary_log_radius)
binary_radius_array = 10 ** binary_log_radius_array
binary_radius = binary_radius_array.tolist()

binary_log_temperature = binary_history.log_Teff
binary_log_temperature_array = np.array(binary_log_temperature)
binary_temperature_array = 10 ** binary_log_temperature_array
binary_temperature = binary_temperature_array.tolist()


# plot HR diagrams
plt.plot(single_temperature[:41], single_luminosity[:41], label='single')
plt.plot(binary_temperature, binary_luminosity, label='binary')
plt.tick_params(axis='x', which="both", labelrotation=45)
plt.tick_params(axis='y', which="both", labelrotation=45)
plt.title('2Msun HR diagram')
plt.xlabel('effective temperature (K)')
plt.ylabel('luminosity (solar units)')
plt.xscale('log')
plt.yscale('log')
ax = plt.gca()
ax.invert_xaxis()

plt.legend()
plt.tight_layout()
plt.savefig('hr_diagram.png')
plt.show()


# plot mass over time
plt.plot(single_age[:41], single_mass[:41], label='single')
plt.plot(binary_age, binary_mass, label='binary')
plt.tick_params(axis='x', which="both", labelrotation=45)
plt.tick_params(axis='y', which="both", labelrotation=45)
plt.title('2Msun mass over time')
plt.xlabel('age (years)')
plt.ylabel('mass (solar units)')

plt.legend()
plt.tight_layout()
plt.savefig('mass_over_time.png')
plt.show()


# plot radius over time
plt.plot(single_age[:41], single_radius[:41], label='single')
plt.plot(binary_age, binary_radius, label='binary')
plt.tick_params(axis='x', which="both", labelrotation=45)
plt.tick_params(axis='y', which="both", labelrotation=45)
plt.title('2Msun radius over time')
plt.xlabel('age (years)')
plt.ylabel('radius (solar units)')

plt.legend()
plt.tight_layout()
plt.savefig('radius_over_time.png')
plt.show()


# plot age over model number
plt.plot(single_model_number, single_age, label='single')
plt.plot(binary_model_number, binary_age, label='binary')
plt.tick_params(axis='x', which="both", labelrotation=45)
plt.tick_params(axis='y', which="both", labelrotation=45)
plt.title('age over model number')
plt.xlabel('model number')
plt.ylabel('age (years)')

plt.legend()
plt.tight_layout()
plt.show()
