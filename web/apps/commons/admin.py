from model_controller.admins import ModelControllerAdmin

from web.apps.commons.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS


class SoftModelControllerAdmin(ModelControllerAdmin):
    exclude = EXCLUDE_MODEL_CONTROLLER_FIELDS + ('alive', )