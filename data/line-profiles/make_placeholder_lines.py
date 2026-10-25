# PLACEHOLDER Fe K-alpha line profiles for three coronal geometries.
# Toy model: thin Keplerian disc around a Schwarzschild BH, no light bending,
# flat-space emissivity from each corona shape. Replace with real Gradus/Kerrz output.
import numpy as np, sys
out = sys.argv[1]
E0, inc, H = 6.4, np.radians(30), 3.0
r = np.geomspace(2.0, 400, 1500); phi = np.linspace(0, 2*np.pi, 720, endpoint=False)
R, P = np.meshgrid(r, phi, indexing='ij')
def ring(rr, a, h):
    if a == 0: return h/(rr**2+h**2)**1.5
    ph = np.linspace(0, 2*np.pi, 200, endpoint=False)
    return np.mean(h/(rr[:,None]**2+a**2-2*rr[:,None]*a*np.cos(ph)+h**2)**1.5, 1)
em = {
 'lamppost': ring(r, 0, H),
 'ring':     ring(r, 8.0, H),
 'disc':     sum(a*ring(r, a, H) for a in np.linspace(0.5, 15, 25)),
}
g = np.sqrt(1-1.5/R) / (1 + R**-0.5*np.sin(inc)*np.sin(P))
dA = (R*np.gradient(r)[:,None]) * (2*np.pi/len(phi))
E = np.linspace(2.5, 8.5, 301)
for name, e in em.items():
    w = (e[:,None]*g**4*dA).ravel()
    F, _ = np.histogram((g*E0).ravel(), bins=np.append(E-0.01, E[-1]+0.01), weights=w)
    F = np.convolve(F, np.ones(3)/3, mode='same'); F /= F.max()
    np.savetxt(f'{out}/{name}.txt', np.c_[E, F], fmt='%.4f',
               header=f'PLACEHOLDER toy profile ({name} corona). Columns: energy [keV], flux [arb.]')
print('ok')
