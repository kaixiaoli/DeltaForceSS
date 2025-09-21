.版本 2
.局部变量 运行结果, 整数型
.局部变量 命令行, 文本型

.局部变量 可执行文件路径, 文本型

; 如果使用 Python 版本，请将下方改为 “python”。此示例假设已运行 build_exe.py
; 并在 dist\ 目录生成了 pyautogui_login_cli.exe。
可执行文件路径 ＝ 取运行目录（） ＋ “dist\\pyautogui_login_cli.exe”

; 如果仍需要使用 Python 脚本版本，可将命令行改写为
; 命令行 ＝ “python """ ＋ 取运行目录（） ＋ “pyautogui_login_cli.py""" ＋ ...”
命令行 ＝ 可执行文件路径 ＋
=======

; 根据实际 Python 路径调整命令行，以下示例默认系统 PATH 中已有 python
命令行 ＝ “python """ ＋ 取运行目录（） ＋ “pyautogui_login_cli.py""" ＋

    “ --username=demo_user --password=demo_pass --launch-wait=5 --post-wait=3”

运行结果 ＝ 运行等待 (命令行, , 真)
如果 (运行结果 ＝ 0)
    信息框 (“调用成功，已模拟键入账号和密码。”)
否则
    信息框 (“调用失败，错误码：” ＋ 到文本 (运行结果))
如果结束
