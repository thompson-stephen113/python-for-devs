from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from .forms import SalesSearchForm
from .models import Sale
from .utils import get_bookname_from_id, get_chart

# Create your views here.
# FBV "home"
def home(request):
    return render(request, "sales/home.html")

# FBV "records", protected
@login_required
def records(request):
    # Creates an instance of SalesSearchForm
    form = SalesSearchForm(request.POST or None)

    # Initializes dataframe to None
    sales_df = None

    # Initializes chart to None
    chart = None

    # Checks if the Search button is clicked
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        chart_type = request.POST.get("chart_type")

        # Applies filter to extract data
        qs = Sale.objects.filter(book__name=book_title)

        # Checls if data is found
        if qs:
            # Converts queryset values to pandas dataframe
            sales_df = pd.DataFrame(qs.values())

            # Converts ID to Name of book
            sales_df["book_id"] = sales_df["book_id"].apply(get_bookname_from_id)
            
            # Calls get_chart by passing chart_type from user input, sales dataframe, and labels
            chart = get_chart(chart_type, sales_df, labels=sales_df["book_id"].values)

            # Converts dataframe to HTML
            sales_df = sales_df.to_html()

        '''
        print(book_title, chart_type)

        # Querysets
        print("Exploring querysets:")

        # Case 1
        print("Case 1: Output of Sale.objects.all()")
        qs = Sale.objects.all()
        print(qs)

        # Case 2
        print("Case 2: Output of Sale.objects.filter(book__name=book_title)")
        qs = Sale.objects.filter(book__name=book_title)
        print(qs)

        # Case 3
        print("Case 3: Output of qs.values")
        print(qs.values())

        # Case 4
        print("Case 4: Output of qs.values_list()")
        print(qs.values_list())

        # Case 5
        print("Case 5: Output of Sale.objects.get(id=1)")
        obj = Sale.objects.get(id=1)
        print(obj)
        '''

    # Prepares data to send from view to template
    context = {
        "form": form,
        "sales_df": sales_df,
        "chart": chart,
    }

    # Loads records page using "context" information
    return render(request, "sales/records.html", context)
