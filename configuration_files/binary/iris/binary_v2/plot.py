import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr


# locate and read out log files
from matplotlib.ticker import FormatStrFormatter

logs_donor_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/binary_v2/LOGS1/'
logs_accretor_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/binary_v2/LOGS2/'
logs_binary_dir = '//wsl.localhost/Ubuntu/home/bips/binary_project/binary_v2/'

history_donor = mr.MesaData(logs_donor_dir + 'history.data')
history_accretor = mr.MesaData(logs_accretor_dir + 'history.data')
history_binary = mr.MesaData(logs_binary_dir + 'binary_history.data')


# define properties
age_donor = history_donor.star_age
age_accretor = history_accretor.star_age
age_binary = history_binary.age

mass_donor = history_donor.star_mass
mass_accretor = history_accretor.star_mass

log_mass_transfer = history_binary.lg_mtransfer_rate

model_number_donor = history_donor.model_number
model_number_accretor = history_accretor.model_number

luminosity_donor = history_donor.luminosity
luminosity_accretor = history_accretor.luminosity

log_temperature_donor = history_donor.log_Teff
log_temperature_donor_array = np.array(log_temperature_donor)
temperature_donor_array = (10 ** log_temperature_donor_array) / 1000
temperature_donor = temperature_donor_array.tolist()
temperature_donor_array = (10 ** log_temperature_donor_array)
temperature_donor = temperature_donor_array.tolist()

log_temperature_accretor = history_accretor.log_Teff
log_temperature_accretor_array = np.array(log_temperature_accretor)
temperature_accretor_array = 10 ** log_temperature_accretor_array
temperature_accretor = temperature_accretor_array.tolist()
temperature_accretor_array = (10 ** log_temperature_accretor_array)
temperature_accretor = temperature_accretor_array.tolist()


# plot masses over time
fig, axs = plt.subplots(2, sharex=True)
fig.suptitle('mass over time')

axs[0].plot(age_donor, mass_donor, c='r', label='donor')
axs[0].legend(loc='lower left')

axs[1].plot(age_accretor, mass_accretor, label='accretor')
axs[1].legend(loc='upper left')

fig.supxlabel('age (years)')
fig.supylabel('mass (solar units)')

plt.tight_layout()
plt.savefig('most_recent_mass_over_time.png')
plt.show()


# plot masses over model number
fig, axs = plt.subplots(2, sharex=True)
fig.suptitle('mass over model number')

axs[0].plot(model_number_donor, mass_donor, c='r', label='donor')
axs[0].legend(loc='lower left')

axs[1].plot(model_number_accretor, mass_accretor, label='accretor')
axs[1].legend(loc='upper left')

fig.supxlabel('model number')
fig.supylabel('mass (solar units)')

plt.tight_layout()
plt.savefig('most_recent_mass_over_model_number.png')
plt.show()


# # plot mass transfer over model number
# plt.plot(model_number_donor, age_binary)
# plt.show()


# plot HR diagrams
fig, axs = plt.subplots(1, 2)
fig.suptitle('HR diagram')

axs[0].plot(temperature_donor, luminosity_donor, c='r', label='donor')
axs[0].invert_xaxis()
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].tick_params(axis='x', which="both", labelrotation=45)
axs[0].tick_params(axis='y', which="both", labelrotation=45)
# axs[0].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# axs[0].xaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
axs[0].legend()

axs[1].plot(temperature_accretor, luminosity_accretor, label='accretor')
axs[1].invert_xaxis()
axs[1].set_xscale('log')
axs[1].set_yscale('log')
axs[1].tick_params(axis='x', which="both", labelrotation=45)
axs[1].tick_params(axis='y', which="both", labelrotation=45)
# axs[1].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# axs[1].xaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
axs[1].legend()

fig.supxlabel('effective temperature (K)')
fig.supylabel('luminosity (solar units)')

plt.tight_layout()
plt.savefig('most_recent_hr_diagram.png')
plt.show()


# plot age over model_number
plt.plot(age_accretor, model_number_accretor)
plt.show()
