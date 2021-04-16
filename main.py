import os
from dotenv import load_dotenv

from services.ClauseCatalogService import ClauseCatalogService

load_dotenv()
CLAUSE_CATALOG_HOST = os.getenv("CLAUSE_CATALOG_HOST")
CLAUSE_CATALOG_PORT = os.getenv("CLAUSE_CATALOG_PORT")


if __name__ == '__main__':
    agreement_service = ClauseCatalogService(CLAUSE_CATALOG_HOST, CLAUSE_CATALOG_PORT)
    agreement_service.populate_db()

