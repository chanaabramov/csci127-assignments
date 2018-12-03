#include <iostream>
#include <cstdlib> 
#include <iostream>

int main()
{
  int a;
  std::cout<< "Enter a number between 0 and 99:" ;
  std::cin >> a;
  int highlow;
  int guess;
  int high;
  int low;
  high = 99;
  low = 1;
  guess = (rand()%high)+low;
  while(guess != a){
    std::cout << guess  << std::endl;
    std::cout<< "Is the number higher(1), lower(-1), or equal(0) to the one I guessed?:";
    std::cin>> highlow;
    if (highlow == -1){
      high = guess;
      low= 1;
      guess = (rand()%high)+low;
      }
    else if(highlow == 1){
      high = 99-guess;
      low = guess;
      guess = (rand()%(99-high))+low;
      }
   

      


  }


}
