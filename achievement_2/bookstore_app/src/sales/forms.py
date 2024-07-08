from django import forms

# Stores the available choices for charts
CHART_CHOICES = (
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart")
)

# CBV "SalesSearchForm"
class SalesSearchForm(forms.Form):
    book_title = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
