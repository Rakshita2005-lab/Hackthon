import difflib

def compare(old_code, new_code):
    diff = difflib.unified_diff(
        old_code.splitlines(),
        new_code.splitlines()
    )
    return "\n".join(diff)