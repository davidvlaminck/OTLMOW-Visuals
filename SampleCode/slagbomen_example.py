from pathlib import Path

from otlmow_converter.OtlmowConverter import to_objects

from otlmow_visuals.PyVisWrapper import PyVisWrapper


def modify_html(file_path: Path) -> None:
    with open(file_path) as file:
        file_data = file.readlines()

    replace_index = -1
    for index, line in enumerate(file_data):
        if "drawGraph();" in line:
            replace_index = index
        # if '<div id="mynetwork" class="card-body">' in line:
        #     file_data[index] = file_data[index].replace('<div id="mynetwork" class="card-body">', '<div id="mynetwork" class="card-body" style="display:flex">')


    if replace_index > 0:
        file_data[replace_index] = file_data[replace_index].replace("drawGraph();",
                                                                    "var network = drawGraph();")
        file_data.insert(replace_index, "var container = document.getElementById('mynetwork');\n")
        file_data.insert(replace_index + 1,
                         "var isPhysicsOn = true;\n")
        file_data.insert(replace_index + 2,
                         "function disablePhysics(){\n")
        file_data.insert(replace_index + 3, "if(isPhysicsOn){")
        file_data.insert(replace_index + 4, 'newOptions={"physics":{"enabled":false}};\n')
        file_data.insert(replace_index + 5, "network.setOptions(newOptions)};\n;")
        file_data.insert(replace_index + 6, "isPhysicsOn = false;\n};\n")
        file_data.insert(replace_index + 7,
                         "container.addEventListener('mouseover', disablePhysics);\n")
    with open(file_path, 'w') as file:
        for line in file_data:
            file.write(line)


if __name__ == "__main__":
    # to run this example install the otlmow-converter in your local python environment
    html_path = Path("slagbomen_visual.html")
    objects = list(to_objects(Path("DA-2024-35924_export.xlsx")))

    PyVisWrapper().show(list_of_objects= objects,
                        html_path=html_path,  launch_html=False)

    modify_html(html_path)
