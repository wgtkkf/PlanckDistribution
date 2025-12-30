#include<iostream>
#include "include/function.h"

int main()
{
    Message obj_m;
    PLANCK obj_pl;
    ForLoop obj_fl;

    obj_m.start();
    obj_fl.loop_calculation(obj_pl);
    obj_m.end();
    return 0;
}

// See the below!
// Execute with this command: ./run.sh