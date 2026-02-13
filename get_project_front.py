
import argparse
import os
from typing import Set, List

# ✅ Расширения файлов
EXTENSIONS: Set[str] = {".py", ".json", ".html", ".css", ".js"}

# ✅ Игнорируемые директории
IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".idea",
    "env",
    "venv",
    "node_modules",
    "site-packages",
    "hooks",
    "logs",
    "refs",
    "pack",
}

DEFAULT_FILES: List[str] = [

]

DEFAULT_DIRS: List[str] = ['.']


EXTENSION_TO_LANG = {
    ".py": "python",
    ".js": "javascript",
    ".json": "json",
    ".html": "html",
    ".css": "css",
}


def read_file_safe(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(path, encoding="latin-1") as f:
                return f.read()
        except Exception as e:
            return f"[Ошибка чтения (кодировка): {e}]"
    except Exception as e:
        return f"[Ошибка чтения файла: {e}]"


def should_take_file(filename: str) -> bool:
    return os.path.splitext(filename)[1].lower() in EXTENSIONS


def get_lang(filename: str) -> str:
    return EXTENSION_TO_LANG.get(os.path.splitext(filename)[1].lower(), "")


def write_one_file_md(path: str, out, base_dir: str | None = None):
    abs_path = os.path.abspath(path)
    if not os.path.isfile(abs_path):
        out.write(f"\n> ❌ **Файл не найден:** `{abs_path}`\n\n")
        return

    rel_path = os.path.relpath(abs_path, base_dir) if base_dir else path
    lang = get_lang(path)

    out.write(f"\n## 📄 `{rel_path}`\n\n")
    out.write(f"```{lang}\n")
    out.write(read_file_safe(abs_path))
    out.write("\n```\n")


def collect_directory_md(root_dir: str, out):
    root_dir = os.path.abspath(root_dir)

    if not os.path.exists(root_dir):
        out.write(f"\n> ❌ **Папка не найдена:** `{root_dir}`\n\n")
        return

    out.write(f"\n# 📂 Директория: `{root_dir}`\n")

    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRECTORIES]
        rel_root = os.path.relpath(current_root, root_dir)

        out.write(f"\n## 📁 `{rel_root}`\n")

        for filename in sorted(files):
            if should_take_file(filename):
                full_path = os.path.join(current_root, filename)
                write_one_file_md(full_path, out, root_dir)


def parse_args():
    p = argparse.ArgumentParser(
        description="Собрать файлы и директории в AI-friendly Markdown."
    )

    p.add_argument("--files", "-f", nargs="*", default=DEFAULT_FILES)
    p.add_argument("--dirs", "-d", nargs="*", default=DEFAULT_DIRS)
    p.add_argument("--out", "-o", default="combined_output.md")

    return p.parse_args()


def main():
    args = parse_args()

    with open(args.out, "w", encoding="utf-8") as out:
        out.write("# 🤖 AI Code Bundle\n\n")
        out.write("## 📌 Параметры\n")
        out.write(f"- **Files:** `{args.files}`\n")
        out.write(f"- **Dirs:** `{args.dirs}`\n")
        out.write(f"- **Extensions:** `{sorted(EXTENSIONS)}`\n")

        out.write("\n---\n\n")

        for fpath in args.files:
            write_one_file_md(fpath, out)

        for dpath in args.dirs:
            collect_directory_md(dpath, out)

    print(f"✅ Готово. Markdown файл: {args.out}")


if __name__ == "__main__":
    main()
