
def replaceDivs(note):
    # somewhat primitive, but should handle the auto-inserted divs
    def fmt(txt):
        return txt.replace("<div>", "<br>").replace("</div>", "").strip()

    changed = False
    for key, val in note.items():
        if "<div>" in val:
            note[key] = fmt(val)
            changed = True
    
    if changed:
        note.flush()
