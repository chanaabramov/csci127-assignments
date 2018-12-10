#include <iostream>
using namespace std;
#include <math.h>

double quad(int a, int b, int c){
  int quadr;
  int d;
  b = b*b;
  d = a*c;
  quadr = b-4*d;
  return quadr;
}

double quadsolve( int a, int b , int c){
  float quadr;
  quadr = quad(a,b, c);
  float  s;
  if(quadr >=0){
    s =  sqrt(quadr);
  }
  else{
    s = 0;
  }
  return s;
}

int main(){
  cout<< quad(3,4,5)<< "\n";
  cout<< quadsolve(1,4,2)<< "\n";
			  
  return 0;
  



}
