# 📁 Document360 API - Folder Management (Migration Task)

This project demonstrates CRUD operations (Create, Read, Update, Delete) on folders using the [Document360 API](https://docs.document360.io/docs/rest-api). It was developed as part of a Migration Specialist internship task to showcase API usage, automation, and data handling.

---

## 🔧 Technologies Used

- 🐍 Python 3
- `requests` library for making HTTP calls
- `tabulate` library for CLI table formatting

---

## ✅ Features

-  **GET**: Fetch and display all folders (including subfolders) in a tabular format.
-  **POST**: Create a new folder under a specified parent folder.
-  **PUT**: Update the title of an existing folder.
-  **DELETE**: Delete a folder by ID.
-  Status messages and responses are printed after each operation.

---

## 📂 Folder Operations Included

| Operation | HTTP Method | File / Function |
|-----------|-------------|-----------------|
| Get folders | `GET` | `fetch_folders()` |
| Create folder | `POST` | `create_folder()` |
| Update folder title | `PUT` | `update_folder()` |
| Delete folder | `DELETE` | `delete_folder()` |
