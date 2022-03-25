# Acceptable surface temperature range: 220K-320K
# Considering an idealized aquaplanet

import math
import numpy as np

consts = {'sigma' : 5.67e-08, # Stefan-Boltzmann constant (Wm^-2K^-4)
	'solarLuminosity' : 3.846e26, # (W)
	'alpha_ice' : 0.4,
	'alpha_ocean' : 0.3,
	'epsilon' : 0.5284,		# Substitutes for CO2 greenhouse effect.
	'T_o' : 280, # (K)
	'T_i' : 250,
	'au_conversion' : 1.496e11
}

def alphaMain(T_e):
	return consts.get('alpha_ice') - (consts.get('alpha_ice') - 
		consts.get('alpha_ocean'))*((T_e-consts.get('T_i'))/
		(consts.get('T_o')-consts.get('T_i')))**2
#return consts.get('alpha_ice') - (consts.get('alpha_ice')-consts.get('alpha_ocean')
#		*(T_e-consts.get(T)))

def olr(T_e):
	return consts.get('epsilon') * consts.get('sigma') * (T_e ** 4)

def irradiance(T_e):
	return (4 * olr(T_e))/(1-0.3)#alphaMain(T_e))

def inverseSquare_rOut(T_e):
	return (math.sqrt(consts.get('solarLuminosity')/
		(irradiance(T_e)*4*math.pi)))

T_bdry = [220,320]
zone_bdry = []
for t in T_bdry:
	zone_bdry.append(inverseSquare_rOut(t)/consts.get('au_conversion'))

print(alphaMain(220))
print(alphaMain(320))
#zone_bdry = zone_bdry.sort()
for i in zone_bdry:
	print(i)