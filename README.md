# 📂 filexl

A simple Python CLI tool to list all files in a given directory and export them to an Excel file. Supports filtering by file extension, optional path naming, and detection of duplicate file names.

---

## 🚀 Features

- 🔍 Recursively lists all files in a directory (including hidden files)
- 📝 Outputs to Excel with columns:
  - File Name
  - Extension
  - Full Path
  - Path Name (optional)
- 🔁 Appends to existing Excel files
- 🎯 Filter by file extension (`--ext`)
- 🔎 Export only duplicate file names with `--only-duplicates`
- 🔠 Optional case-insensitive extension filtering
- ✅ Simple CLI interface with `--help` support

---

## 🧰 Installation

```bash
pip install filexl
```

## ⚙️ Options

| Option | Description |
|:-------|:------------|
| `--extensions` | Filter files by specific extensions (e.g., `.jpg .png`) |
| `--case-sensitive` | Match extensions case-sensitively |
| `--only-duplicates` | Save only files with duplicate file names |
| `--extract-duplicates-from` | Create a new Excel file containing only duplicates from an existing Excel file |
| `--out` | Output Excel file name for extracted duplicates |
| `--help` | Show help message and usage instructions |


## 📦 Usage

Basic usage
```
filexl --path D:\data

```

With optional path name and Excel file name
```
filexl --path D:\data --name "MyData" --filename myfiles.xlsx

```

Filter by extensions (space or comma-separated)
```
filexl --path D:\images --ext .jpg .png --ignore-case

```

Export only duplicate file names
```
# With default output name (duplicates.xlsx)
filexl --path D:\data --only-duplicates

# Or with a custom output file
filexl --path D:\data --only-duplicates mydups.xlsx

```

Extract Duplicates from an Existing Excel
```
filexl --extract-duplicates-from myfiles.xlsx --out only_duplicates.xlsx
```
This command reads myfiles.xlsx, finds duplicate file names, and writes them to only_duplicates.xlsx.

## 🧪 Example Output

| File Name | Extension | Path                              | Path Name |
|-----------|-----------|-----------------------------------|-----------|
| report    | pdf       | D:\docs\2023\report.pdf           | Documents |
| report    | pdf       | D:\docs\2022\report.pdf           | Documents |
| image     | jpg       | D:\media\photos\image.jpg         | Media     |
| notes     | txt       | D:\projects\docs\notes.txt        | Projects  |

## 🧱 Development
To build a standalone executable:
```
pip install pyinstaller
pyinstaller --onefile filexl/cli.py

```

## 📜 License
MIT License. Use it freely in your own projects!

## 👨‍💻 Author
Developed by Kiarash Gharahgozloo
GitHub: @kiarash-gh