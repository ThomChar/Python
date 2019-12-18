import datetime
import math

class Markov1:
 
    def __init__(self,lamb, mu):
        self.lamb = lamb
        self.mu = mu
        self.rho = self.__ro__()
        self.tmpsServ = self.__tempsMoyService__()
        self.L = self.__nbreMoyClientSysteme__()
        self.Lq = self.__nbreMoyClientFile__()
        self.s = round((1/(1-self.rho))-1,5)
        self.q0 = self.__aucunClientFile__()
        self.w = self.__dureeMoyAttenteSysteme__()
        self.wq = self.__dureeMoyAttenteFile__()
    
    def __ro__(self):
        return round(self.lamb/self.mu,5)

    def __tempsMoyService__(self):
        return round(1/self.mu,5)
    
    def __nbreMoyClientSysteme__(self):
        return round(self.lamb/(self.mu-self.lamb),5)
    
    def __nbreMoyClientFile__(self):
        return round(pow(self.lamb,2)/(self.mu*(self.mu-self.lamb)),5)

    def __aucunClientFile__(self):
        return round(1-self.rho,5)
    
    def __jClientFile__(self,j):
        return round(pow(self.rho,j)*(1-self.rho),5)
    
    def __dureeMoyAttenteSysteme__(self):
        return round(1/(self.mu-self.lamb),5)

    def __dureeMoyAttenteFile__(self):
        return round(self.lamb/(self.mu*(self.mu-self.lamb)),5)
    
    def __tempsSejourSysteme__(self,t):
        return round(math.exp(-self.mu*(1-self.rho)*t),5)

class Markov1K:
 
    def __init__(self,lamb,mu,k):
        self.lamb = lamb
        self.mu = mu
        self.K = k
        self.rho = self.__ro__()
        self.tmpsServ = self.__tempsMoyService__()
        self.L = self.__nbreMoyClientSysteme__()
        self.q0 = self.__jClientFile__(0)
        self.Lq = self.__nbreMoyClientFile__()
        self.s = round((1/(1-self.rho))-1,5)
        self.w = self.__dureeMoyAttenteSysteme__()
        self.wq = self.__dureeMoyAttenteFile__()
    
    def __ro__(self):
        return round(self.lamb/self.mu,5)

    def __tempsMoyService__(self):
        return round(1/self.mu,5)
    
    def __nbreMoyClientSysteme__(self):#a été changé
        if(self.rho == 1):
            return round(self.K/2,5)
        else:
            return round((self.rho*(1-(self.K+1)*pow(self.rho,self.K)+self.K*pow(self.rho,self.K+1)))/((1-self.rho)*(1-pow(self.rho,self.K+1))),5)
    
    def __nbreMoyClientFile__(self):#Change peut être
        return round(self.L-(1-self.q0),5)
    
    def __jClientFile__(self,j): #Change
        if(self.rho == 1):
            return round(1/(self.K+1),5)
        else:
            return round(((1-self.rho)*pow(self.rho,j))/(1-pow(self.rho,self.K+1)),5)
    
    def __dureeMoyAttenteSysteme__(self):
        return round(1/(self.mu-self.lamb),5)

    def __dureeMoyAttenteFile__(self):
        return round(self.lamb/(self.mu*(self.mu-self.lamb)),5)
    
    def __tempsSejourSysteme__(self,t):
        return round(math.exp(-self.mu*(1-self.rho)*t),5)

class MarkovS:
 
    def __init__(self,lamb, mu, s):
        self.lamb = lamb
        self.mu = mu
        self.S = s
        self.rho = self.__ro__()
        self.tmpsServ = self.__tempsMoyService__()
        self.q0 = self.__aucunClientFile__()
        self.Lq = self.__nbreMoyClientFile__()
        self.wq = self.__dureeMoyAttenteFile__()
        self.w = self.__dureeMoyAttenteSysteme__()
        self.L = self.__nbreMoyClientSysteme__()
    
    def __ro__(self):
        return round(self.lamb/(self.S*self.mu),5)

    def __tempsMoyService__(self):
        return round(1/self.mu,5)
    
    def __nbreMoyClientSysteme__(self):
        return round(self.lamb*self.w,5)
    
    def __nbreMoyClientFile__(self):
        return round(self.q0*(pow(self.rho*self.S,self.S)*self.rho)/(math.factorial(self.S)*pow(1-self.rho,2)),5)

    def __aucunClientFile__(self):
        res = 0
        tmp = pow(self.rho*self.S,self.S)/(math.factorial(self.S)*(1-self.rho))
        for j  in range(0,self.S):
            res = res + (pow(self.rho*self.S,j)/math.factorial(j))
        resfinal = 1/(res+tmp)
        return round(resfinal,5)
    
    def __jClientFile__(self,j):
        if(j >= 0 and j < self.S):
            return round(self.q0*(pow(self.rho*self.S,j)/math.factorial(j)),5)
        else:
            return round(self.q0*(pow(self.S,self.S)*pow(self.rho,j)/math.factorial(self.S)),5)
    
    def __dureeMoyAttenteSysteme__(self):
        return round(self.wq+(1/self.mu),5)

    def __dureeMoyAttenteFile__(self):
        return round(self.Lq/self.lamb,5)
    
    def __tempsSejourSysteme__(self,t):
        expression1 = self.q0 *(pow(self.rho*self.S,self.S)/(math.factorial(self.S)*(1-self.rho)))
        expression2 = (1-math.exp(-self.mu*t*(self.S-1-(self.rho*self.S))))/(self.S-1-(self.rho*self.S))
        return round(math.exp(-self.mu*t)*(1+ (expression1*expression2)),5)

    def __DureeAttenteSansService__(self,t):
        if(t==0):
            return round((self.q0*pow(self.rho*self.S,self.S))/(math.factorial(self.S)*(1-self.rho)),5)
        else:
            return round((math.exp(-self.S*self.mu*t*(1-self.rho)))*self.__DureeAttenteSansService__(0),5)