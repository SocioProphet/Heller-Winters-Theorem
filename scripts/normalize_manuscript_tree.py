#!/usr/bin/env python3
import os, argparse, shutil

def ensure_dir(p): os.makedirs(p, exist_ok=True)

def write_if_missing(path, content):
    if os.path.exists(path): return False
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    return True

def normalize(root: str, force: bool=False):
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip .git-like or venv-like trees if present inside manuscript
        base = os.path.basename(dirpath)
        if base in {".git", ".venv", "__pycache__"}:
            continue

        toc_dir = os.path.join(dirpath, "toc")
        ensure_dir(toc_dir)

        legacy_toc = os.path.join(dirpath, "TOC.md")
        new_toc = os.path.join(toc_dir, "TOC.md")

        if os.path.exists(legacy_toc):
            if force or (not os.path.exists(new_toc)):
                shutil.copyfile(legacy_toc, new_toc)
        else:
            # Create a minimal toc/TOC.md if neither exists
            if force or (not os.path.exists(new_toc)):
                with open(new_toc, "w", encoding="utf-8") as f:
                    f.write("# TOC\n\n- (populate)\n")

        # Ensure README exists at each node (do not overwrite)
        readme = os.path.join(dirpath, "README.md")
        write_if_missing(readme, f"# {os.path.basename(dirpath)}\n\n(Scaffold node — populate purpose, scope, artifacts, and changes.)\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="manuscript")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    normalize(args.root, force=args.force)

if __name__ == "__main__":
    main()
