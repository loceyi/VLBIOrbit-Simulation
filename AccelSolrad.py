# %--------------------------------------------------------------------------
# # %
# # % AccelSolrad: Computes the acceleration due to solar radiation pressure
# # %			   assuming the spacecraft surface normal to the Sun direction
# # %
# # % Inputs:
# # %   r           Spacecraft position vector
# # %   r_Earth	    Earth position vector (Barycentric)
# # %   r_Moon		Moon position vector (geocentric)
# # %   r_Sun       Sun position vector (geocentric)
# # %   r_SunSSB    Sun position vector (Barycentric)
# # %   Area        Cross-section
# # %   mass        Spacecraft mass
# # %   Cr          Solar radiation pressure coefficient
# # %   P0          Solar radiation pressure at 1 AU
# # %   AU          Length of one Astronomical Unit
# # %   shm         Shadow model (geometrical or cylindrical)
# # %
# # % Output:
# # %   a    		Acceleration (a=d^2r/dt^2)
# # %
# # % Notes:
# # %   r, r_sun, Area, mass, P0 and AU must be given in consistent units,
# # %   e.g. m, m^2, kg and N/m^2.
# # %
from Cylindrical import Cylindrical
from Shadow import Shadow
import numpy as np
from math import sqrt
def AccelSolrad(r,r_Earth,r_Moon,r_Sun,r_SunSSB,Area,mass,Cr,P0,AU,shm):

    # %        Moon wrt Earth  wrt=with regard to        pccor      rpc
    # %        Earth wrt Sun                             ccor       rc
    # %        Moon wrt Sun                              pscor      rps
    # %        Satellite wrt Earth                      sbcor      rsb
    # %        Satellite wrt Sun                        bcor       rb
    # %        Satellite wrt Moon                       sbpcor     rsbp
    pccor = r_Moon
    ccor = r_Earth-r_SunSSB
    pscor = r_Moon-r_Sun
    sbcor = r
    bcor = r-r_Sun
    sbpcor = r-r_Moon

    if shm=='cylindrical' :

        nu = Cylindrical(r,r_Sun)
    else:

        lambda_1, ecltyp= Shadow(pccor,ccor,pscor,sbcor,bcor,sbpcor)
        nu=lambda_1



    # % Acceleration
    norm_bcor=sqrt(np.dot(bcor,bcor))
    a = nu*Cr*(Area/mass)*P0*(AU*AU)*bcor/(norm_bcor**3)

    return a