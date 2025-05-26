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
        # file_data[replace_index] = file_data[replace_index].replace("drawGraph();",
        #                                                             "var network = drawGraph();")
        # file_data.insert(replace_index, "var container = document.getElementById('mynetwork');\n")
        # file_data.insert(replace_index + 1,
        #                  "var isPhysicsOn = true;\n")
        # file_data.insert(replace_index + 2,
        #                  "function disablePhysics(){\n")
        # file_data.insert(replace_index + 3, "if(isPhysicsOn){")
        # file_data.insert(replace_index + 4,
        #                  'newOptions={"layout":{"hierarchical":{"enabled":false}}};\n')
        # file_data.insert(replace_index + 5, "network.setOptions(newOptions);\n")
        # file_data.insert(replace_index + 6,
        #                  'newOptions={\"physics\":{\"enabled\":false}};\n AddEdge("bareel", "licht","#000000","to");\n')
        # file_data.insert(replace_index + 7, "network.setOptions(newOptions);\n")
        # file_data.insert(replace_index + 8, "isPhysicsOn = false;\n}};\n")
        # file_data.insert(replace_index + 9,
        #                  "container.addEventListener('mouseover', disablePhysics);\n")
        #
        # file_data.insert(replace_index + 10,"function AddEdge(from_id, to_id,color,arrow)")
        # file_data.insert(replace_index + 11,"{")
        # file_data.insert(replace_index + 12,    'network.body.data.edges.add([{'
        #            ' "arrowStrikethrough": false,'
        #             '"arrows": arrow,'
        #            ' "color": color,'
        #             '"from": from_id,'
        #             '"label": "beheerder",'
        #           '  "smooth": {'
        #                ' "enabled": false'
        #         '    },'
        #     '        "to": to_id,'
        #      '       "width": 2'
        #         '}]);')
        # file_data.insert(replace_index + 13,"}")
        #
        # file_data.insert(replace_index + 14, "function AddEdgeWithLabel(from_id, to_id,color,arrow,label)")
        # file_data.insert(replace_index + 15, "{")
        # file_data.insert(replace_index + 16, 'network.body.data.edges.add([{'
        #                                      ' "arrowStrikethrough": false,'
        #                                      '"arrows": arrow,'
        #                                      ' "color": color,'
        #                                      '"from": from_id,'
        #                                      '"label": label,'
        #                                      '  "smooth": {'
        #                                      ' "enabled": false'
        #                                      '    },'
        #                                      '        "to": to_id,'
        #                                      '       "width": 2'
        #                                      '}]);')
        # file_data.insert(replace_index + 17, "}\n")
        # file_data.insert(replace_index + 18,
        #                  "container.addEventListener(\'click\', (event) => {console.log('hey')});\n")

        add_data = [ "var container = document.getElementById('mynetwork');",
                         "var isPhysicsOn = true;",
                         "function disablePhysics(){",
                        "if(isPhysicsOn){",

                         'newOptions={"layout":{"hierarchical":{"enabled":false}}};\n',
         "network.setOptions(newOptions);",

                         'newOptions={\"physics\":{\"enabled\":false}};\n',
         "network.setOptions(newOptions);",
         "isPhysicsOn = false;\n}};",

                         "container.addEventListener('mouseover', disablePhysics);",

         "function AddEdge(from_id, to_id,color,arrow)",
         "{",
         'network.body.data.edges.add([{'
                                             ' "arrowStrikethrough": false,'
                                             '"arrows": arrow,'
                                             ' "color": color,'
                                             '"from": from_id,'
                                             '"label": "beheerder",'
                                             '  "smooth": {'
                                             ' "enabled": false'
                                             '    },'
                                             '        "to": to_id,'
                                             '       "width": 2'
                                             '}]);',
         "}",


                         "function AddEdgeWithLabel(from_id, to_id,color,arrow,label)",
         "{",
         'network.body.data.edges.add([{'
                                             ' "arrowStrikethrough": false,'
                                             '"arrows": arrow,'
                                             ' "color": color,'
                                             '"from": from_id,'
                                             '"label": label,'
                                             '  "smooth": {'
                                             ' "enabled": false'
                                             '    },'
                                             '        "to": to_id,'
                                             '       "width": 2'
                                             '}]);',
         "}"]


        # file_data.insert(replace_index + 14,"AddEdge('bareel', 'licht');")
        replace_and_add_lines(file_data, replace_index,
                                 "drawGraph();",
                                 "var network = drawGraph();",
                                 add_data)


    with open(file_path, 'w') as file:
        for line in file_data:
            file.write(line)


def replace_and_add_lines(file_data,replace_index,start_line_to_replace:str,start_replacement:str, list_of_followup_lines:list[str]):
    file_data[replace_index] = file_data[replace_index].replace(start_line_to_replace,
                                                                start_replacement)
    for i,followup_line in enumerate(list_of_followup_lines):
        file_data.insert(replace_index + i, followup_line + "\n")


if __name__ == "__main__":
    # to run this example install the otlmow-converter in your local python environment
    html_path = Path("slagbomen_visual.html")
    # objects = list(to_objects(Path("DA-2024-35924_export.xlsx")))
    objects = list(to_objects(Path("slagbomen_example.xlsx")))
    PyVisWrapper().show(list_of_objects= objects,
                        html_path=html_path,  launch_html=False)

    modify_html(html_path)
