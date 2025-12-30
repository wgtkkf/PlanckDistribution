#include<iostream>  // need this
#include "include/function.h"
#include <cmath>
#include <fstream>  // Required for file operations
#include <iomanip>  // For formatting

void Message::start()
{
    std::cout << "### Calculation started. ###\n";
}

void Message::end()
{
    std::cout << "### Calculation end.     ###\n";
}

double PLANCK::planck_function(double lambda)
{
    
    double blaket{0.0};
    double term1{0.0};
    double term2{0.0};
    double eplanck{0.0};

    blaket = C2/(lambda*TEMPERATURE);

    if (blaket < CUTOFF)
    {
        term1 = std::pow(lambda, 5);
        term2 = std::exp(C2/(lambda*TEMPERATURE))-1;
        eplanck = C1/(term1*term2);
    }else{
        eplanck = 0;
    }

    return eplanck;
}

double ForLoop::increment(double wl)
{
    double wl_return{0.0};

    if (wl < 0.99){
        wl_return = 0.01;
    }
    else if (wl_return < 10){
        wl_return = 0.1;
    }
    else{
        wl_return = 1.0;
    }    

    return wl_return;
}

double ForLoop::loop_calculation(PLANCK& callPlanck)
{
    double power{0.0};
    double wl_pass{0.0};

    // 1. Create and open the file
    std::ofstream outFile("power_cpp.txt");

    // Check if the file opened successfully (good defense-coding practice)
    if (!outFile.is_open()) {
        std::cerr << "Error: Could not open file for writing!" << std::endl;
        return 0;
    }

    /* initialization of wl */
    wl_pass = WL_MIN;

    while (wl_pass < WL_MAX){
        power = callPlanck.planck_function(wl_pass);        

        if (power > 0)
        {            
            // 3. Write to the file instead of (or in addition to) the console
            // We use a single space as requested
            if (power > POWER_MIN){
                outFile << std::fixed << std::setprecision(6) 
                        << wl_pass << " " << power << "\n";
            }            
            COUNTER = COUNTER + 1;            
        }
        
        wl_pass += this->increment(wl_pass);            
    }

    // 4. Close the file
    outFile.close();

    return COUNTER;
}