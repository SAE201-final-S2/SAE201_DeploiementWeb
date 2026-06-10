from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

Base = declarative_base()

# ── Dimensions géographiques ────────────────────────────────────────────

class Region(Base):
    __tablename__ = "region"
    code = Column(String(10), primary_key=True)
    libelle = Column(String(100), nullable=False)
    departements = relationship("Departement", backref="region")
    def __repr__(self): return f"{self.code} – {self.libelle}"

class Departement(Base):
    __tablename__ = "departement"
    code = Column(String(10), primary_key=True)
    libelle = Column(String(100), nullable=False)
    region_code = Column(String(10), ForeignKey("region.code"), nullable=False)
    def __repr__(self): return f"{self.code} – {self.libelle}"

# ── Dimensions métier ────────────────────────────────────────────────

class ProfessionSante(Base):
    __tablename__ = "profession_sante"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(200), nullable=False, unique=True)
    def __repr__(self): return self.libelle

class TrancheAge(Base):
    __tablename__ = "tranche_age"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(100), nullable=False, unique=True)
    def __repr__(self): return self.libelle

class Sexe(Base):
    __tablename__ = "sexe"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(50), nullable=False, unique=True)
    def __repr__(self): return self.libelle

# ── Dimensions d’activité ──────────────────────────────────────────────

class TypeExercice(Base):
    __tablename__ = "type_exercice"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(200), nullable=False, unique=True)
    def __repr__(self): return self.libelle

class TypeSecteur(Base):
    __tablename__ = "type_secteur"
    code = Column(String(20), primary_key=True, nullable=False, unique=True)
    libelle = Column(String(200), nullable=False)
    def __repr__(self): return f"{self.code} – {self.libelle}"

 # ── Dimensions financières ──────────────────────────────────────────────

class TypeHonoraire(Base):
    __tablename__ = "type_honoraire"
    # Il n'y a plus de hiérarchie à 3 niveaux
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(200), nullable=False, unique=True)
    def __repr__(self): return self.libelle


class TypePrescription(Base):
    __tablename__ = "type_prescription"
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(200), nullable=False, unique=True)
    def __repr__(self): return self.libelle