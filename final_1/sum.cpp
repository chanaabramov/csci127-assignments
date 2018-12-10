#include <iostream>
using namespace std;

double sumofsquares( int a, int b){
    int result = 0;
  if(a <b ){
    int i = b - a;
    int c;
    for(c = 0; c<= i; c++){
       result = result +  a*a;
       a = a+1;
      
    }
  }
      return result;

}
int main(){
  cout<< sumofsquares(2,4)<< "\n";
  cout<< sumofsquares(5,6)<< "\n";
  cout<< sumofsquares(10,20)<< "\n";
  cout<< sumofsquares(4,8)<< "\n";
  return 0;

}
