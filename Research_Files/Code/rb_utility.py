#!/usr/bin/python
from numpy import double
import sys
from time import time


def rb_perccount(jj,maxjj):
    """
    -------------------------------------------------------------------
    This code reports the percentage of a for loop done to the screen.
    **** NOTE *** This code currently only works on command line.
	Need to figure out how to make it work in notebook environment.

	Calling Sequence: rb_perccount(I,Imax)
    Input:
            I = Current iteration between 0 and Imax
	     Imax = Maximum number of iterations
	
    Output: 
            Percentage of the for loop done.
            Shows the amount of time elapsed during the job.
	
    WARNING: Do not print anything to the screen between calls of this function!
	
       Written by Rongmon Bordoloi Nov 15 2016
	--------------------------------------------------------------------
    """
    global _start_time
    jj=double(jj)
    maxjj=double(maxjj)
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    if (jj ==0.0):
        pc_done=0.0
        _start_time=time()
        elapsed=double(_start_time-(_start_time))
    else:
        end_time=time()
        elapsed=double(end_time-(_start_time))
        pc_done  =  ((jj+1.)/(maxjj+1.)) * 100.

    elapsed_str = format_interval(elapsed)
    remainTime = format_interval(elapsed/(jj+1.)*(maxjj-jj))
    print ('{:s}'.format('Percentage Done: ')+'{:5.2f}'.format(pc_done)+'{:s}'.format('%    Time Elapsed: ') +elapsed_str+'{:s}'.format('   Time Remaining: ') +remainTime)
    sys.stdout.write(CURSOR_UP_ONE)
    #if (jj != maxjj):
    #    sys.stdout.write(ERASE_LINE)

def format_interval(t):
    """
        Formats a number of seconds as a clock time, [H:]MM:SS
        
        Parameters
        ----------
        t  : int
        Number of seconds.
        Returns
        -------
        out  : str
        [H:]MM:SS
        """
    mins, s = divmod(int(t), 60)
    h, m = divmod(mins, 60)
    if h:
        return '{0:d}:{1:02d}:{2:02d}'.format(h, m, s)
    else:
        return '{0:02d}:{1:02d}'.format(m, s)

   
