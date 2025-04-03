class Mixture():

	def __init__(self,*args):

		super().__init__(*args)

	def quality(gas,liq):
		"""Returns mass quality of gas."""
		return gas/(gas+liq)

	def alpha(gas,liq):
		"""Returns volume quality of gas."""
		return gas/(gas+liq)
    
    def rho(rho_L,rho_G,alpha:float=0.5):
        """Returns mixture density based on void fraction."""
        return rho_L*(1-alpha)+rho_G*alpha
        
    def visc(visc_L,visc_G,x:float=0.5):
        """Returns mixture viscosity based on mass quality."""
        return visc_L*(1-x)+visc_G*x