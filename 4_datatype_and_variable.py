             #list datatype#
             
list1=[];
print("Empty list: ");
print(list1);

list2=["geeks","for","geeks"];
print("full list : ");
print(list2);

list3=["geeks","for","geeks"];
print("getfirst: ");
print(list3[0]);

print("riverse: ");
list4=[10,20,30];
list4.reverse();
print(list4);

print("insert: ");
list4.insert(1,40);
print(list4);

list5=[40,20,50,30];
list5.sort();
print("sorting : ");
print(list5);

print("indexing: ");
print(list5.index(20));

print("deleting: ");
list5.pop(2);
print(list5);

list5.copy();
print("copy: ");
print(list5);

list6=[60,70];
list5.extend(list6);
print("extend: ");
print(list5);

      #tuple datatype #
      
tuple=();
print("empty: ");
print(tuple);

tuple1=("geeks","for");
print(tuple1);

list4=[1,2,3,4];
print(list4);

tuple1="jai";
tuple2="sri ram";
tuple3=(tuple1,tuple2);
print(tuple3);

tuple=(10,20,30);
print(tuple);


 #set datatype #
set1=set();
print(set1);

set2=set("raj");
print(set2);

set3={10,"ankit",30,"raj"};
print("set3 : ")
print(set3);

print(set3.pop())
print("delete : ")
print(set3);

set3.add("majeet");
print("adding : ")
print(set3);

set4={10,"ankit","raj",50};
print("uniun : ");
print(set3 |set4);

set4={10,"ankit","raj",50};
print("intersection  : ");
print(set3 & set4);

set4={10,"ankit","raj",50};
print("minus : ");
print(set3-set4);


print(set3.union(set3));

set1=set(["geeks","for","geeks"]);
print(set1);

set2=set([1,"geeks",2,"for",3,5]);
print(set2);

    #dictionaries datatype #
    
dict={};
print(dict);

dict={"age":20};
print(dict["age"]);

dict={1:"geeks",2:"For",3:"geeks"};
print(dict);

dict={1:"raj","name":"geeks",3:"malhotra"};
print(dict["name"]);

print(dict.get(3));

dict.clear();
print("clear : ",dict);
  #complex variable#
var=3+6j;
print(var);
print(type(var));  