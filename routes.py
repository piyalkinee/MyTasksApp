from fastapi import APIRouter

from modules.appinit import controller as appinit_controller
from modules.tasks import controller as tasks_controller

routes = APIRouter()

routes.include_router(appinit_controller.routes)
routes.include_router(tasks_controller.routes)