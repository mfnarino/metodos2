import numpy as np
import matplotlib.pyplot as plt

def histograma_compara(n_personas):
    
    resultado = np.random.random(n_personas)
        
    ii_funciona = resultado < 0.75
    ii_no_funciona = resultado > 0.75
        
    resultado[ii_funciona] = 0
    resultado[ii_no_funciona] = 1
        
    funciona = len(resultado[resultado == 0])
    no_funciona = len(resultado[resultado == 1])
    
    x_1 = np.random.poisson(3, n_personas)
    si = np.random.poisson(2, funciona)
    no = np.random.poisson(3, no_funciona)
    x_2 = np.concatenate((si, no), axis = 0)
    
    plt.hist(x_1, bins = np.max(x_1), label = 'sin medicamento', rwidth=0.2, align='right')
    plt.hist(x_2, bins = np.max(x_2), label = 'con medicamento', rwidth=0.2)
    plt.xlabel('N gripas')
    plt.ylabel('N personas')
    plt.legend()
    plt.savefig('gripas.png')
    
histograma_compara(10000)