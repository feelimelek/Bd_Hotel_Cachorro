from .Connection import postgree
from pydantic import BaseModel


class Dieta(BaseModel):
    dieta_id: int
    comida: str
    frequencia: str
    restricoes: str


def insertDieta(dieta: Dieta):
    conn = postgree()
    response = conn.mutation(
        f'INSERT INTO DIETA (DIETA_ID, COMIDA, FREQUENCIA, RESTRICOES) values ({dieta.dieta_id}, \'{dieta.comida}\', \'{dieta.frequencia}\', \'{dieta.restricoes}\');')
    print(f'insert \'dieta\' {dieta}')


def listDietas():
    conn = postgree()
    dietas = conn.query("""SELECT * FROM DIETA;""")
    print(f'list all \'dieta\'')
    return dietas


def updateDieta(dieta: Dieta):
    conn = postgree()
    print(f'update \'dieta\' {dieta}')
    return conn.mutation(
        f'UPDATE DIETA SET COMIDA = \'{dieta.comida}\', FREQUENCIA = \'{dieta.frequencia}\', RESTRICOES = \'{dieta.restricoes}\' WHERE DIETA_ID = \'{dieta.dieta_id}\';')


def deleteDieta(dieta_id: int):
    conn = postgree()
    print(f'delete \'dieta\' from id {dieta_id}')
    response = conn.mutation('DELETE FROM DIETA d WHERE d.DIETA_ID = dieta_id;')
    return response
