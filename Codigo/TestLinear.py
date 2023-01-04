from Linear import Linear
INPUT_SIZE    = 784
MIDDLE_SIZE   = 300
OUTPUT_SIZE   = 10

H1 = Linear(INPUT_SIZE,MIDDLE_SIZE)
H2 = Linear(MIDDLE_SIZE,OUTPUT_SIZE)

def forward(X):
    A1  = H1.forward(X)
    A2  = H2.forward(A2)
    return A2

#gamma learning rate
def backward(ERR,gamma):
    #internamente de estas funciones
    #se van corrigiendo los pesos
    B2 = H2.backward(ERR,gamma)
    B1 = H1.backward(B2,gamma)
    