from sqlalchemy.orm import Session
from app.models import Organization
from app.schemas import OrganizationCreate

def create_organization(db: Session, organization: OrganizationCreate):
    db_organization = Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization