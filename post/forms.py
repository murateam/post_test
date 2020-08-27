from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML

from .models import Post

from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from django.conf import settings


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'image')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()



		self.helper.form_show_labels = False
		# self.helper.disable_csrf = True
		self.helper.layout = Layout(
			'title',
			'body',
			'image',
			HTML("""{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.imagefile.value }}">{% endif %}""")
		)