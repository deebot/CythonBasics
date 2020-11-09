# CythonBasics
This repository contains the codes written while exploring cython for the course  Simulation and Modelling.

## <u>Primes_Speedtest</u>
This folder contains  code to calculate no of primes. 
  
To create shared object library. Compile using following command
  
    python setup.py build_ext --inplace

After you have the .so file.To test the speed run the code timing_test.py using command below
  
    python timing_test.py
    
## <u>WrapperC</u>
This folder contains an example to create a  wrapper for C code.

🔨 Build using following command

    make

💡 TO test the wrapper.In terminal run

    ipython3

Then import the module

    import mt_random as mt

Run the command to give initial seed. Here we pass 1000

    mt.init_state(1000)

Generate random number

    mt.rand_int32()
    

clean using
    
    make clean
    

