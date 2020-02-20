import extinction
dust_dir = './'

# Assume you have a spectrum over some set of wavelengths
wavelengths = np.linspace(3000, 10000, 7001)
flux = 

av
rv = 3.1
e_bv = 0.2
av = rv * e_bv

mag_ext = extinction.fitzpatrick99(wavelengths, av, rv)
extincted_flux = flux * 10**(0.4 * mag_ext)
