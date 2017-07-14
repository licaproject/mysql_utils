#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

// In Out C Python
using namespace std;

#ifndef EXPORT_H
#define EXPORT_H

// To make sure you don't declare the function more than once by including the header
// multiple times.



const char* get_function_module(string function);

const char* get_object_module(string object);

const char* get_value_module(string value);

#endif
