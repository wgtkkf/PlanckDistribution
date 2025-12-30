import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# =============================================
# This code was generated supported by Gemini =
# =============================================
class Graph:
    # Modified to accept two sets of data: (x1, y1) and (x2, y2)
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def display(self):
        csfont = {'fontname':'DejaVu Sans'} 
        plt.figure() 
        plt.grid(True, which="both", ls="-", alpha=0.5) # Enhanced grid for log scale

        # Plot 1: Analytical (Python)
        plt.plot(self.x1, self.y1, 'blue', label="Analytical, Python") 
        
        # Plot 2: Numerical (C++) - Using a dashed red line to distinguish
        plt.plot(self.x2, self.y2, 'lime', linestyle='--', label="Analytical, C++") 

        ## graph information    
        plt.xlabel(r'Wavelength [$\mu$m]', **csfont)            
        plt.ylabel(r'Blackbody emissive power [W/(m$^{2}$ $\mu$m)]', **csfont)

        # font for legend
        font = font_manager.FontProperties(family='DejaVu Sans',
                                           weight='bold',
                                           style='normal', size=10)
        plt.legend(loc='upper right', prop=font) 

        # Log-Log Style
        plt.xscale('log')
        plt.yscale('log')        

        #
        plt.xlim(1, 100)      # Sets x-axis from 0 to 100
        plt.ylim(1, 100) # Useful for log scales

        # plot options
        plt.xticks([1, 10, 100], **csfont)
        plt.yticks([1, 10, 100], **csfont)

        # graph save & display
        plt.savefig("comparison.png", dpi=300) 
        plt.show()                  
        return 0

# ==========================================
# DATA LOADING LOGIC (EXTERNAL)
# ==========================================

# 1. Load C++ data (Dynamic row length)
cpp_data = np.loadtxt("power_cpp.txt")
x_cpp = cpp_data[:, 0]
y_cpp = cpp_data[:, 1]

# 2. Load Python data (Dynamic row length)
py_data = np.loadtxt("power_python.txt")
x_py = py_data[:, 0]
y_py = py_data[:, 1]

# 3. Create the instance with BOTH datasets
my_graph = Graph(x_py, y_py, x_cpp, y_cpp)

# 4. Generate the single combined plot
my_graph.display()