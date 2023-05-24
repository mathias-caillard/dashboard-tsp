from config import *
from equivalence_historique import equivalence_titre, equivalence_ligne



def correspondance_equivalence(code_indicateur):
    if code_indicateur in equivalence_ligne:
        return True
    return False




