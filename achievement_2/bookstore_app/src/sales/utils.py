from io import BytesIO
import base64
import matplotlib.pyplot as plt
from books.models import Book

# Defines function that gets book name from its ID
def get_bookname_from_id(val):
    bookname = Book.objects.get(id=val)
    return bookname

# Defines function to create graph
def get_graph():
    # Creates a BytesIO buffer for the image
    buffer = BytesIO()

    # Creates plot with a BytesIO object as a file-like object
    plt.savefig(buffer, format="png")

    # Sets cursor to beginning of the stream
    buffer.seek(0)

    # Retrieves content of the file
    image_png = buffer.getvalue()

    # Encodes the bytes-like object
    graph = base64.b64encode(image_png)

    # Decodes to get the string as output
    graph = graph.decode("utf-8")

    # Frees up the memory of buffer
    buffer.close()

    # Returns the image/graph
    return graph

# Defines function to implement logic to prepare the chart based on user input
def get_chart(chart_type, data, **kwargs):
    # Switches plot backend to Anti-Grain Geometry to write to file
    plt.switch_backend("AGG")

    # Specifies figure size
    fig = plt.figure(figsize=(6,3))

    # Selects chart_type based on user input from form
    if chart_type == "#1":
        # Plots bar chart between date on x-axis and quantity on y-axis
        plt.bar(data["date_created"], data["quantity"])
    
    elif chart_type == "#2":
        # Generates pie chart based on price with book titles as labels
        labels = kwargs.get("labels")
        plt.pie(data["price"], labels=labels)

    elif chart_type == "#3":
        # Plots line chart based on date on x-axis and price on y-axis
        plt.plot(data["date_created"], data["price"])

    else:
        print("Unknown chart type")

    # Specifies layout details
    plt.tight_layout()

    # Returns the graph to file
    chart = get_graph()
    return chart
