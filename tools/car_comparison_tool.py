# tools/create_car_comparison_html_output.py
from schema.car_comparison_schema import CarComparisonHTMLOutput
from tools import generate_html
from tools import file_saver

def create_car_comparison_html_output(car1_data: dict, car2_data: dict) -> CarComparisonHTMLOutput:
    """
    Generates an HTML comparison page from two car research results, saves it,
    and returns the structured output matching CarComparisonHTMLOutput schema.
    """
    # 1️⃣ Generate HTML
    html_content = generate_html(car1_data, car2_data)

    # 2️⃣ Save HTML to 'html/' folder
    saved_file_path = file_saver(html_content, "car_comparison.html")

    # 3️⃣ Package into output schema
    # return CarComparisonHTMLOutput(
    #     html_content=html_content,
    #     saved_file_path=saved_file_path,
    #     output_key="car_comparison_html_output"
    # )
