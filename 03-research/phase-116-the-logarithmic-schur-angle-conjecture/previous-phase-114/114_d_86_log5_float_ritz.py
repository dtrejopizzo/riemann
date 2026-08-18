#!/usr/bin/env python3
"""Selection-only Ritz diagnostic at T=log(5)/2; never a certificate."""
import os,runpy
from pathlib import Path
os.environ['D83_LOG5']='1'
runpy.run_path(str(Path(__file__).with_name('114_d_83_log2_complement_float_diagnostic.py')),
               run_name='__main__')
