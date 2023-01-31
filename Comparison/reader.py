
# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt

'''
# STAR 1
# HRD
# load and plot data
h = mr.MesaData('LOGS1/history.data')
plt.plot(h.log_Teff, h.log_L)

# set axis labels
plt.title('HR Diagram Star 1')
plt.xlabel('log Effective Temperature')
plt.ylabel('log Luminosity')

# invert the x-axis
plt.gca().invert_xaxis()

plt.show()


# TRho
# load entire LOG directory information
l = mr.MesaLogDir('./LOGS1')
# grab the last profile
p = l.profile_data()

# this works even if you only have logRho and logT!
plt.loglog(p.Rho, p.T)
plt.title('TRho Graph Star 1')
plt.xlabel("Density")
plt.ylabel("Temperature")
plt.show()


# mass over time
# load and plot data
plt.plot(h.model_number, h.star_1_mass)

# set axis labels
plt.title('Star 1 mass over time')
plt.ylabel('star 1 mass')
plt.xlabel('model number')

plt.show()
'''


# load and plot data
h1 = mr.MesaData('1Msol/history.data')
h2 = mr.MesaData('2Msol/history.data')
h4 = mr.MesaData('4Msol/history.data')
h8 = mr.MesaData('8Msol/history.data')
h5 = mr.MesaData('5Msol/history.data')
hDonor = mr.MesaData('LOGS1/history.data')
hCompanion = mr.MesaData('LOGS2/history.data')
# load entire LOG directory information
l1 = mr.MesaLogDir('./1Msol')
l2 = mr.MesaLogDir('./2Msol')
l4 = mr.MesaLogDir('./4Msol')
l8 = mr.MesaLogDir('./8Msol')
l5 = mr.MesaLogDir('./5Msol')
lDonor = mr.MesaLogDir('./LOGS1')
lCompanion = mr.MesaLogDir('./LOGS2')
# grab the last profile
p1 = l1.profile_data()
p2 = l2.profile_data()
p4 = l4.profile_data()
p8 = l8.profile_data()
p5 = l5.profile_data()
pDonor = lDonor.profile_data()
pCompanion = lCompanion.profile_data()

plt.style.use("dark_background")
figure, axis = plt.subplots(2, 2)

#axis[0, 0].plot(h1.log_Teff, h1.log_L, label='1Msol', color='w', alpha=0.25)
#axis[0, 0].plot(h2.log_Teff, h2.log_L, label='2Msol', color='w', alpha=0.25)
#axis[0, 0].plot(h4.log_Teff, h4.log_L, label='4Msol', color='w', alpha=0.25)
#axis[0, 0].plot(h8.log_Teff, h8.log_L, label='8Msol', color='w', alpha=0.25)
axis[0, 0].plot(h5.log_Teff, h5.log_L, label='5Msol', color='w')
axis[0, 0].plot(hDonor.log_Teff, hDonor.log_L, label='1', color='b')
axis[0, 0].set_title("HR Diagram Donor Star")
axis[0, 0].set_xlabel("log Effective Temperature")
axis[0, 0].set_ylabel("log Luminosity")
axis[0, 0].invert_xaxis()

#axis[0, 1].plot(h1.log_Teff, h1.log_L, label='1Msol', color='w', alpha=0.25)
#axis[0, 1].plot(h2.log_Teff, h2.log_L, label='2Msol', color='w', alpha=0.25)
#axis[0, 1].plot(h4.log_Teff, h4.log_L, label='4Msol', color='w', alpha=0.25)
#axis[0, 1].plot(h8.log_Teff, h8.log_L, label='8Msol', color='w', alpha=0.25)
axis[0, 1].plot(h1.log_Teff, h1.log_L, label='5Msol', color='w')
axis[0, 1].plot(hCompanion.log_Teff, hCompanion.log_L, label='2', color='r')
axis[0, 1].set_title("HR Diagram Companion Star")
axis[0, 1].set_xlabel("log Effective Temperature")
axis[0, 1].set_ylabel("log Luminosity")
axis[0, 1].invert_xaxis()

#axis[1, 0].loglog(p1.Rho, p1.T, label='1Msol', color='w', alpha=0.25)
#axis[1, 0].loglog(p2.Rho, p2.T, label='2Msol', color='w', alpha=0.25)
#axis[1, 0].loglog(p4.Rho, p4.T, label='4Msol', color='w', alpha=0.25)
#axis[1, 0].loglog(p8.Rho, p8.T, label='8Msol', color='w', alpha=0.25)
axis[1, 0].loglog(p5.Rho, p5.T, label='5Msol', color='w')
axis[1, 0].loglog(pDonor.Rho, pDonor.T, label='1', color='b')
axis[1, 0].set_title("TRho Graph Single Star")
axis[1, 0].set_xlabel("Density")
axis[1, 0].set_ylabel("Temperature")

#axis[1, 1].loglog(p1.Rho, p1.T, label='1Msol', color='w', alpha=0.25)
#axis[1, 1].loglog(p2.Rho, p2.T, label='2Msol', color='w', alpha=0.25)
#axis[1, 1].loglog(p4.Rho, p4.T, label='4Msol', color='w', alpha=0.25)
#axis[1, 1].loglog(p8.Rho, p8.T, label='8Msol', color='w', alpha=0.25)
axis[1, 1].loglog(p1.Rho, p1.T, label='5Msol', color='w')
axis[1, 1].loglog(pCompanion.Rho, pCompanion.T, label='2', color='r')
axis[1, 1].set_title("TRho Graph Companion Star")
axis[1, 1].set_xlabel("Density")
axis[1, 1].set_ylabel("Temperature")

'''
axis[2, 0].plot(hDonor.star_age, hDonor.star_mass, label='1', color='b')
axis[2, 0].set_title("Mass over time Donor Star")
axis[2, 0].set_xlabel("Time")
axis[2, 0].set_ylabel("Mass")

axis[2, 1].plot(hCompanion.star_age, hCompanion.star_2_mass, label='2', color='r')
axis[2, 1].set_title("Mass over time Companion Star")
axis[2, 1].set_xlabel("Time")
axis[2, 1].set_ylabel("Mass")

axis[3, 0].plot(hDonor.star_age, hDonor.log_R, label='1', color='b')
axis[3, 0].set_title("Radius over time Donor Star")
axis[3, 0].set_xlabel("Time")
axis[3, 0].set_ylabel("Radius")

axis[3, 1].plot(hCompanion.star_age, hCompanion.log_R, label='2', color='r')
axis[3, 1].set_title("Radius over time Companion Star")
axis[3, 1].set_xlabel("Time")
axis[3, 1].set_ylabel("Radius")
'''

# Combine all the operations and display
figure.tight_layout()
plt.show()

'''
plt.plot(hDonor.log_Teff, hDonor.log_L, label='1', color='b')
plt.plot(hCompanion.log_Teff, hCompanion.log_L, label='2', color='r')
plt.title("HR Diagram Donor Star")
plt.xlabel("log Effective Temperature")
plt.ylabel("log Luminosity")
plt.gca().invert_xaxis()
plt.show()
'''

