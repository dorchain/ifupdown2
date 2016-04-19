#!/usr/bin/env python
#
# Copyright 2015 Cumulus Networks, Inc. All rights reserved.
#
# Author: Roopa Prabhu, roopa@cumulusnetworks.com
#
#

class ifupdownFlags():

	def __init__(self):
                self.FORCE = False
                self.DRYRUN = False
                self.NOWAIT = False
                self.PERFMODE = False
                self.CACHE = False

                # Flags
                self.CACHE_FLAGS = 0x0

flags = ifupdownFlags()