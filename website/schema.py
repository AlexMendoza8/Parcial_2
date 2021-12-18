from .ext import ma
from .models import sarampion_panama

class VacunasSchema(ma.SQLAlchemyAutoSchema): #Schema
    class Meta:
        model = sarampion_panama
        load_instance = True