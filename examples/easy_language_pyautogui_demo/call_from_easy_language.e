.版本 2
.局部变量 运行结果, 整数型
.局部变量 命令行, 文本型

; 根据实际 Python 路径调整命令行，以下示例默认系统 PATH 中已有 python
命令行 ＝ “python """ ＋ 取运行目录（） ＋ “pyautogui_login_cli.py""" ＋
    “ --username=demo_user --password=demo_pass --launch-wait=5 --post-wait=3”

运行结果 ＝ 运行等待 (命令行, , 真)
如果 (运行结果 ＝ 0)
    信息框 (“调用成功，已模拟键入账号和密码。”)
否则
    信息框 (“调用失败，错误码：” ＋ 到文本 (运行结果))
如果结束
