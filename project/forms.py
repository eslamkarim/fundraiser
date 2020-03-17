from django import forms

from project.models import Category, Tag
import datetime

class DateInput(forms.DateInput):
      input_type = 'date'

class ContactForm(forms.Form):
      project_title = forms.CharField(max_length=100, label='Project Title')
      details = forms.CharField(label='Project Details',widget=forms.Textarea)
      category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,initial=Category.objects.all()[0])
      target = forms.IntegerField(min_value=1,max_value=1000000000)
      tags = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,queryset=Tag.objects.all())
      start_date = forms.DateField(widget=DateInput,initial=datetime.date.today,required=True)
      end_date = forms.DateField(widget=DateInput,initial=datetime.date.today,required=True)
      
      
      def clean_project_title(self):
            project_title = self.cleaned_data['project_title']
            if len(project_title) == 0:
                  raise forms.ValidationError("project title can't be empty ")
            if len(project_title) >100:
                  raise forms.ValidationError("project title can't be more than 100 character ")
            return project_title
      
      def clean_details(self):
            details = self.cleaned_data['details']
            if len(details) == 0:
                  raise forms.ValidationError("project title can't be empty ")
            return details
      
      def clean_category(self):
            category = self.cleaned_data['category']
            try:
                  Category.objects.get(name = category)
            except:
                  raise forms.ValidationError("please choose from list")
            return category
      
      def clean_target(self):
            target = self.cleaned_data['target']
            if target <= 0:
                  raise forms.ValidationError("project title can't lower than 1 ")
            if target > 1000000000:
                  raise forms.ValidationError("project title can't be more than 1000000000 ")
            return target
      
      def clean_tags(self):
            tags = self.cleaned_data['tags']
            for val in tags:
                  try:
                        Tag.objects.get(name=val)
                  except:
                        raise forms.ValidationError("please choose from list")
            return tags
                  
      
      def clean_start_date(self):
            start_date = self.cleaned_data['start_date']
            print("Date = ",start_date)
            if (start_date-datetime.date.today()).days < 0:
                  raise forms.ValidationError("Start date can't be in the past")
            return start_date

      def clean_end_date(self):
            end_date = self.cleaned_data['end_date']
            if self.cleaned_data.get('start_date')==None:
                  return end_date
            start_date = self.cleaned_data['start_date']
            print("Date = ",end_date)
            if (end_date-start_date).days <= 0:
                  raise forms.ValidationError("end date must be after start Date")
            return end_date