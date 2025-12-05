import os

TEMPLATE_PATH = "templates/car_comparison_template.html"

def generate_html(car1_data: dict, car2_data: dict) -> str:
    """Generate HTML from a template and two car data dictionaries."""

    if not os.path.exists(TEMPLATE_PATH):
        raise FileNotFoundError(f"Template file not found: {TEMPLATE_PATH}")

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders with actual data
    replacements = {
        "{{car1_model}}": car1_data.get("car_model", "Car 1"),
        "{{car2_model}}": car2_data.get("car_model", "Car 2"),
        "{{car1_summary}}": car1_data.get("Summary", ""),
        "{{car2_summary}}": car2_data.get("Summary", ""),
        "{{car1_engine}}": car1_data.get("Engine", ""),
        "{{car2_engine}}": car2_data.get("Engine", ""),
        "{{car1_fuel}}": car1_data.get("Fuel Type", ""),
        "{{car2_fuel}}": car2_data.get("Fuel Type", ""),
        "{{car1_transmission}}": car1_data.get("Transmission", ""),
        "{{car2_transmission}}": car2_data.get("Transmission", ""),
        "{{car1_power}}": car1_data.get("Max Power", ""),
        "{{car2_power}}": car2_data.get("Max Power", ""),
        "{{car1_torque}}": car1_data.get("Max Torque", ""),
        "{{car2_torque}}": car2_data.get("Max Torque", ""),
        "{{car1_mileage}}": car1_data.get("Mileage", ""),
        "{{car2_mileage}}": car2_data.get("Mileage", ""),
        "{{car1_price}}": car1_data.get("Price Range", ""),
        "{{car2_price}}": car2_data.get("Price Range", ""),
        "{{car1_features}}": car1_data.get("Key Features", ""),
        "{{car2_features}}": car2_data.get("Key Features", ""),
    }

    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)

    return template
