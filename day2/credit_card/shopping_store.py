# -*- coding:utf-8 -*-
__auth__ = 'christian'

from ATM import *
init_goods_dict = {"6plus":6888,"acer":3500,"Nokia":2500,"basketbook":200,"bike":500,"Nike":800,"bag":100,"coffee":35}
goods_dict = {}  #商品信息字典
shopping_car = {}  #购物车字典

def show_goods_list():
    print '%-22s%s'%('商品名称', '价格')
    for k, i in enumerate(init_goods_dict):
        goods_dict[k+1] = [i, init_goods_dict[i]]
        print "%s.%-16s%s"%(k+1, i, init_goods_dict[i])
    print "\033[34;2m%s %s %s\033[0m"%("v.购物车","m.购买记录","q.退出")
    return goods_dict

def buy_goods():
    while True:
        choice = raw_input("请输入商品编号加入购物车：").strip()
        if choice == 'q':
            return choice
        elif choice == 'v': #输入v操作购物车
            if len(shopping_car) == 0:
                print "\033[31;2m请购买商品！\033[0m"
                continue
            modify_shopping_car()
            break
        elif choice == 'm':  #输入m查看购物历史
            with file("shopping_his.txt") as f:
                for i in f.xreadlines():
                    print i
            raw_input("按任意键返回：")
            break
        elif choice.isdigit() and int(choice) in goods_dict.keys():
            choice = int(choice)
            goods_name = goods_dict[choice][0]   #读出goods_dict字典中的商品名
            goods_amount = []   #设置购买的商品数量为列表形式
            # 将商品名称和数量列表加入购物车字典，数量默认为1，重复购买则增加商品数量列表宽度
            shopping_car.setdefault(goods_name, goods_amount).append(1)
            print "已将商品\033[32;2m%s\033[0m加入购物车" % goods_name

def show_shopping_car(title = "购物车", s=''):
    number_GoodsName = {}
    print '*********************%s******************%s'%(title, s)
    print '%-24s%5s%s%s%14s'%('商品名称','单价','*','数量','总价')
    for k, i in enumerate(shopping_car):
        number_GoodsName[k + 1] = i
        print '%d.%-17s%8s*%s%12s'%(k + 1, i, init_goods_dict[i], len(shopping_car[i]), (init_goods_dict[i] * len(shopping_car[i])))
    #print number_GoodsName
    return number_GoodsName

def choice_templet(message, choice_list):
    while True:
        choice = raw_input(message).strip()
        if choice == '0':
            return choice
        elif not choice.isdigit():
            print "\033[31;2m请输入数字！\033[0m"
        elif int(choice) not in choice_list:
            print "\033[31;2m请输入正确编号！\033[0m"
        else:
            choice = int(choice)
            return choice

def add_goods(number_GoodsName):
    while True:
        choice = choice_templet("请输入要\033[31;2m增加\033[0m的商品的编号('0'返回)：", number_GoodsName)
        if choice == '0':
            break
        else:
            goods = number_GoodsName[choice]
            shopping_car[goods].append(1)
            show_shopping_car()

def substrate_goods(number_GoodsName):
    while True:
        choice = choice_templet("请输入要\033[31;2m减去\033[0m的商品的编号('0'返回)：", number_GoodsName)
        if choice == '0':
            break
        else:
            goods = number_GoodsName[choice]
            print shopping_car[goods]
            shopping_car[goods] = shopping_car[goods][:-1] #减去商品数量，切掉商品数量列表中1个单位宽度
            if len(shopping_car[goods]) == 0:
                shopping_car.pop(goods)
                break
            show_shopping_car()

def delete_goods(number_GoodsName):
    while True:
        choice = choice_templet("请输入要\033[31;2m删除\033[0m的商品的编号('0'返回)：",number_GoodsName)
        if choice == "0":
            break
        else:
            goods = number_GoodsName[choice]
            shopping_car.pop(goods)
            break

def clear_shopping_car():  #清空购物车
    while True:
        choice = raw_input("\033[31;2m是否清空购物车?(y/n)\033[0m")
        if choice not in ["y","n"]:
            continue
        elif choice == "n":
            break
        else:
            shopping_car.clear()
            break

def settle_accounts(number_GoodsName):
    show_shopping_car("交易*", "\n")
    print '-----------------------------------------'
    payment = 0
    for i in number_GoodsName:
        payment += init_goods_dict[number_GoodsName[i]] * len(shopping_car[number_GoodsName[i]])  #累加商品价格
    print '\033[33;2m%s:%d\033[0m' % ('合计', payment)
    choice = raw_input("是否结算？(y)")
    if choice == 'y':
        payment_flag = shopping_interface(payment) #调用银行系统
        if payment_flag:
            buy_record(shopping_car) #如果支付成功，则更新购买历史记录

def buy_record(shopping_car):
    number_GoodsName = {}
    buy_date = time.strftime('%Y-%m-%d %H:%M:%S')
    f = file("shopping_his.txt", 'a')
    f.write("%s\n"%buy_date)
    f.write('%-24s%5s%s%s%14s\n'%('商品名称','单价','*','数量','总价'))
    for k, i in  enumerate(shopping_car):
        number_GoodsName[k + 1] = i
        f.write('%d.%-17s%8s*%s%12s\n'%(k + 1,i,init_goods_dict[i],len(shopping_car[i]),(init_goods_dict[i]                                                                                    * len(shopping_car[i]))))
    f.close()

def modify_shopping_car():
    while True:
        number_GoodsName = show_shopping_car()
        print '\033[34;2m%s %s %s %s %s %s\033[0m' % ('1.增加', '2.减少', '3.删除', '4.清空', '9.结算', '0.返回')
        choice = choice_templet("请选择操作编号：",[1,2,3,4,9,0])
        if choice == '0':
            break
        elif str(choice) == "1":
            add_goods(number_GoodsName)
        elif str(choice) == "2":
            substrate_goods(number_GoodsName)
        elif str(choice) == "3":
            delete_goods(number_GoodsName)
        elif str(choice) == "4":
            clear_shopping_car()
        elif str(choice) == "9":
            settle_accounts(number_GoodsName)


if __name__ == '__main__':
    print "---欢迎进入网上购物系统---"
    while True:
        show_goods_list()
        choice = buy_goods()
        if choice == "q":
            break