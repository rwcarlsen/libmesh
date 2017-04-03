# This Makefile assumes you have libmesh built and installed in $LIBMESH_DIR.

# If the user has no environment variable
# called METHOD, he gets optimized mode.
ifeq (x$(METHOD),x)
  METHOD := oprof
endif

LIBMESH_DIR=$(PWD)/../build

# installed libmesh location of libmesh-config script
libmesh_config := $(LIBMESH_DIR)/bin/libmesh-config

# Use the libmesh-config script to determine the usual make variables.
# Note: passing $METHOD along to the libmesh-config script handles the
# case where METHOD is not set and the user does
# make METHOD=dbg foo
# since in this case, METHOD is never set in the environment and thus
# never passed to libmesh-config correctly.
libmesh_CXX      := $(shell METHOD=$(METHOD) $(libmesh_config) --cxx)
libmesh_INCLUDE  := $(shell METHOD=$(METHOD) $(libmesh_config) --include)
libmesh_CPPFLAGS := $(shell METHOD=$(METHOD) $(libmesh_config) --cppflags)
libmesh_CXXFLAGS := $(shell METHOD=$(METHOD) $(libmesh_config) --cxxflags)
libmesh_LIBS     := $(shell METHOD=$(METHOD) $(libmesh_config) --libs)

# -Rpass=loop-vectorize          identifies loops that were successfully vectorized.
# -Rpass-missed=loop-vectorize   identifies loops that failed vectorization and indicates if vectorization was specified.
# -Rpass-analysis=loop-vectorize identifies the statements that caused vectorization to fail.
# EXTRA_FLAGS := -Rpass=loop-vectorize
# EXTRA_FLAGS := -Rpass-missed=loop-vectorize -Rpass-analysis=loop-vectorize

# File management variables.
srcfiles 	:= $(wildcard *.cc)
opt_executables := $(patsubst %.cc, %-opt, $(srcfiles))

.PHONY: clean

# How to build executables. If you have a source file called foo.cc,
# type 'make foo' to build an executable from it.
%: %.cc
	@echo "Compiling" $<
	@$(libmesh_CXX) $(EXTRA_FLAGS) $(libmesh_INCLUDE) $(libmesh_CPPFLAGS) $(libmesh_CXXFLAGS) $< -o $@-$(METHOD) $(libmesh_LIBS) $(libmesh_LDFLAGS) $(EXTERNAL_FLAGS)

# Generate assembly
%.s: %.cc
	@echo "Generating assembly" $<
	@$(libmesh_CXX) $(libmesh_INCLUDE) $(libmesh_CPPFLAGS) $(libmesh_CXXFLAGS) -S $< -o $@

# File management rules.
clean:
	@rm -f *~ $(opt_executables)
