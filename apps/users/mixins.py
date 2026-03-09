from .utils import is_admin, is_editor

class RoleContextMixin:
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = is_admin(self.request.user)
        context['is_editor'] = is_editor(self.request.user)
        return context