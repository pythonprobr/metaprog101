from timeit import timeit
stmt = '''LineItem('Golden raisins', 10, 36.95)'''
setup = '''from bulkfood import LineItem'''
print(timeit(stmt, setup))
