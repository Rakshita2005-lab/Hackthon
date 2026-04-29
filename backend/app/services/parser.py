# import os

# def parse_codebase(path):
#     structure = []

#     for root, _, files in os.walk(path):
#         for file in files:
#             if file.endswith(".py") or file.endswith(".js"):
#                 file_path = os.path.join(root, file)

#                 with open(file_path, "r", encoding="utf-8") as f:
#                     code = f.read()

#                 structure.append({
#                     "file": file,
#                     "path": file_path,
#                     "code": code
#                 })

#     return structure




import os

def parse_codebase(path):
    structure = []

    if not os.path.exists(path):
        print("❌ Path not found:", path)
        return []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py") or file.endswith(".js"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()

                    structure.append({
                        "file": file,
                        "path": file_path,
                        "code": code
                    })
                except Exception as e:
                    print("Error reading file:", file, e)

    return structure