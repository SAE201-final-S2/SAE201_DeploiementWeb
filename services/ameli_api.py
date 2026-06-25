import requests

class AmeliAPI:
    """Service d'accès à l'API data.ameli.fr."""
    BASE_URL = "https://data.ameli.fr/api/explore/v2.1/catalog/datasets"
    
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'Santéo/1.0'
        })
        
    def get_effectifs(self, profession, departement_code, annee):
        """Effectifs pour une profession, un département et une année.
        Retourne une liste de dictionnaires {annee, effectif, densite}.
        """
        where = (
            f"profession_sante=\"{profession}\" AND "
            f"departement=\"{departement_code}\" AND "
            f"year(annee)={annee} AND "
            f"libelle_classe_age=\"Tout âge\" AND "
            f"libelle_sexe=\"tout sexe\""
        )
        return self._requete(
            "demographie-effectifs-et-les-densites",
            {"select": "annee,effectif,densite", "where": where, "limit": 100},
        )
        
    def get_evolution_effectifs(self, profession, departement_code):
        """Effectifs sur toutes les années disponibles (pour un graphique)."""
        where = (
            f"profession_sante=\"{profession}\" AND "
            f"departement=\"{departement_code}\" AND "
            f"libelle_classe_age=\"Tout âge\" AND "
            f"libelle_sexe=\"tout sexe\""
        )
        return self._requete(
            "demographie-effectifs-et-les-densites",
            {"select": "annee,effectif,densite", "where": where,
             "order_by": "annee", "limit": 100},
        )
        
    def get_honoraires(self, profession, departement_code, annee, type_honoraire=None):
        """Honoraires pour une profession, un département et une année."""
        where = [
            f'profession_sante="{profession}"',
            f'departement="{departement_code}"',
            f'annee={annee}',
        ]
        if type_honoraire:
            where.append(f'type_honoraires_niveau_1="{type_honoraire.niveau_1}"')
            if type_honoraire.niveau_2:
                where.append(f'type_honoraires_niveau_2="{type_honoraire.niveau_2}"')
            if type_honoraire.niveau_3:
                where.append(f'type_honoraires_niveau_3="{type_honoraire.niveau_3}"')

        return self._requete(
            "honoraires-detailles",
            {
                "select": (
                    "annee,"
                    "profession_sante,"
                    "departement,"
                    "type_honoraires_niveau_1,"
                    "type_honoraires_niveau_2,"
                    "type_honoraires_niveau_3,"
                    "montant_honoraires,"
                    "montant_honoraires_moyens"
                ),
                "where": " AND ".join(where),
                "limit": 100,
            },
        )

    def get_evolution_honoraires(self, profession, departement_code, type_honoraire=None):
        """Évolution des honoraires pour une profession et un département."""
        where = [
            f'profession_sante="{profession}"',
            f'departement="{departement_code}"',
        ]
        if type_honoraire:
            where.append(f'type_honoraires_niveau_1="{type_honoraire.niveau_1}"')
            if type_honoraire.niveau_2:
                where.append(f'type_honoraires_niveau_2="{type_honoraire.niveau_2}"')
            if type_honoraire.niveau_3:
                where.append(f'type_honoraires_niveau_3="{type_honoraire.niveau_3}"')

        return self._requete(
            "honoraires-detailles",
            {
                "select": (
                    "annee,"
                    "montant_honoraires,"
                    "montant_honoraires_moyens"
                ),
                "where": " AND ".join(where),
                "order_by": "annee",
                "limit": 100,
            },
        )

    def get_prescriptions(self, profession, departement_code, annee, poste_prescription):
        """Prescriptions pour une profession, un département, une année et un poste."""
        where = (
            f'profession_sante="{profession}" AND '
            f'departement="{departement_code}" AND '
            f'year(annee)={annee} AND '
            f'poste_prescription="{poste_prescription}"'
        )
        return self._requete(
            "prescriptions",
            {
                "select": (
                    "annee,"
                    "poste_prescription,"
                    "libelle_poste_prescription,"
                    "montant_total_prescription,"
                    "montant_moyen_prescription"
                ),
                "where": where,
                "limit": 100,
            },
        )

    def get_evolution_prescriptions(self, profession, departement_code, poste_prescription):
        """Évolution des prescriptions pour une profession, un département et un poste."""
        where = (
            f'profession_sante="{profession}" AND '
            f'departement="{departement_code}" AND '
            f'poste_prescription="{poste_prescription}"'
        )
        return self._requete(
            "prescriptions",
            {
                "select": (
                    "annee,"
                    "montant_total_prescription,"
                    "montant_moyen_prescription"
                ),
                "where": where,
                "order_by": "annee",
                "limit": 100,
            },
        )

    def _requete(self, dataset, params):
        """Méthode privée : effectue une requête GET et gère les erreurs."""
        url = f"{self.BASE_URL}/{dataset}/records"
        try:
            resp = self._session.get(url, params=params)
            resp.raise_for_status()
            return resp.json().get("results", [])
        except requests.RequestException as e:
            print(f"[AmeliAPI] Erreur : {e}")
            return []