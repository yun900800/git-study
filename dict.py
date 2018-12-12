dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict)
Name = '17jo'
Zone = 'com'
print('www.%s.%s'%(Name,Zone))

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
#以上实例输出结果：
#dict['Name']:  Zara
#dict['Age']:  7

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print("dict['Alice']: ", dict['Alice'])
print('str(dict):',str(dict))
print('type(dict)',type(dict))

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry

 
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
#以上实例输出结果：
#dict['Age']:  8
#dict['School']:  DPS School

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键是'Name'的条目
dict.clear()     # 清空词典所有条目
#del dict         # 删除词典

#print("dict['Age']: ", dict['Age'])
#print("dict['School']: ", dict['School'])
#但这会引发一个异常，因为用del后字典不再存在：

# radiansdict.clear()    #删除字典内所有元素
# radiansdict.copy()    #返回一个字典的浅复制
# radiansdict.fromkeys()    #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# radiansdict.get(key, default=None)    #返回指定键的值，如果值不在字典中返回default值
# radiansdict.has_key(key)    #如果键在字典dict里返回true，否则返回false
# radiansdict.items()    #以列表返回可遍历的(键, 值) 元组数组
# radiansdict.keys()    #以列表返回一个字典所有的键
# radiansdict.setdefault(key, default=None)    #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
# radiansdict.update(dict2)    #把字典dict2的键/值对更新到dict里
# radiansdict.values()    #以列表返回字典中的所有值

print('''|---欢迎进入通讯录程序---|
|---1、 查询联系人资料---|
|---2、 插入新的联系人---|
|---3、 删除已有联系人---|
|---4、 退出通讯录程序---|''')
addressBook={}#定义通讯录
while 1:
    temp=input('请输入指令代码：')
    if not temp.isdigit():
        print("输入的指令错误，请按照提示输入")
        continue
    item=int(temp)#转换为数字
    if item==4:
        print("|---感谢使用通讯录程序---|")
        break
    name = input("请输入联系人姓名:")
    if item==1:
        if name in addressBook:
            print(name,':',addressBook[name]) 
            continue
        else:
            print("该联系人不存在！")
    if item==2:
        if name in addressBook:
            print("您输入的姓名在通讯录中已存在-->>",name,":",addressBook[name])
            isEdit=input("是否修改联系人资料(Y/N）:")
            if isEdit=='Y':
                userphone = input("请输入联系人电话：")
                addressBook[name]=userphone
                print("联系人修改成功")
                continue
            else:
                continue
        else:
            userphone=input("请输入联系人电话：")
            addressBook[name]=userphone
            print("联系人加入成功！")
            continue

    if item==3:
        if name in addressBook:
            del addressBook[name]
            print("删除成功！")
            continue
        else:
            print("联系人不存在")

# z字典的键不能出现两次，且字典的键不能改变可以是数字，字符串，元组