%module(package="pynusmv.nusmv.sexp") sexp

%{
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/sexp/SexpInliner.h" 
%}

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/sexp/SexpInliner.h