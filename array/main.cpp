#include <iostream>
#define b 20
using namespace std;
class arr{
int a[b],i,maxs=b;
int top=0;
public:
void inputend(){
int ele;
cout<<"Enter the element=";
cin>>ele;
a[top]=ele;
top++;}
void inputbeg(){
cout<<"Enter the element=";
int ele;
cin>>ele;
for(i=top;i>=0;i--){
    a[i+1]=a[i];
}
a[0]=ele;top++;
}
void inputpos(){
cout<<"Enter the position=";
int ele,pos;
cin>>pos;
cout<<"Enter the element=";
cin>>ele;
for(i=top;i>=pos-1;i--){
    a[i+1]=a[i];
}top++;
a[pos-1]=ele;

}
void deletebeg(){
cout<<"Element has been deleted=";
cout<<a[0];
for(i=0;i<=top+1;i++){
    a[i]=a[i+1];
}
top--;
}
void deleteend(){
cout<<"Element has been deleted="<<a[top-1];
top--;}
void deletepos(){
cout<<"Enter the position of element to be deleted=";
int pos;
cin>>pos;
for(i=pos-1;i<=top;i++){
    a[i]=a[i+1];
}
cout<<"Element has been deleted."<<endl;
top--;
}
void deletele(){
cout<<"Enter the element to be deleted=";
int ele,count;
cin>>ele;
for(i=0;i<=top;i++){
    if(a[i]==ele){
        count=i;
        cout<<"Element has been deleted."<<endl;
    }

}
for(i=count;i<=top;i++){
    a[i]=a[i+1];
}
top--;
}

void print(){
cout<<"All elements are=";
for(i=0;i<top;i++){
cout<<a[i]<<"  ";}}

};
int main()
{arr a;
q:cout<<endl<<"Choose an option"<<endl;
cout<<"1.Enter the element at beg."<<endl;
cout<<"2.Enter the element at end."<<endl;
cout<<"3.Enter the element at a position."<<endl;
cout<<"4.Delete the element from beginning."<<endl;
cout<<"5.Delete the element from end."<<endl;
cout<<"6.Delete the element of a particular position."<<endl;
cout<<"7.Delete the entered element."<<endl;
cout<<"8.Print all elements."<<endl;
cout<<"9.Exit."<<endl;
int choice;
cin>>choice;
switch(choice){
case 1:
    a.inputbeg();
    goto q;
case 2:
    a.inputend();
    goto q;
case 3:
    a.inputpos();
    goto q;
case 4:
    a.deletebeg();
    goto q;
case 5:
    a.deleteend();
    goto q;
case 6:
    a.deletepos();
    goto q;
case 7:
    a.deletele();
    goto q;
case 8:
    a.print();
    goto q;
case 9:
    break;
default:
    cout<<"You choose the wrong option.";
    goto q;
}
    return 0;
}
