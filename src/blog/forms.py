from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
    
    
class BlogPostModelForm(forms.ModelForm):
    title = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']
        
        
    def clean_title(self, *args, **kwargs):
        instance = self.instance

        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # same thing as: id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used...try again!")
        return title
    
    