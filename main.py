import hou
import subprocess

def generate_render_commands():
    selected_nodes = hou.selectedNodes()
    if not selected_nodes:
        hou.ui.displayMessage("No nodes selected. Please select one or more render nodes.", 
                            severity=hou.severityType.Warning)
        return
    
    copytext = ''
    for node in selected_nodes:
        try:
            path = node.path()
            range = int(node.parm("trange").eval())

            start_frame = str(int(hou.frame()))
            end_frame = str(int(hou.frame()))

            if(range != 0):
                start_frame = str(int(node.parm("f1").eval()))
                end_frame = str(int(node.parm("f2").eval()))

            t1 = f'mread {hou.getenv("HIPFILE")}'
            t2 = f"render -V -f {start_frame} {end_frame} {str(path)}"
            
            newtext = t1 + '\n\n' + t2 + '\n\n'
            print(newtext)

            copytext += newtext
        except Exception as e:
            print(f"Error processing node {node.path()}: {e}")
            continue

    try:
        process = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
        process.communicate(copytext.encode("utf-8"))
        print(f"//-----------Copied {len(hou.selectedNodes())} nodes to Clipboard!!-----------------//")

    except Exception as e:
        hou.ui.displayMessage(f"Failed to copy to clipboard (Windows): {e}", severity=hou.severityType.Error)

generate_render_commands()
