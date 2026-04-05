import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.app.models.aula import buscar_aula, criar_aula
from application.app.models.turma import buscar_todas_matriculas, buscar_todas_turma, buscar_turma
from application.database.connection import get_connection
from application.app.models.alunos import buscar_aluno_por_rfid

if get_connection():
    print("Connection successful") 
    try:
        RA_aluno = buscar_aluno_por_rfid("A1B2C3D4")
        print(RA_aluno)
        
        id_turma = str(buscar_turma(1, RA_aluno)[0])
        print(id_turma)

        criar_aula(id_turma)
        aula = buscar_aula(id_turma)
        print(str(aula))
        
    except Exception as e:
        print(f"An error occurred: {e}")
else:    
    print("Connection failed")