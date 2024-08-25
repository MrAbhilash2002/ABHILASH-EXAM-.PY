1. What is decorator , write a decorator?
    .a decorator is way to modify or enhance the behaviour of function or class with out modify the original function or class it self.
    . it is function who take another function as an argument.
def decore(calculator):
    def substraction(a,b)
        sub=a-b
        return sub, calculator(a,b)
    return substraction

@decore
def calculator(a,b):
    add=a+b
    return add
print(calculator(120,30))

2.What is lambda expression, write a lambda expression?
A lambda expression is a quick way to create a small, one-time-use function in programming. Think of it as a shortcut for defining a function
without giving it a name. It is a single line statement.
    syntax:
    lambda parameter:logics/statements

3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
repetitive character , without using any inbuilt function.

a= 'Hello everyone'
result = count_repetitive_chars(a)
print(result)

4.WAF , Reverse a string words.
> Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function.
input_string = 'hello world'
output_string = reverse_words(input_string)
print(output_string)

5.WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’
def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    result += str(count) + s[-1]

    return result
input_string = 'aaabbaacd'
output_string = compress_string(input_string)
print(output_string)

6.Sort a list integer element without using inbuilt function?
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
numbers = [14, 20, 62, 32, 18]
bubble_sort(numbers)
print(numbers)
def lists_to_dict(keys, values):
    result_dict = {}
    for key, value in zip(keys, values):
        result_dict[key] = value
    return result_dict

7.Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}
Take a two list a parameter, return dictionary, look like above result.
def lists_to_dict(keys, values):
    result_dict = {}
    for key, value in zip(keys, values):
        result_dict[key] = value
    return result_dict
Li = [1, 2, 3, 4]
Li2 = [10, 20, 30, 40]
result = lists_to_dict(Li, Li2)
print(result)

8.Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
the csv and print in console bar
import csv
data = [
    ["first_name", "email", "phn_no"],
    ["abhilash panigrahi", "abhilash.panigrahi.02@gmail.com", "6370818133"],
    ["swagatika pradhan", "swagatikap65@gmail.com", "63702513766"],
    ["tusar pati","tusar123@gmail.com","9437921907"]
    ["ashutosh sahu","asu54@gmail.com","8895891645"]
]
print(data)

9.What is exception handling , how handel the exception in python , explain with each
block.
Exception handling in Python is a mechanism for managing errors and unusual conditions that occur during program execution using try, except, else, and finally blocks.
.try Block:
The code inside
try (result = a / b) tries to perform the division.

.else Block(Optional):if there are no errors,it prints the result of the division.
. finally= this block always runs.
10.Difference between Moudle and Packages (3 diff)
module.-A single file containing
       -It can define functions, classes, and variables, and can include runnable code.
       -A module is just a single .py file, for example= abhi.py.
pakage.-it containing one or more Python
       -It allows for a hierarchical structure of modules.
       -A package is a directory with a special __init__.py file.
11.Difference between List vs tuple vs set vs dictionary?
list= .The list can be represented by [ ]
      . list allows duplicate elements
      .list can be created using the list() function
tuple=.Tuple can be represented by  ( )
      .Tuple allows duplicate elements
      .Tuple can be created using the tuple() function.
set=.The set can be represented by { }
   .The Set will not allow duplicate elements
   .A set can be created using the set() function
dictionary=.The dictionary can be represented by { }
           .The dictionary doesn’t allow duplicate keys.
           .A dictionary is mutable, its Keys are not duplicated.
12.What is Garbage Collection?
it is the process of automatic deletion of unwanted or unused objects to free the memory is calledgarbage collection.
13.What is list comprehension , write code in list comprehension?
List comprehension is way to creat a list in python.
It allows you to generate a new list by applying an expression to each item in an existing iterable like a list or range and optionally filtering elements.
14.Difference between Shallow copy vs Deep Copy?
shallow copy= its faster.
deep copy=its comparatively slower

15.Explain break, continue, pass with code?
break=it is used to terminate the loop or statement in which it is present.
for loop:
 if condition:
        break
 continue=Continue is also a loop control statement just like the break statement.
 for loop:
     if condition:
         continue
 pass=The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

function/ condition / loop:
   pass



SQL(section)
1.Explain about the DML,DDL,TCL,DQL commands?
DDL=DDL commands manage database structure,
DML=DML commands handle data manipulation.
TCL=TCL commands manage transactional changes.
DQL=used for fetching data from a relational database.

2.What is join, explain about the all joins?
A join in Structured Query Language is a query that combines rows from two or more tables, views, or materialized views.
1.inner join( Returns rows when there is a match in both tables.)
2.left join( Returns all rows from the left table and the matched rows from the right table. If there is no match, the result is NULL for columns from the right table.)
3.right join(Useful when you want all rows from the right table and any matches from the left table.
)
4.full join(Returns rows when there is a match in one of the tables. It combines the results of both LEFT and RIGHT joins.)
5.cross join(Returns the Cartesian product of both tables, i.e., every row from the first table is combined with every row from the second table.)
6.self join(A regular join where a table is joined with itself.)

3.Difference between Joins vs Subquery?
joins=.Joins combine rows from two or more tables based on a related column between them.
      .oins are generally more efficient than subqueries, especially when dealing with large datasets. They often leverage indexes effectively.
      .Joins are best for combining columns from multiple tables into a single result set.
subquery=Subqueries are queries neted inside another query.
         .Subqueries can be less efficient, especially if they are not optimized properly. They may involve more processing, particularly if they are correlated subqueries.



