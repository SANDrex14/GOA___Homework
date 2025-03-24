import os

folder_path = "C:/Users/pc/Desktop/GOA HOMEWORK"

for i in range(140):
    day_folder = os.path.join(folder_path, f"day {i:03}")
    classwork_folder = os.path.join(day_folder, "classwork")
    homework_folder = os.path.join(day_folder, "homework")

    os.makedirs(classwork_folder, exist_ok=True)
    os.makedirs(homework_folder, exist_ok=True)

    # კლასვორკისა და ჰოუმვორქის ფაილების შექმნა
    with open(os.path.join(classwork_folder, "notes.txt"), "w", encoding="utf-8") as f:
        f.write("წაშლილია")

    with open(os.path.join(homework_folder, "task.txt"), "w", encoding="utf-8") as f:
        f.write("წაშლილია")

# =======================================================

# import os
# import shutil

# folder_path = "C:/Users/pc/Desktop/GOA HOMEWORK"

# for i in range(1, 101):
#     classwork_folder = os.path.join(folder_path, f"day {i:03}", "claswork")
    
#     if os.path.exists(classwork_folder):
#         shutil.rmtree(classwork_folder)  # წაშლის classwork ფოლდერს მთლიანად
