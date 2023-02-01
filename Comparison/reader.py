
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

# determine what mass donor and companion star are initially
Donor_star_mass_list = hDonor.star_mass
Companion_star_mass_list = hCompanion.star_mass
Donor_star_mass = Donor_star_mass_list[0]
Companion_star_mass = Companion_star_mass_list[0]
#print(Donor_star_mass, Companion_star_mass)

# state what single star data to use (1,2,4,5 or 8 Msol)
if Donor_star_mass <= 1:
	hd = h1
	ld = l1
	pd = p1
	Dmass = "1 Msol"
if Donor_star_mass > 1 and Donor_star_mass <= 2:
	hd = h2
	ld = l2
	pd = p2
	Dmass = "2 Msol"
if Donor_star_mass > 2 and Donor_star_mass <= 4:
	hd = h4
	ld = l4
	pd = p4
	Dmass = "4 Msol"
if Donor_star_mass > 4 and Donor_star_mass <= 5:
	hd = h5
	ld = l5
	pd = p5
	Dmass = "5 Msol"
if Donor_star_mass > 5:
	hd = h8
	ld = l8
	pd = p8
	Dmass = "8 Msol"

# same for companion
if Companion_star_mass <= 1:
	hc = h1
	lc = l1
	pc = p1
	Cmass = "1 Msol"
if Companion_star_mass > 1 and Companion_star_mass <= 2:
	hc = h2
	lc = l2
	pc = p2
	Cmass = "2 Msol"
if Companion_star_mass > 2 and Companion_star_mass <= 4:
	hc = h4
	lc = l4
	pc = p4
	Cmass = "4 Msol"
if Companion_star_mass > 4 and Companion_star_mass <= 5:
	hc = h5
	lc = l5
	pc = p5
	Cmass = "5 Msol"
if Companion_star_mass > 5:
	hc = h8
	lc = l8
	pc = p8
	Cmass = "8 Msol"
	
# set up figure
plt.style.use("dark_background")
figure, axis = plt.subplots(2, 2)

# HRD plots
axis[0, 0].plot(hd.log_Teff, hd.log_L, label='single star', color='w')
axis[0, 0].plot(hDonor.log_Teff, hDonor.log_L, label='1', color='b')
axis[0, 0].set_title(f"HR Diagram Donor Star ({Dmass})")
axis[0, 0].set_xlabel("log Effective Temperature")
axis[0, 0].set_ylabel("log Luminosity")
axis[0, 0].invert_xaxis()

axis[0, 1].plot(hc.log_Teff, hc.log_L, label='single star', color='w')
axis[0, 1].plot(hCompanion.log_Teff, hCompanion.log_L, label='2', color='r')
axis[0, 1].set_title(f"HR Diagram Companion Star ({Cmass})")
axis[0, 1].set_xlabel("log Effective Temperature")
axis[0, 1].set_ylabel("log Luminosity")
axis[0, 1].invert_xaxis()

# TRho plots
axis[1, 0].loglog(pd.Rho, pd.T, label='single star', color='w')
axis[1, 0].loglog(pDonor.Rho, pDonor.T, label='1', color='b')
axis[1, 0].set_title(f"TRho Graph Donor Star ({Dmass})")
axis[1, 0].set_xlabel("Density")
axis[1, 0].set_ylabel("Temperature")

axis[1, 1].loglog(pc.Rho, pc.T, label='single star', color='w')
axis[1, 1].loglog(pCompanion.Rho, pCompanion.T, label='2', color='r')
axis[1, 1].set_title(f"TRho Graph Companion Star ({Cmass})")
axis[1, 1].set_xlabel("Density")
axis[1, 1].set_ylabel("Temperature")

# Combine all the operations and display
figure.tight_layout()
plt.show()


figure, axis = plt.subplots(3, 2)

# Mass over time plots
axis[0, 0].plot(hDonor.star_age, hDonor.star_mass, label='1', color='b')
axis[0, 0].set_title(f"M/t Graph Donor Star ({Dmass})")
axis[0, 0].set_ylabel("Mass")
axis[0, 0].set_xlabel("Time")

axis[0, 1].plot(hCompanion.star_age, hCompanion.star_mass, label='2', color='r')
axis[0, 1].set_title(f"M/t Graph Companion Star ({Cmass})")
axis[0, 1].set_ylabel("Mass")
axis[0, 1].set_xlabel("Time")

# distance and orbital period
axis[1, 0].plot(hDonor.star_age, hDonor.period_days, label='1', color='b')
axis[1, 0].set_title(f"Period/t Graph Donor Star ({Dmass})")
axis[1, 0].set_ylabel("Period")
axis[1, 0].set_xlabel("Time")

axis[1, 1].plot(hCompanion.star_age, hCompanion.binary_separation, label='2', color='r')
axis[1, 1].set_title(f"Seperation/t Graph Companion Star ({Cmass})")
axis[1, 1].set_ylabel("Seperation")
axis[1, 1].set_xlabel("Time")

# star radii
axis[2, 0].plot(hd.star_age, hd.log_R, label='single star', color='w')
axis[2, 0].plot(hDonor.star_age, hDonor.log_R, label='1', color='b')
axis[2, 0].set_title(f"M/t Graph Donor Star ({Dmass})")
axis[2, 0].set_ylabel("Radius")
axis[2, 0].set_xlabel("Time")

axis[2, 1].plot(hc.star_age, hc.log_R, label='single star', color='w')
axis[2, 1].plot(hCompanion.star_age, hCompanion.log_R, label='2', color='r')
axis[2, 1].set_title(f"M/t Graph Companion Star ({Cmass})")
axis[2, 1].set_ylabel("Radius")
axis[2, 1].set_xlabel("Time")

# Combine all the operations and display
figure.tight_layout()
plt.show()
