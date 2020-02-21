import extinction

import matplotlib.pyplot as plt
import numpy as np

import astropy.units as u
import astropy.constants as const


# Assume you have a spectrum over some set of wavelengths
wavelength = np.linspace(3000, 10000, 701) * u.angstrom
frequency = const.c / wavelength
frequency = frequency.to(u.Hz)
# Constant AB erg/s/cm^2/Hz
norm = 1000 * u.erg / u.s / u.cm ** 2
flux_density_frequency = norm / frequency
flux_density_wavelength = flux_density_frequency * const.c / wavelength ** 2
flux_density_wavelength = flux_density_wavelength.to(
    u.erg / u.s / u.cm ** 2 / u.angstrom
)

ax1 = plt.gca()
ax1.plot(
    wavelength,
    flux_density_wavelength,
    color="blue",
    ls="-",
    label="spectral flux density (lambda)",
)
ax1.set_xlabel(r"$\lambda [\AA]$")
ax1.set_ylabel(r"$\frac{dF}{d\lambda}$")
ax2 = ax1.twinx()
ax2.plot(
    wavelength,
    flux_density_frequency,
    color="blue",
    ls="--",
    label=r"spectral flux density (freq)",
)
ax2.set_xlabel(r"$\nu$ [Hz]$")
ax2.set_ylabel(r"$\frac{dF}{d\nu}$")
plt.legend()
plt.show()

# av
rv = 3.1
e_bv = 0.2
av = rv * e_bv

mag_ext = extinction.fitzpatrick99(wavelength.to(u.angstrom), av, rv)
extincted_flux_density_wavelength = flux_density_wavelength * 10 ** (-0.4 * mag_ext)

plt.clf()
ax1 = plt.gca()

ax1.plot(
    wavelength, flux_density_wavelength, color="blue", label="Flux density (wavelength)"
)
ax1.plot(
    wavelength,
    extincted_flux_density_wavelength,
    color="orange",
    label="Extincted flux density (wavelength)\nR_V=3.1, E(B-V)=0.2",
)
ax1.set_xlabel(r"$\lambda [\AA]$")
ax1.set_ylabel(r"$\frac{dF}{d\lambda}$ [erg/s/cm$^2$/$\AA$]")
plt.legend()
plt.show()
