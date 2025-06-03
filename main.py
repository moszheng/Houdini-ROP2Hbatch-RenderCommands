#1. Select Node which want to render
#2. Launch Script
#3. Paste Text to Hscript
import subprocess

copytext = ''

for node in hou.selectedNodes():
    path = node.path()
    range = int(node.parm("trange").eval())

    start = str(int(hou.frame()))
    end = str(int(hou.frame()))

    if(range != 0):
        start = str(int(node.parm("f1").eval()))
        end = str(int(node.parm("f2").eval()))

    t1 = "mread " + hou.getenv("HIPFILE")
    t2 = "render -V -f " + start + " " + end + " " + str(path)
    
    newtext = t1 + '\n\n' + t2 + '\n\n'
    print(newtext)

    copytext += newtext

try:
    process = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
    process.communicate(copytext.encode("utf-8"))
    print(f"//-----------Copied {len(hou.selectedNodes())} nodes to Clipboard!!-----------------//")

except Exception as e:
    hou.ui.displayMessage(f"Failed to copy to clipboard (Windows): {e}", severity=hou.severityType.Error)
