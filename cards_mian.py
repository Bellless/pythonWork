
import cards_tools

#while True 为无限循环，由用户决定什么时候终止
while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()
    #系统提示用户输入
    action_str = input("请选择希望执行的操作")
    print("您选择的操作是【 %s 】" % action_str)

    #对输入的数字进行判断操作
    #1，2，3 针对名片进行操作
    if action_str in ["1","2","3"]:

        #新增名片
        if action_str == "1":
            cards_tools.new_card()

        #显示全部
        elif action_str == "2":
            cards_tools.show_all()

        #查询名片
        elif action_str == "3":
            cards_tools.search_card()

        #如果在开发中不希望马上编写分枝的代码
        #可以使用pass关键字代替，pass关键字是一个占位符，能够保证程序的代码结构完整
        #pass关键字不执行任何操作

    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片系统】")

        break

    # 其它数字输入，给于错误重新选择提示
    else:

        print("您输入的不正确，请重新选择")

