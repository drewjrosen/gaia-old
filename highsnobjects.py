import astropy
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
from mpl_toolkits.mplot3d import Axes3D
import sys, os, time, string, math, commands, subprocess

#read in data from Gaia catalog
file=fits.open('tgas-source.fits')
data_list=file[1]


#Pull data we want from .fits file

#Parallax data
parallax=data_list.data['parallax'] #in mas
parallax_error=data_list.data['parallax_error'] #error

#proper motion
propermotion_ra=data_list.data['pmra']
propermotion_dec=data_list.data['pmdec']

#RA and DEC
ra=data_list.data['ra']
dec=data_list.data['dec']



#calculate SN ratio
ratio=parallax/parallax_error

#select high SN data that we want
highSNindices = ratio > 16.

#locations of data we want
#np.where(highSNindices)

#distances we want from high SN data
distance=1./parallax[highSNindices] #in Kpc

#Calculate transverse velocity in RA and DEC then in real space
transv_ra=4.74*propermotion_ra[highSNindices]*distance #km/s
transv_dec=4.74*propermotion_dec[highSNindices]*distance #km/s

transverse_vsqared=transv_ra**2+transv_dec**2
transverse_v=transverse_vsqared**(.5)


#test add

#plotting

#distance distribution
plt.hist(distance,bins=100,log=True)
plt.show()

#Relative velocity distribution
plt.hist(transverse_v,bins=100,log=True)
plt.show()
plt.savefig('highsnVelocities.png')

#3D Map of selected stars
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(ra[highSNindices],dec[highSNindices],distance)
plt.show()
plt.savefig('highsn3Dmap.png')

