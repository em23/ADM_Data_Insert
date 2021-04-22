import os
from dotenv import load_dotenv

from services.ClauseCatalogService import ClauseCatalogService
from services.TemplateCatalogService import TemplateCatalogService

load_dotenv()
CLAUSE_CATALOG_HOST = os.getenv("CLAUSE_CATALOG_HOST")
CLAUSE_CATALOG_PORT = os.getenv("CLAUSE_CATALOG_PORT")
TEMPLATE_CATALOG_HOST = os.getenv("TEMPLATE_CATALOG_HOST")
TEMPLATE_CATALOG_PORT = os.getenv("TEMPLATE_CATALOG_PORT")


if __name__ == '__main__':
    clause_service = ClauseCatalogService(CLAUSE_CATALOG_HOST, CLAUSE_CATALOG_PORT)
    clause_service.populate_db()

    template_service = TemplateCatalogService(TEMPLATE_CATALOG_HOST, TEMPLATE_CATALOG_PORT)
    template_service.populate_db()



