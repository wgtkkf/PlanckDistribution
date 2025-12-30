#ifndef _FUNCTION_H_
#define _FUNCTION_H_
#include <numbers>

class Message
{
    public:
        void start();
        void end();

};

class PLANCK
{
    public:
        double planck_function(double lambda);
        
        /* constant parameters */
        const double KB = 1.38064852e-23;
        const double PH = 6.62607004e-34; /* Planck constant */
        double PI = std::numbers::pi;

    private:
        const double DH = 0.5*PH/PI;      /* Reduced Planck constant */
        const double C1 = 3.742e8;        /* [W/micron4/m2] */
        const double C2 = 1.439e4;        /* [micron*K] */
        const double TEMPERATURE = 300;   /* [K] */    
        const double CUTOFF = 708;

};

class ForLoop
{
    public:
        double increment(double wl);
        double loop_calculation(PLANCK& callPlanck);

    protected:
        const double WL_MAX = 100;
        const double WL_MIN = 0.01;
        const double POWER_MIN = 1e-8;
        double COUNTER = {0.0};
};

#endif // _FUNCTION_H_