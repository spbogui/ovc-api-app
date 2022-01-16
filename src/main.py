import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.routers.authentication import auth
from src.routers.social_center import social_center
from src.routers.user import user
from src.routers.school_folowup import school_followup
from src.routers.nutritional_followup import nutritional_followup
from src.routers.member_identification import member
from src.routers.household_identification import household
from src.routers.reference import reference
from src.routers.support_activity import activity
from src.routers.member_evaluation import evaluation
from src.routers.household_structure import household_structure
from src.routers.household_evaluation import household_evaluation
from src.routers.graduation import graduation
from src.routers.graduation_service import graduation_service
from src.routers.structure import structure
# from src.routers.migration import migration

app = FastAPI()

origins = ["*"]

app.include_router(auth)
app.include_router(user)
app.include_router(household)
app.include_router(household_evaluation)
app.include_router(graduation)
app.include_router(graduation_service)
app.include_router(household_structure)
app.include_router(member)
app.include_router(evaluation)
app.include_router(activity)
app.include_router(school_followup)
app.include_router(nutritional_followup)
app.include_router(reference)
# app.include_router(counter_reference)
app.include_router(social_center)
app.include_router(structure)
# app.include_router(migration)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, access_log=True)
