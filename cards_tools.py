
#记录所有名片信息
card_list = []
def show_menu():
    """
     定义显示菜单函数

    """
    print("*" * 50)
    print("欢迎使用【名片系统】v1.8")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    """

    新增名片
    """
    print("-" * 50)
    print("新增名片")

    #1 提示用户输入名片信息
    name_str = input("请输入姓名")
    phone_str = input("请输入电话")
    qq_str = input("请输入QQ")
    email_str = input("请输入邮箱")

    #2 使用用户输入的信息创建一个名片

    card_dict = {
        "name":name_str,
        "phone":phone_str,
        "qq":qq_str,
        "email":email_str,
    }

    #3 将用户输入的信息追加到字典中
    card_list.append(card_dict)

    #4 提示用户添加信息成功
    print("添加 %s 信息成功" % name_str)

def show_all():
    """

    显示所有名片
    """
    print("-" * 50)
    print("显示所有名片")

    #遍历名片，没有名片 提示用户新建
    if len(card_list) == 0:
        print("没有名片，请新建")
        #return会返回一个函数执行的结果，下方代码不会被执行
        #如果return后面没有任何类容，会返回到调用函数的位置
        return

    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")

    #打印分割线
    print("=" * 50)

    #遍历并打印字典中的信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

def search_card():
    """
    定义一个card_dict变量，遍历card_list里面的信息
    """
    print("-" * 50)
    print("搜索名片")

    #提示用户要搜索的姓名
    find_name = input("请输入你要搜索的姓名")

    #遍历名片，如果未找到 提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("*" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            #TODO 针对后续查找到的记录进行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("没有找到 %s 学生信息" %find_name)

def deal_card(find_dict):
    """
    处理find_dict变量中接受到的信息
    :param find_dict:
    """
    print(find_dict)
    action_str = input("请输入你要进行的操作 "
                        "【1】 修改 【2】 删除 【0】 返回上一级")
    if action_str == "1":

        #修改find_card变量中接收到的信息
        find_dict ["name"] = input_card_info(find_dict ["name"], "姓名：")
        find_dict ["phone"] = input_card_info(find_dict ["phone"], "电话：")
        find_dict ["qq"] = input_card_info(find_dict ["qq"], "QQ：")
        find_dict ["email"] = input_card_info(find_dict ["email"], "邮箱：")
        print("修改名片成功")

    elif action_str == "2":

    #删除find_card变量中接受到的信息
        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info(dict_value,tip_message):

    """
      重写一个不同于系统input的方法，使得用户不修改内容时返回原本的内容
    :param dict_value: 字典中原来的值
    :param tip_message: 提示用户输入的值
    :return:
    """
    #1 提示用户输入
    result_card = input(tip_message)

    #2 判断用户是否输入,如果输入了，直接返回输入的结果
    if len(result_card) > 0:
        return result_card

    #3  如果用户没有输入，返回字典中原有的结果
    else:
        return  dict_value
