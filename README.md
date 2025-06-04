# Redshift Render Command Generator for Hbatch

This script is designed to quickly generate hbatch commands for selected ROP nodes. It preparing render jobs for hbatch.

## Features
- **Generates hbatch commands**: Creates the necessary mread and render commands for selected ROP nodes.
- **Supports single frame or frame range**: Automatically detects if a ROP is set to render a single frame or a frame range and adjusts the command accordingly.
- **Copies to clipboard**: Puts the generated commands directly onto your system's clipboard for easy pasting into a terminal or render submission system.

## How to Use
1. Create a shelf tool and paste the code.
1. Select one or more ROP nodes in your scene
1. Click and Run the script from shelf.
1. The generated hbatch commands will be printed to the log and copied to your clipboard.
1. Paste these commands into Hbatch.
1. Enjoy render!

## Example Output
```bat
mread /path/to/your/scene.hip

render -V -f 1 100 /out/mantra_node1

mread /path/to/your/scene.hip

render -V -f 101 200 /out/karma_node2
```