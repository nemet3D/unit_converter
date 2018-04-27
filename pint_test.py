import pint
u = pint.UnitRegistry()
q = u.Quantity

c = 2.998 * (10**8) * u.m / u.sec
c_converted = c.to('km/hour')
print('Viteaz luminii in metri pe secunda este: {} . Convertit in kilometri pe ora este {} .' .format(c, c_converted))

rho = 62.4 * u.lb / u.ft**3
rho_converted = rho.to('kg/m**3')
print('Densitatea in lb pe ft cub este: {} . Convertit in kilograme pe metru cub este {} .' .format(rho, rho_converted))

Rg = 0.08206 * u.(L*atm) / u.(mole*K)
Rg_converted = Rg.to('J/mole')
print('Constanta gazului ideal este: {} . Convertit in kilograme pe metru cub este {} .' .format(Rg, Rg_converted))

rho = 62.4 * u.lb / u.ft**3
rho_converted = rho.to('kg/m**3')
print('Densitatea in lb pe ft cub este: {} . Convertit in kilograme pe metru cub este {} .' .format(rho, rho_converted))
