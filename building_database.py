import os
from config import db
from website.models import sarampion_panama

# Data to initialize database with
VACUNAS = [
    {"year": 1960, "porcentage": '', 
    "country": '' , "code":''}
]

# Delete database file if it exists currently
if os.path.exists("parcial_2.db"):
    os.remove("parcial_2.db")



# iterate over the PEOPLE structure and populate the database
for vac in VACUNAS:
    p = sarampion_panama(
                            year=vac.get("year"), 
                            porcentage=vac.get("porcentage"),
                            country=vac.get("country"),
                            code=vac.get("code")
                            )
    db.session.add(p)



db.session.commit()