# Homework 1
# Coded by Takuro TOKUNAGA
# Modified:
# August 28, 2018
# December 20, 29, 2025

import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

class Comments:
    def __init__(self, comment1, comment2):
        self.com1 = comment1
        self.com2 = comment2

    def begin(self):
        print ("### " + str(self.com1)  + "   ###")

    def end(self):
        print ("### " + str(self.com2)  + " ###")

    pass

class TimeCounter:
    def __init__(self, time_counter):
        self.time_counter = time_counter

    def time_return(self):
            return self.time_counter

class Graph:
    def __init__(self, argx, argy):
        self.x = argx
        self.y = argy

    def display(self):
        # graph display
        csfont = {'fontname':'DejaVu Sans'} # define font
        plt.figure
        plt.grid() # grid display
        plt.plot(self.x, self.y, 'blue', label="Analytical solution")  # for analytical solution

        ## graph information
        #plt.title('Distribution', **csfont) # graph title
        plt.xlabel('Wavelength [micron]', fontdict=None, labelpad=None, **csfont)
        plt.ylabel('Blackbody emissive power [W/m2 micron]', fontdict=None, labelpad=None, **csfont)

        # font for legend
        font = font_manager.FontProperties(family='DejaVu Sans',
                                           weight='bold',
                                           style='normal', size=10)
        plt.legend(loc='upper right', prop=font) # legend

        # Change scales to log
        plt.xscale('log')
        plt.yscale('log')

        #
        plt.xlim(1, 100)      # Sets x-axis from 0 to 100
        plt.ylim(1, 100) # Useful for log scales

        # plot options
        plt.xticks([1, 10, 100], **csfont)
        plt.yticks([1, 10, 100], **csfont)

        # graph save & display
        plt.savefig("solution.png", dpi=300) # 1. file saving (1. should be before 2.)
        plt.show()                  # 2. file showing (2. should be after 1.)

        return 0

class Planck:
    def __init__(self, arg_lambda):
        self.arg_lambda = arg_lambda

        # constants
        self.KB = 1.38064852*np.power(10.,-23) # Boltzmann constant
        self.PH = 6.62607004*np.power(10.,-34) # Planck constant
        self.DH = self.PH/(2*np.pi)            # Reduced Planck constant
        self.C1 = 3.742*np.power(10.,8)        # [W/micron4/m2]
        self.C2 = 1.439*np.power(10.,4)        # [micron*K]
        self.TEMPERATURE = 300                 # [K]

        # cutoff
        self.CUTOFF = 708

    def planck_function(self):
        blaket = self.C2/(self.arg_lambda*self.TEMPERATURE)
        if blaket < self.CUTOFF:
            term1 = np.power(self.arg_lambda,5)
            term2 = np.exp(self.C2/(self.arg_lambda*self.TEMPERATURE))-1
            self.eplanck = self.C1/(term1*term2)
        else:
            self.eplanck = 0

        return self.eplanck

class ForLoop:
    def __init__(self, start_wl, max_wl, counter, filename='power_python.txt'):
        self.wl = start_wl
        self.wlmax = max_wl
        self.counter = counter
        self.filename = filename

    def increment(self):
        """Determines the step size based on current wavelength."""
        if self.wl < 0.99:
            return 0.01
        elif self.wl < 10:
            return 0.1
        else:
            return 1

    def loop_calculation(self):
        """Executes the loop and writes results to file."""
        with open(self.filename, 'w') as f:
            while self.wl < self.wlmax:
                # Instantiate and call the method from your other class
                planck_instance = Planck(self.wl)
                pwr = planck_instance.planck_function()

                if pwr > 0:
                    f.write(f"{self.wl} {pwr}\n")
                    self.counter = self.counter + 1

                # Update wavelength using the logic helper
                self.wl += self.increment()

        return self.counter

    def read_file(self):
        data = pd.read_csv(self.filename, sep=" ", header=None) # change file name here tab:\t for CHPC
        data.columns = ["x", "y"]

        self.x = np.zeros(self.counter)
        self.y = np.zeros(self.counter)

        # input data into tables
        for i in range(0, self.counter):
            self.x[i] = data.iat[i,0] # x line
            self.y[i] = data.iat[i,1] # fx line, 1:prop, 2:evan, 3:total

        return self.x, self.y

# --- main routine ---
if __name__ == '__main__':
    # instanced: time class and message class
    start = TimeCounter(time.time())
    msg = Comments('Calculation started.', 'Calculation completed.')

    # message method
    msg.begin()

    # Create the scanner and run it
    loop = ForLoop(start_wl=0.01, max_wl=100, counter=0)
    loop.loop_calculation()

    # message method
    msg.end()

    # Plot
    graphInstance = Graph(loop.read_file()[0], loop.read_file()[1])
    graphInstance.display()

    #
    end = TimeCounter(time.time())
    print(f"elapsed_time:{end.time_return() - start.time_return():.2f}[sec]")
