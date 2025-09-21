# 易语言调用 pyautogui 键盘输入示例

该示例展示了如何在易语言程序中调用独立的 Python 脚本或由其打包的
EXE，利用 [pyautogui](https://pyautogui.readthedocs.io/) 模拟输入账号和密码。

## 目录说明

- `pyautogui_login_cli.py`：纯 Python 编写的命令行脚本，可选地启动目标程序，随后在当前焦点窗口中输入账号与密码。
- `build_exe.py`：基于 PyInstaller 的辅助脚本，一键在 `dist/` 目录生成可执行文件。
- `call_from_easy_language.e`：易语言示例代码，演示如何使用 `运行等待` 调用脚本或生成的 EXE，并根据返回值提示执行结果。

## 使用步骤

1. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

2. **可选：打包成独立 EXE**

   若希望易语言直接调用 EXE，可先安装 [PyInstaller](https://pyinstaller.org/)，然后执行

   ```bash
   pip install pyinstaller
   python build_exe.py
   ```

   生成的 `dist/pyautogui_login_cli.exe` 会放在当前目录下的 `dist/` 里。易语言可直接调用该文件，无需依赖 Python 环境。

3. **在目标电脑上放置示例文件**

   将整个 `easy_language_pyautogui_demo` 文件夹拷贝到易语言工程所在目录，确保易语言可以定位到 `pyautogui_login_cli.py` 或生成的 EXE。

4. **修改易语言示例**

   - 在 `call_from_easy_language.e` 中把 `demo_user`、`demo_pass` 改为实际账号与密码；
   - 若直接调用 Python 版本且 Python 未加入系统 PATH，请把 `python` 换成具体的解释器路径（例如 `C:\\Python39\\python.exe`）。
   - 若已生成 EXE，请将命令行中的 `python ...py` 换成 `dist\\pyautogui_login_cli.exe`。

5. **运行**

   - 易语言程序调用脚本或 EXE 时，可选地给 `--target` 参数传入登录程序的路径，例如：

     ```易语言
     命令行 ＝ “dist\\pyautogui_login_cli.exe --target="C:\\Program Files\\WeGame\\wegame.exe" --username=账号 --password=密码”
     ```

   - `pyautogui_login_cli.py`（无论以 Python 还是 EXE 形式运行）会自动等待窗口启动并依次输入账号、密码，再按下回车键提交。

## 常见问题

- **如何调整等待时间？**

  使用 `--launch-wait` 控制启动程序后的等待秒数，`--post-wait` 控制提交后脚本停留的时间。

- **如何调整键入速度？**

  通过 `--typing-interval` 参数设置字符间隔（单位秒），数值越大输入越慢，能提升模拟输入的稳定性。

- **如何修改提交按键？**

  默认提交按键是 `enter`，可通过 `--submit-keys=enter,enter` 等形式指定多个按键序列。

