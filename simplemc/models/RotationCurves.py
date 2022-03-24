
from simplemc.cosmo.paramDefs import Anfw_par, rs_par
from simplemc.functions_LBS import *
import numpy as np
from scipy import interpolate


class RotationCurves():
    def __init__(self, varya= True, varyb= True):
        """
        Class to constrain rotational curves profiles,
            Here we assume a NFW profile
        Parameters
        ----------
        varya
        varyb

        Returns
        -------

        """
        ## Example used to fit a straigth line two parameters: a, b
        self.varya = varya
        self.varyb = varyb
       

        self.Anfw = Anfw_par.value
        self.rs = rs_par.value
        


    # my free params (parameters/priors see ParamDefs.py)
    def freeParameters(self):
        l = []
        if (self.varya): l.append(Anfw_par)
        if (self.varyb): l.append(rs_par)
        return l

    def printFreeParameters(self):
        print("Free parameters and values currently accepted:")
        self.printParameters(self.freeParameters())


    def printParameters(self, params):
        for p in params:
            print(p.name, '=' , p.value , '+/-' , p.error)


    def updateParams(self, pars):
        for p in pars:
            if p.name == "Anfw":
                self.Anfw = p.value
            elif p.name == "rs":
                self.rs = p.value
        return True


    #def rotation(self,x):
        #def nfw(r, rs =1, A=0.05):
       # A  = self.Anfw
        #rs = self.rs
        #return (A**2*(rs**3)/x)*(np.log((rs+x)/rs) - x/(rs+x))
    #l=0 function
    def rotation(self,x):
        A = self.Anfw
        rs = self.rs
        m_a = 10.**(A)
        eps = 10.**(rs)
        Vc = Vc_xy(x,m_a,eps)
    #If you want to use np.arange in the previous function, It is recommended to use extrapolate
        f = interpolate.interp1d(Vc[0],Vc[1],fill_value='extrapolate')
        Vc_new = f(x)
        return Vc_new
    #l=0 + l=1 + l=2 function multi
    def rotation(self,x):
       # A = self.Anfw
        #rs = self.rs
        #phi0 = self.phi0
        #phi1 = self.phi1
        #phi2 = self.phi2

        #m_a = 10.**(A)
        #eps0 = 10.**(rs)
        #phi0 = 10.**(phi0)
        #phi1 = 10.**(phi1)
        #phi2 = 10.**(phi2)
        #Vc2 = Vc_inter(x,m_a,eps0,phi0,phi1,phi2)
        #return np.sqrt(Vc2)


    def prior_loglike(self):
        return 0
