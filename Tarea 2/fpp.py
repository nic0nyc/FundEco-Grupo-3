import matplotlib.pyplot as plt
import numpy as np

# Parametros para el análisis

coeficienteTrabajoEconomiaChilena = 0.5
coeficienteTrabajoConstruccion = 0.8

#Parametros del código
ALPHA = 1 - coeficienteTrabajoEconomiaChilena   # capital share in economia chilena
BETA = 1 - coeficienteTrabajoConstruccion   # capital share in construccion
KBAR = 100  # Total capital supply
LBAR = 100  # Total labor supply

"""Función Producción Economía Chilena"""
def FuncionProduccionEconomiaChilena(capital, labour, alpha):
    
    return (capital**alpha)*(labour**(1 - alpha))

"""Función Producción Industria de la Construcción"""
def FuncionProduccionConstruccion(capital, labour, beta):
    
    return (capital**beta)*(labour**(1 - beta))

def edgeworth(L, Kbar=KBAR, Lbar=LBAR,alpha=ALPHA, beta=BETA):
    """efficiency locus: """
    a = (1-alpha)/alpha
    b = (1-beta)/beta
    return b*L*Kbar/(a*(Lbar-L)+b*L)

def ppf(LA,Kbar=KBAR, Lbar=LBAR,alpha=ALPHA,beta=BETA):
    """Draw a production possibility frontier
    
    arguments:
    LA -- labor allocated to ag, from which calculate QA(Ka(La),La) 
    """

    KA = edgeworth(LA, Kbar, Lbar, alpha, beta)
    RTS = (alpha/(1-alpha))*(KA/LA)
    QA = FuncionProduccionEconomiaChilena(KA, LA, alpha)
    QM = FuncionProduccionConstruccion(Kbar-KA, Lbar-LA, beta)
    #ax.scatter(QA,QM)
    La = np.arange(0,Lbar)
    Ka = edgeworth(La, Kbar, Lbar, alpha, beta)
    Qa = FuncionProduccionEconomiaChilena(Ka, La, alpha)
    Qm = FuncionProduccionConstruccion(Kbar-Ka, Lbar-La, beta)
    ax.set_xlim(0, Lbar)
    ax.set_ylim(0, Kbar)
    ax.plot(Qa, Qm, 'k-')
    ax.set_xlabel(r'$Q_E$', fontsize=18)
    ax.set_ylabel(r'$Q_C$', fontsize=18)
    plt.show()

fig, ax = plt.subplots(figsize=(7,6))
ppf(1)

#test