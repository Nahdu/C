
//This is a directive and tells the computer to the iostream library
#include <iostream> 

//namespaces are used to group a set of classes, functions, and more under a name.
//all elements in iostream are declared within the std namespace this command is necessary
using namespace std;

//Functions can be defined before main and implemented later.
int sum(int x, int y);

//This is where program execution starts
//Brackets start on the line after the iterational or conditional structure is defined/
//Anyone who beleives differently is wrong.
int main()
{
  //Printing out a message
  cout << "This is going to be a review of pointers" << endl;

  //set x to 5 and x_ptr to 5. Note that * is used bother to define a pointer and to dereference a value.
  int x = 5;
  int *x_ptr = &x;

  cout << "X is " << x << " and the address of x is " << x_ptr << endl;
  cout << "We can change x by dereferencing x and changing its value." << endl;

  //Set the value at the address held in x_ptr to be 65
  *x_ptr = 65;

  cout << "The value of x is now " << x << endl;


  //returning 0 here means the program compelted its execution without any errors.
  return 0;
}


//Sum is implemented here
int sum(int x, int y)
{
  return x + y;
}
