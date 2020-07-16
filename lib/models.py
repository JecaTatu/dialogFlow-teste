from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

from django.db import models
from django.utils.translation import ugettext_lazy as _

#
# Model mixins
#

class TimeStampedMixin(models.Model):
    """
    Add timestamp control to a model.
    """
    created_at = AutoCreatedField(_('criado em'))
    updated_at = AutoLastModifiedField(_('modificado em'))

    class Meta:
        abstract = True


#
# Model base classes with mixin combinations
#

class BaseModel(TimeStampedMixin, models.Model):
    """
    An abstract base class model with timestamp control added.
    """
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)


class BaseSafeDeleteModel(BaseModel, SafeDeleteModel):
    """
    An abstract base class model that provides both timestamp
    and safe delete functionality.
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        abstract = True
