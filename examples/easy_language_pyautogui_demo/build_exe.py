"""Build a standalone pyautogui_login_cli.exe using PyInstaller."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def ensure_pyinstaller() -> None:
    try:
        import PyInstaller  # type: ignore # noqa: F401
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on environment
        raise SystemExit(
            "PyInstaller 未安装。请先运行 'pip install pyinstaller' 再执行本脚本。"
        ) from exc


def run_pyinstaller(base_dir: Path) -> None:
    cli_path = base_dir / "pyautogui_login_cli.py"
    if not cli_path.exists():
        raise SystemExit(f"未找到脚本：{cli_path}")

    dist_dir = base_dir / "dist"
    build_dir = base_dir / "build"
    spec_path = base_dir / "pyautogui_login_cli.spec"

    # 清理旧的构建产物，避免 PyInstaller 读取过期配置。
    for path in (dist_dir, build_dir, spec_path):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        elif path.is_file():
            path.unlink(missing_ok=True)

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        str(cli_path),
        "--name",
        "pyautogui_login_cli",
        "--onefile",
        "--distpath",
        str(dist_dir),
        "--workpath",
        str(build_dir),
        "--specpath",
        str(base_dir),
    ]

    subprocess.run(command, check=True)


def main() -> int:
    ensure_pyinstaller()
    run_pyinstaller(Path(__file__).resolve().parent)
    print("已在 dist/ 目录生成 pyautogui_login_cli.exe")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
