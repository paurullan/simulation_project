def principal:
    n_usuaris = X
    n_peticions_max = N
    tr = simulacio(n_usuaris, n_peticions_max)

def simulacio(n_usuaris, n_peticions_max):
    init
    mentre peticions < n_peticions_max:
        temporitzacio

def init:
    rellotge, temps_resposta, peticions = 0, 0, 0
    pobla(n_usuaris)

def temporitzacio:
    esdeveniment = selecciona(esdeveniments)
    rellotge = temps(esdevenimnet)
    processa(esdeveniment)

def processa(esdeveniment):
    opcio(esdeveniment):
        cpu    -> rutina_cpu
        disc   -> rutina_disc
        usuari -> rutina_usuari

def rutina_disc:
    genera_acces_cpu
    si la cua no es buida:
        decrementa(cua)
        genera_transaccio_disc

def rutina_cpu:
    possibilitat = aleatori( 1 / (n_transaccions_peticio + 1))
    si possibilitat:
        surt_a_reflexionar
    sino:
        genera_transaccio_disc

def rutina_usuari:
    genera_transaccio_cpu
    incrementa_peticions

def surt_a_reflexionar:
    acumulacio_estadistic
    genera_peticio_usuari

def acumulacio_estadistic:
    temps_reposta = rellotge - inici_peticio
