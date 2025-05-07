from fastapi import Depends, APIRouter
from app.api.deps import get_db
from app.crud import organization
from app.schemas import OrganizationCreate
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/organizations/")
def create_organization_endpoint(organization: OrganizationCreate, db: Session = Depends(get_db)):
    return organization.create_organization(db=db, organization=organization)