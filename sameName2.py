def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

#因为 eggs 在 spam()的顶部被声明为 global,所以当 eggs 被赋值为'spam'时赋值发生在全局作用域的 spam 上。没有创建局部 spam 变量。
