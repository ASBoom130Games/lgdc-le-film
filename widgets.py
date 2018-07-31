from django import forms
from django.forms.utils import flatatt
from django.forms import
from django.utils.safestring import mark_safe

class user(forms.CharField):
    def render(self, name, value, attrs=None):
        super().render(name, value, attrs)
        flat_attrs = flatatt(attrs)
        html = '''
      <div class="md-form form-sm mb-5">
      <i class="fa fa-envelope prefix"></i>
     <input %(attrs)s type="email" class="form-control form-control-sm validate" value="%(value)s">
    <label data-error="wrong" data-success="right" for="modalLRInput10">Nom d'utilisateur</label>
</div>
        ''' % {
            'attrs': flat_attrs,
            'id': attrs['id'],
            'value': value,
        }
        return mark_safe(html)