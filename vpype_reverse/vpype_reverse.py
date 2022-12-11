import vpype as vp
import vpype_cli
import numpy as np

@vpype_cli.cli.command(group="Plugins")
@vpype_cli.layer_processor
def vpype_reverse(lines: vp.LineCollection) -> vp.LineCollection:
    """
    Reverse the order that a layer will be drawn.
    
    vpype read {in.filename} vpype-reverser --layer all write {out.filename}
    """
    new_lines = lines.clone()

    for line in reversed(lines):
        new_lines.append(np.flip(line, axis=0))
    
    return new_lines
