#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math

# Import stuff for working with dates
from datetime import datetime
from matplotlib.dates import date2num, num2date

# Github has a "traffic" page now, but it doesn't seem like you can
# put in an arbitrary date range?  When I looked at it, it showed the
# numbers of unique visitors and views for the last two weeks only...
# So as long as I check back at least once every two weeks I can keep
# a record of it?  Great...

# https://github.com/libMesh/libmesh/graphs/traffic

# Date, Views, Unique Visitors
data = [
    '2014-Feb-17', 274, 25,
    '2014-Feb-18', 145, 30,
    '2014-Feb-19', 129, 27,
    '2014-Feb-20', 202, 24,
    '2014-Feb-21', 240, 22,
    '2014-Feb-22', 62,  17,
    '2014-Feb-23', 28,  12,
    '2014-Feb-24', 217, 19,
    '2014-Feb-25', 90,  25,
    '2014-Feb-26', 189, 36,
    '2014-Feb-27', 112, 26,
    '2014-Feb-28', 81,  20,
    '2014-Mar-01', 113, 17,
    '2014-Mar-02', 53,  16,
    '2014-Mar-03', 41,  21,
    '2014-Mar-04', 144, 35,
    '2014-Mar-05', 51,  20,
    '2014-Mar-06', 157, 25,
    '2014-Mar-07', 50,  22,
    '2014-Mar-08', 50,  11,
    '2014-Mar-09', 42,  13,
    '2014-Mar-10', 61,  16,
    '2014-Mar-11', 27,  16,
    '2014-Mar-12', 111, 20,
    '2014-Mar-13', 66,  20,
    '2014-Mar-14', 223, 25,
    '2014-Mar-15', 46,   9,
    '2014-Mar-16', 26,  17,
    '2014-Mar-17', 80,  29,
    '2014-Mar-18', 59,  30,
    '2014-Mar-19', 85,  31,
    '2014-Mar-20', 122, 18,
    '2014-Mar-21', 61,  21,
    '2014-Mar-22', 33,  18,
    '2014-Mar-23', 64,  14,
    '2014-Mar-24', 95,  24,
    '2014-Mar-25', 75,  28,
    '2014-Mar-26', 49,  18,
    '2014-Mar-27', 57,  24,
    '2014-Mar-28', 33,  16,
    '2014-Mar-29', 41,  16,
    '2014-Mar-30', 19,  11,
    '2014-Mar-31', 52,  12,
    '2014-Apr-01', 120, 21,
    '2014-Apr-02', 68,  23,
    '2014-Apr-03', 98,  28,
    '2014-Apr-04', 77,  21,
    '2014-Apr-05', 80,  15,
    '2014-Apr-06', 55,  15,
    '2014-Apr-07', 71,  31,
    '2014-Apr-08', 84,  26,
    '2014-Apr-09', 33,  18,
    '2014-Apr-10', 32,  16,
    '2014-Apr-11', 51,  20,
    '2014-Apr-12', 25,  15,
    '2014-Apr-13', 49,  20,
    '2014-Apr-14', 120, 23,
    '2014-Apr-15', 191, 27,
    '2014-Apr-16', 219, 24,
    '2014-Apr-17', 216, 30,
    '2014-Apr-18', 63,  19,
    '2014-Apr-19', 36,  11,
    '2014-Apr-20', 25,   7,
    '2014-Apr-21', 115, 24,
    '2014-Apr-22', 128, 31,
    '2014-Apr-23', 87,  25,
    '2014-Apr-24', 108, 23,
    '2014-Apr-25', 111, 20,
    '2014-Apr-26', 89,   9,
    '2014-Apr-27', 29,  11,
    '2014-Apr-28', 177, 28,
    '2014-Apr-29', 170, 27,
    '2014-Apr-30', 183, 28,
    '2014-May-01', 97,  25,
    '2014-May-02', 64,  23,
    '2014-May-03', 43,  12,
    '2014-May-04', 32,  14,
    '2014-May-05', 125, 28,
    '2014-May-06', 68,  24,
    '2014-May-07', 68,  19,
    '2014-May-08', 114, 14,
    '2014-May-09', 47,  20,
    '2014-May-10', 139, 20,
    '2014-May-11', 14,   9,
    '2014-May-12', 90,  27,
    '2014-May-13', 92,  22,
    '2014-May-14', 197, 32,
    '2014-May-15', 140, 26,
    '2014-May-16', 59,  20,
    '2014-May-17', 21,  9 ,
    '2014-May-18', 54,  16,
    '2014-May-19', 117, 28,
    '2014-May-20', 47,  18,
    '2014-May-21', 55,  19,
    '2014-May-22', 77,  26,
    '2014-May-23', 28,  12,
    '2014-May-24', 38,  13,
    '2014-May-25', 36,  14,
    '2014-May-26', 44,  13,
    '2014-May-27', 166, 24,
    '2014-May-28', 139, 20,
    '2014-May-29', 67,  25,
    '2014-May-30', 73,  11,
    '2014-May-31', 60,  9 ,
    '2014-Jun-01', 22,  11,
    '2014-Jun-02', 87,  18,
    '2014-Jun-03', 103, 31,
    '2014-Jun-04', 105, 27,
    '2014-Jun-05', 74,  22,
    '2014-Jun-06', 55,  16,
    '2014-Jun-07', 53,  15,
    '2014-Jun-08', 19,  5 ,
    '2014-Jun-09', 91,  14,
    '2014-Jun-10', 136, 19,
    '2014-Jun-11', 104, 27,
    '2014-Jun-12', 195, 22,
    '2014-Jun-13', 51,  18,
    '2014-Jun-14', 4,   4 ,
    '2014-Jun-15', 19,  8 ,
    '2014-Jun-16', 86,  19,
    '2014-Jun-17', 60,  20,
    '2014-Jun-18', 115, 25,
    '2014-Jun-19', 73,  20,
    '2014-Jun-20', 24,  12,
    '2014-Jun-21', 12,  4 ,
    '2014-Jun-22', 30,  10,
    '2014-Jun-23', 106, 23,
    '2014-Jun-24', 51,  16,
    '2014-Jun-25', 115, 25,
    '2014-Jun-26', 77,  24,
    '2014-Jun-27', 91,  24,
    '2014-Jun-28', 30,  9 ,
    '2014-Jun-29', 9,   7 ,
    '2014-Jun-30', 80,  25,
    '2014-Jul-01', 118, 17,
    '2014-Jul-02', 124, 18,
    '2014-Jul-03', 103, 22,
    '2014-Jul-04', 33,  11,
    '2014-Jul-05', 37,  13,
    '2014-Jul-06', 25,  11,
    '2014-Jul-07', 147, 27,
    '2014-Jul-08', 123, 14,
    '2014-Jul-09', 75,  24,
    '2014-Jul-10', 68,  16,
    '2014-Jul-11', 103, 22,
    '2014-Jul-12', 21,  6 ,
    '2014-Jul-13', 16,  3 ,
    '2014-Jul-14', 103, 24,
    '2014-Jul-15', 86,  16,
    '2014-Jul-16', 90,  20,
    '2014-Jul-17', 92,  18,
    '2014-Jul-18', 70,  17,
    '2014-Jul-19', 27,  8 ,
    '2014-Jul-20',  7,  4 ,
    '2014-Jul-21', 66,  19,
    '2014-Jul-22', 63,  16,
    '2014-Jul-23', 56,  14,
    '2014-Jul-24', 110, 19,
    '2014-Jul-25', 27,  14,
    '2014-Jul-26', 9,   8 ,
    '2014-Jul-27', 27,  9 ,
    '2014-Jul-28', 73,  23,
    '2014-Jul-29', 136, 22,
    '2014-Jul-30', 25,  14,
    '2014-Jul-31', 113, 29,
    '2014-Aug-01', 68,  20,
    '2014-Aug-02', 34,  5 ,
    '2014-Aug-03', 17,  5 ,
    '2014-Aug-04', 28,  17,
    '2014-Aug-05', 66,  15,
    '2014-Aug-06', 62,  24,
    '2014-Aug-07', 123, 17,
    '2014-Aug-08', 92,  19,
    '2014-Aug-09', 29,  9 ,
    '2014-Aug-10', 9,   5 ,
    '2014-Aug-11', 75,  17,
    '2014-Aug-12', 108, 19,
    '2014-Aug-13', 173, 25,
    '2014-Aug-14', 109, 28,
    '2014-Aug-15', 46,  17,
    '2014-Aug-16', 33,  11,
    '2014-Aug-17', 109, 15,
    '2014-Aug-18', 154, 20,
    '2014-Aug-19', 143, 23,
    '2014-Aug-20', 54,  10,
    '2014-Aug-21', 31,  19,
    '2014-Aug-22', 86,  16,
    '2014-Aug-23', 30,  7 ,
    '2014-Aug-24', 19,  8 ,
    '2014-Aug-25', 135, 18,
    '2014-Aug-26', 140, 20,
    '2014-Aug-27', 81,  23,
    '2014-Aug-28', 87,  21,
    '2014-Aug-29', 40,  11,
    '2014-Aug-30', 102, 11,
    '2014-Aug-31', 26,  8 ,
    '2014-Sep-01', 37,  11,
    '2014-Sep-02', 64,  11,
    '2014-Sep-03', 52,  19,
    '2014-Sep-04', 172, 37,
    '2014-Sep-05', 42,  13,
    '2014-Sep-06', 29,  15,
    '2014-Sep-07', 24,  8 ,
    '2014-Sep-08', 56,  13,
    '2014-Sep-09', 87,  25,
    '2014-Sep-10', 80,  14,
    '2014-Sep-11', 82,  22,
    '2014-Sep-12', 53,  18,
    '2014-Sep-13', 22,  9 ,
    '2014-Sep-14', 31,  10,
    '2014-Sep-15', 99,  28,
    '2014-Sep-16', 174, 32,
    '2014-Sep-17', 137, 24,
    '2014-Sep-18', 96,  30,
    '2014-Sep-19', 84,  25,
    '2014-Sep-20', 45,  15,
    '2014-Sep-21', 34,  11,
    '2014-Sep-22', 57,  21,
    '2014-Sep-23', 130, 19,
    '2014-Sep-24', 169, 30,
    '2014-Sep-25', 195, 29,
    '2014-Sep-26', 82,  17,
    '2014-Sep-27', 32,  10,
    '2014-Sep-28', 19,  8 ,
    '2014-Sep-29', 71,  15,
    '2014-Sep-30', 45,  18,
    '2014-Oct-01', 136, 19,
    '2014-Oct-02', 132, 19,
    '2014-Oct-03', 127, 20,
    '2014-Oct-04', 61,  15,
    '2014-Oct-05', 6,   4 ,
    '2014-Oct-06', 72,  16,
    '2014-Oct-07', 98,  26,
    '2014-Oct-08', 33,  17,
    '2014-Oct-09', 65,  10,
    '2014-Oct-10', 39,  17,
    '2014-Oct-11', 14,  8 ,
    '2014-Oct-12', 44,  9 ,
    '2014-Oct-13', 36,  14,
    '2014-Oct-14', 160, 27,
    '2014-Oct-15', 311, 35,
    '2014-Oct-16', 333, 35,
    '2014-Oct-17', 147, 32,
    '2014-Oct-18', 57,  13,
    '2014-Oct-19', 114, 19,
    '2014-Oct-20', 135, 31,
    '2014-Oct-21', 176, 42,
    '2014-Oct-22', 180, 38,
    '2014-Oct-23', 251, 38,
    '2014-Oct-24', 193, 27,
    '2014-Oct-25', 75,  18,
    '2014-Oct-26', 30,  15,
    '2014-Oct-27', 76,  28,
    '2014-Oct-28', 162, 34,
    '2014-Oct-29', 408, 46,
    '2014-Oct-30', 197, 31,
    '2014-Oct-31', 99,  33,
    '2014-Nov-01', 31,  10,
    '2014-Nov-02', 130, 22,
    '2014-Nov-03', 147, 31,
    '2014-Nov-04', 131, 42,
    '2014-Nov-05', 135, 39,
    '2014-Nov-06', 99,  29,
    '2014-Nov-07', 68,  24,
    '2014-Nov-08', 53,  19,
    '2014-Nov-09', 25,  11,
    '2014-Nov-10', 126, 23,
    '2014-Nov-11', 165, 33,
    '2014-Nov-12', 101, 27,
    '2014-Nov-13', 40,  18,
    '2014-Nov-14', 57,  20,
    '2014-Nov-15', 94,  13,
    '2014-Nov-16', 9,   6 ,
    '2014-Nov-17', 66,  29,
    '2014-Nov-18', 112, 30,
    '2014-Nov-19', 89,  22,
    '2014-Nov-20', 54,  15,
    '2014-Nov-21', 66,  24,
    '2014-Nov-22', 38,  13,
    '2014-Nov-23', 12,  8 ,
    '2014-Nov-24', 102, 25,
    '2014-Nov-25', 113, 20,
    '2014-Nov-26', 63,  22,
    '2014-Nov-27', 39,  14,
    '2014-Nov-28', 67,  21,
    '2014-Nov-29', 29,  11,
    '2014-Nov-30', 116, 11,
    '2014-Dec-01', 95,  28,
    '2014-Dec-02', 101, 31,
    '2014-Dec-03', 170, 24,
    '2014-Dec-04', 124, 34,
    '2014-Dec-05', 88,  13,
    '2014-Dec-06', 8,   7,
    '2014-Dec-07', 14,  8,
    '2014-Dec-08', 28,  15,
    '2014-Dec-09', 69,  20,
    '2014-Dec-10', 176, 21,
    '2014-Dec-11', 158, 34,
    '2014-Dec-12', 53,  13,
    '2014-Dec-13', 8,   5,
    '2014-Dec-14', 16,  7,
    '2014-Dec-15', 187, 24,
    '2014-Dec-16', 93,  20,
    '2014-Dec-17', 81,  24,
    '2014-Dec-18', 76,  18,
    '2014-Dec-19', 52,  18,
    '2014-Dec-20', 32,  13,
    '2014-Dec-21', 22,  6,
    '2014-Dec-22', 38,  18,
    '2014-Dec-23', 24,  13,
    '2014-Dec-24', 15,  11,
    '2014-Dec-25', 34,  9,
    '2014-Dec-26', 26,  8,
    '2014-Dec-27', 16,  8,
    '2014-Dec-28', 9,   5,
    '2014-Dec-29', 45,  8,
    '2014-Dec-30', 79,  7,
    '2014-Dec-31', 16,  10,
    '2015-Jan-01', 2,   2,
    '2015-Jan-02', 22,  13,
    '2015-Jan-03', 11,  7,
    '2015-Jan-04', 90,  4,
    '2015-Jan-05', 40,  21,
    '2015-Jan-06', 77,  18,
    '2015-Jan-07', 101, 22,
    '2015-Jan-08', 160, 30,
    '2015-Jan-09', 94,  22,
    '2015-Jan-10', 23,  9,
    '2015-Jan-11', 26,  10,
    '2015-Jan-12', 84,  26,
    '2015-Jan-13', 140, 31,
    '2015-Jan-14', 207, 27,
    '2015-Jan-15', 113, 23,
    '2015-Jan-16', 134, 27,
    '2015-Jan-17', 45,  9,
    '2015-Jan-18', 34,  11,
    '2015-Jan-19', 62,  20,
    '2015-Jan-20', 63,  16,
    '2015-Jan-21', 74,  24,
    '2015-Jan-22', 69,  26,
    '2015-Jan-23', 77,  17,
    '2015-Jan-24', 63,  14,
    '2015-Jan-25', 27,  9,
    '2015-Jan-26', 57,  22,
    '2015-Jan-27', 118, 19,
    '2015-Jan-28', 91,  21,
    '2015-Jan-29', 66,  21,
    '2015-Jan-30', 123, 28,
    '2015-Jan-31', 27,  11,
    '2015-Feb-01', 52,  9,
    '2015-Feb-02', 89,  22,
    '2015-Feb-03', 47,  14,
    '2015-Feb-04', 82,  22,
    '2015-Feb-05', 127, 27,
    '2015-Feb-06', 74,  24,
    '2015-Feb-07', 23,  8,
    '2015-Feb-08', 20,  11,
    '2015-Feb-09', 61,  22,
    '2015-Feb-10', 90,  30,
    '2015-Feb-11', 86,  20,
    '2015-Feb-12', 127, 23,
    '2015-Feb-13', 259, 27,
    '2015-Feb-14', 17,  9,
    '2015-Feb-15', 7,   3,
    '2015-Feb-16', 120, 27,
    '2015-Feb-17', 130, 28,
    '2015-Feb-18', 49,  16,
    '2015-Feb-19', 219, 21,
    '2015-Feb-20', 126, 31,
    '2015-Feb-21', 69,  9,
    '2015-Feb-22', 51,  10,
    '2015-Feb-23', 100, 28,
    '2015-Feb-24', 206, 19,
    '2015-Feb-25', 95,  22,
    '2015-Feb-26', 115, 35,
    '2015-Feb-27', 80,  20,
    '2015-Feb-28', 100, 16,
    '2015-Mar-01', 53,  8,
    '2015-Mar-02', 193, 22,
    '2015-Mar-03', 101, 19,
    '2015-Mar-04', 135, 33,
    '2015-Mar-05', 201, 31,
    '2015-Mar-06', 65,  20,
    '2015-Mar-07', 61,  12,
    '2015-Mar-08', 35,  9,
    '2015-Mar-09', 86,  23,
    '2015-Mar-10', 38,  21,
    '2015-Mar-11', 118, 28,
    '2015-Mar-12', 107, 19,
    '2015-Mar-13', 124, 28,
    '2015-Mar-14', 17,  12,
    '2015-Mar-15', 42,  12,
    '2015-Mar-16', 111, 24,
    '2015-Mar-17', 180, 24,
    '2015-Mar-18', 83,  27,
    '2015-Mar-19', 96,  19,
    '2015-Mar-20', 106, 21,
    '2015-Mar-21', 31,  14,
    '2015-Mar-22', 58,  11,
    '2015-Mar-23', 56,  19,
    '2015-Mar-24', 107, 28,
    '2015-Mar-25', 119, 25,
    '2015-Mar-26', 99,  22,
    '2015-Mar-27', 259, 20,
    '2015-Mar-28', 76,  12,
    '2015-Mar-29', 22,  9,
    '2015-Mar-30', 156, 31,
    '2015-Mar-31', 79,  22,
    '2015-Apr-01', 128, 31,
    '2015-Apr-02', 71,  22,
    '2015-Apr-03', 47,  8,
    '2015-Apr-04', 62,  12,
    '2015-Apr-05', 75,  12,
    '2015-Apr-06', 62,  22,
    '2015-Apr-07', 90,  23,
    '2015-Apr-08', 67,  25,
    '2015-Apr-09', 68,  24,
    '2015-Apr-10', 63,  18,
    '2015-Apr-11', 53,  9,
    '2015-Apr-12', 19,  9,
    '2015-Apr-13', 35,  11,
    '2015-Apr-14', 106, 27,
    '2015-Apr-15', 200, 29,
    '2015-Apr-16', 218, 29,
    '2015-Apr-17', 125, 25,
    '2015-Apr-18', 61,  8,
    '2015-Apr-19', 26,  8,
    '2015-Apr-20', 162, 23,
    '2015-Apr-21', 110, 22,
    '2015-Apr-22', 187, 31,
    '2015-Apr-23', 137, 24,
    '2015-Apr-24', 200, 20,
    '2015-Apr-25', 87,  12,
    '2015-Apr-26', 49,  13,
    '2015-Apr-27',   67,   19,
    '2015-Apr-28',  135,   24,
    '2015-Apr-29',  127,   26,
    '2015-Apr-30',  140,   28,
    '2015-May-01',   40,   16,
    '2015-May-02',   44,    9,
    '2015-May-03',   31,   12,
    '2015-May-04',  155,   18,
    '2015-May-05',  168,   22,
    '2015-May-06',  121,   18,
    '2015-May-07',   77,   14,
    '2015-May-08',  128,   21,
    '2015-May-09',   29,   13,
    '2015-May-10',   35,    5,
    '2015-May-11',  156,   27,
    '2015-May-12',  138,   19,
    '2015-May-13',  118,   25,
    '2015-May-14',  144,   29,
    '2015-May-15',  181,   16,
    '2015-May-16',   58,    6,
    '2015-May-17',   72,    5,
    '2015-May-18',   31,    9,
    ]

# Github now tracks the total number of clones and unique cloners
clone_data = [
    '2014-Aug-03', 0,   0,
    '2014-Aug-04', 10,  6,
    '2014-Aug-05', 7,   7,
    '2014-Aug-06', 21, 14,
    '2014-Aug-07', 11,  9,
    '2014-Aug-08', 9,   8,
    '2014-Aug-09', 2,   2,
    '2014-Aug-10', 2,   2,
    '2014-Aug-11', 8,   6,
    '2014-Aug-12', 9,   8,
    '2014-Aug-13', 19, 11,
    '2014-Aug-14', 9,   7,
    '2014-Aug-15', 5,   5,
    '2014-Aug-16', 5,   2,
    '2014-Aug-17', 5,   5,
    '2014-Aug-18', 10,  8,
    '2014-Aug-19', 9,   8,
    '2014-Aug-20', 3,   3,
    '2014-Aug-21', 12,  8,
    '2014-Aug-22', 3,   3,
    '2014-Aug-23', 2,   2,
    '2014-Aug-24', 3,   3,
    '2014-Aug-25', 8,   5,
    '2014-Aug-26', 7,   7,
    '2014-Aug-27', 9,   8,
    '2014-Aug-28', 19, 12,
    '2014-Aug-29', 18, 14,
    '2014-Aug-30', 1,   1,
    '2014-Aug-31', 1,   1,
    '2014-Sep-01', 6,   5,
    '2014-Sep-02', 9,   8,
    '2014-Sep-03', 5,   4,
    '2014-Sep-04', 9,   8,
    '2014-Sep-05', 3,   3,
    '2014-Sep-06', 1,   1,
    '2014-Sep-07', 2,   2,
    '2014-Sep-08', 9,   9,
    '2014-Sep-09', 16, 10,
    '2014-Sep-10', 9,   8,
    '2014-Sep-11', 9,   7,
    '2014-Sep-12', 5,   3,
    '2014-Sep-13', 5,   5,
    '2014-Sep-14', 9,   7,
    '2014-Sep-15', 8,   7,
    '2014-Sep-16', 12,  8,
    '2014-Sep-17', 19, 11,
    '2014-Sep-18', 15, 11,
    '2014-Sep-19', 16,  8,
    '2014-Sep-20', 0,   0,
    '2014-Sep-21', 4,   4,
    '2014-Sep-22', 4,   3,
    '2014-Sep-23', 19, 14,
    '2014-Sep-24', 13, 11,
    '2014-Sep-25', 26, 15,
    '2014-Sep-26', 10,  9,
    '2014-Sep-27', 1,   1,
    '2014-Sep-28', 1,   1,
    '2014-Sep-29', 10,  9,
    '2014-Sep-30', 11,  5,
    '2014-Oct-01', 15, 13,
    '2014-Oct-02', 14, 13,
    '2014-Oct-03', 15, 13,
    '2014-Oct-04', 7,   7,
    '2014-Oct-05', 2,   2,
    '2014-Oct-06', 10,  8,
    '2014-Oct-07', 38, 24,
    '2014-Oct-08', 19, 16,
    '2014-Oct-09', 27, 14,
    '2014-Oct-10', 30, 18,
    '2014-Oct-11', 8,   7,
    '2014-Oct-12', 10,  8,
    '2014-Oct-13', 20, 17,
    '2014-Oct-14', 22, 14,
    '2014-Oct-15', 22, 14,
    '2014-Oct-16', 25, 17,
    '2014-Oct-17', 15,  9,
    '2014-Oct-18', 7,   5,
    '2014-Oct-19', 7,   5,
    '2014-Oct-20', 19, 14,
    '2014-Oct-21', 26, 18,
    '2014-Oct-22', 31, 16,
    '2014-Oct-23', 16, 13,
    '2014-Oct-24', 11,  9,
    '2014-Oct-25', 4,   3,
    '2014-Oct-26', 8,   8,
    '2014-Oct-27', 11,  8,
    '2014-Oct-28', 9,   8,
    '2014-Oct-29', 19, 16,
    '2014-Oct-30', 10,  8,
    '2014-Oct-31', 8,   7,
    '2014-Nov-01', 8,   6,
    '2014-Nov-02', 5,   5,
    '2014-Nov-03', 15, 14,
    '2014-Nov-04', 16, 13,
    '2014-Nov-05', 7,   7,
    '2014-Nov-06', 6,   6,
    '2014-Nov-07', 8,   8,
    '2014-Nov-08', 9,   7,
    '2014-Nov-09', 4,   4,
    '2014-Nov-10', 12, 10,
    '2014-Nov-11', 15, 13,
    '2014-Nov-12', 18, 12,
    '2014-Nov-13', 13,  8,
    '2014-Nov-14', 16, 13,
    '2014-Nov-15', 6,   4,
    '2014-Nov-16', 5,   4,
    '2014-Nov-17', 17, 12,
    '2014-Nov-18', 11,  9,
    '2014-Nov-19', 19, 12,
    '2014-Nov-20', 25, 16,
    '2014-Nov-21', 14, 10,
    '2014-Nov-22', 7,   5,
    '2014-Nov-23', 4,   4,
    '2014-Nov-24', 11,  8,
    '2014-Nov-25', 8,   6,
    '2014-Nov-26', 19, 13,
    '2014-Nov-27', 3,   3,
    '2014-Nov-28', 12,  7,
    '2014-Nov-29', 5,   4,
    '2014-Nov-30', 7,   7,
    '2014-Dec-01', 15, 11,
    '2014-Dec-02', 11,  8,
    '2014-Dec-03', 7,   6,
    '2014-Dec-04', 7,   6,
    '2014-Dec-05', 13, 11,
    '2014-Dec-06', 8,   7,
    '2014-Dec-07', 2,   2,
    '2014-Dec-08', 15, 11,
    '2014-Dec-09', 9,   4,
    '2014-Dec-10', 4,   3,
    '2014-Dec-11', 8,   7,
    '2014-Dec-12', 15,  9,
    '2014-Dec-13', 7,   4,
    '2014-Dec-14', 4,   3,
    '2014-Dec-15', 27, 13,
    '2014-Dec-16', 15, 11,
    '2014-Dec-17', 27, 17,
    '2014-Dec-18', 18, 14,
    '2014-Dec-19', 19, 16,
    '2014-Dec-20', 6,  5,
    '2014-Dec-21', 3,  3,
    '2014-Dec-22', 4,  4,
    '2014-Dec-23', 7,  7,
    '2014-Dec-24', 5,  4,
    '2014-Dec-25', 1,  1,
    '2014-Dec-26', 4,  3,
    '2014-Dec-27', 6,  4,
    '2014-Dec-28', 1,  1,
    '2014-Dec-29', 3,  3,
    '2014-Dec-30', 2,  2,
    '2014-Dec-31', 1,  1,
    '2015-Jan-01', 5,  2,
    '2015-Jan-02', 5,  5,
    '2015-Jan-03', 4,  4,
    '2015-Jan-04', 2,  2,
    '2015-Jan-05', 10, 10,
    '2015-Jan-06', 20, 17,
    '2015-Jan-07', 13, 11,
    '2015-Jan-08', 14, 8,
    '2015-Jan-09', 18, 11,
    '2015-Jan-10', 3,  2,
    '2015-Jan-11', 2,  1,
    '2015-Jan-12', 28, 14,
    '2015-Jan-13', 22, 15,
    '2015-Jan-14', 19, 15,
    '2015-Jan-15', 13, 11,
    '2015-Jan-16', 13, 11,
    '2015-Jan-17', 4,  3,
    '2015-Jan-18', 8,  8,
    '2015-Jan-19', 16, 7,
    '2015-Jan-20', 34, 21,
    '2015-Jan-21', 28, 20,
    '2015-Jan-22', 24, 14,
    '2015-Jan-23', 11, 9,
    '2015-Jan-24', 5,  4,
    '2015-Jan-25', 5,  5,
    '2015-Jan-26', 27, 12,
    '2015-Jan-27', 25, 19,
    '2015-Jan-28', 45, 20,
    '2015-Jan-29', 39, 26,
    '2015-Jan-30', 26, 19,
    '2015-Jan-31', 8,  6,
    '2015-Feb-01', 10, 6,
    '2015-Feb-02', 11, 8,
    '2015-Feb-03', 22, 17,
    '2015-Feb-04', 16, 13,
    '2015-Feb-05', 25, 18,
    '2015-Feb-06', 14, 10,
    '2015-Feb-07', 3,  3,
    '2015-Feb-08', 5,  5,
    '2015-Feb-09', 16, 15,
    '2015-Feb-10', 16, 12,
    '2015-Feb-11', 18, 15,
    '2015-Feb-12', 24, 18,
    '2015-Feb-13', 16, 11,
    '2015-Feb-14', 16, 8,
    '2015-Feb-15', 6,  5,
    '2015-Feb-16', 17, 11,
    '2015-Feb-17', 13, 9,
    '2015-Feb-18', 22, 17,
    '2015-Feb-19', 31, 19,
    '2015-Feb-20', 13, 10,
    '2015-Feb-21', 14, 7,
    '2015-Feb-22', 7,  5,
    '2015-Feb-23', 19, 10,
    '2015-Feb-24', 21, 11,
    '2015-Feb-25', 12, 7,
    '2015-Feb-26', 13, 9,
    '2015-Feb-27', 10, 10,
    '2015-Feb-28', 10, 6,
    '2015-Mar-01', 4,  4,
    '2015-Mar-02', 13, 13,
    '2015-Mar-03', 14, 12,
    '2015-Mar-04', 23, 18,
    '2015-Mar-05', 30, 17,
    '2015-Mar-06', 14, 12,
    '2015-Mar-07', 4,  4,
    '2015-Mar-08', 5,  5,
    '2015-Mar-09', 9,  7,
    '2015-Mar-10', 7,  6,
    '2015-Mar-11', 16, 12,
    '2015-Mar-12', 15, 13,
    '2015-Mar-13', 15, 12,
    '2015-Mar-14', 10, 9,
    '2015-Mar-15', 3,  2,
    '2015-Mar-16', 11, 9,
    '2015-Mar-17', 16, 13,
    '2015-Mar-18', 8,  7,
    '2015-Mar-19', 13, 11,
    '2015-Mar-20', 9,  8,
    '2015-Mar-21', 3,  3,
    '2015-Mar-22', 2,  1,
    '2015-Mar-23', 13, 12,
    '2015-Mar-24', 24, 19,
    '2015-Mar-25', 18, 14,
    '2015-Mar-26', 13, 9,
    '2015-Mar-27', 8,  8,
    '2015-Mar-28', 7,  5,
    '2015-Mar-29', 2,  2,
    '2015-Mar-30', 19, 15,
    '2015-Mar-31', 21, 14,
    '2015-Apr-01', 15, 12,
    '2015-Apr-02', 9,  8,
    '2015-Apr-03', 7,  6,
    '2015-Apr-04', 7,  6,
    '2015-Apr-05', 2,  2,
    '2015-Apr-06', 19, 9,
    '2015-Apr-07', 21, 13,
    '2015-Apr-08', 10, 10,
    '2015-Apr-09', 12, 8,
    '2015-Apr-10', 4,  4,
    '2015-Apr-11', 2,  2,
    '2015-Apr-12', 4,  4,
    '2015-Apr-13', 8,  6,
    '2015-Apr-14', 10, 10,
    '2015-Apr-15', 11, 10,
    '2015-Apr-16', 10, 6,
    '2015-Apr-17', 9,  7,
    '2015-Apr-18', 0,  0,
    '2015-Apr-19', 7,  5,
    '2015-Apr-20', 2,  2,
    '2015-Apr-21', 13, 8,
    '2015-Apr-22', 18, 11,
    '2015-Apr-23', 15, 10,
    '2015-Apr-24', 13, 8,
    '2015-Apr-25', 4,  4,
    '2015-Apr-26', 4,  4,
    '2015-Apr-27',    9,    7,
    '2015-Apr-28',    6,    6,
    '2015-Apr-29',   12,    8,
    '2015-Apr-30',   15,   14,
    '2015-May-01',   13,   10,
    '2015-May-02',    5,    4,
    '2015-May-03',    3,    3,
    '2015-May-04',   14,   10,
    '2015-May-05',   12,   10,
    '2015-May-06',   10,    6,
    '2015-May-07',   11,    8,
    '2015-May-08',   11,    8,
    '2015-May-09',    0,    0,
    '2015-May-10',    4,    4,
    '2015-May-11',   17,   13,
    '2015-May-12',   24,   10,
    '2015-May-13',   18,   15,
    '2015-May-14',   10,    7,
    '2015-May-15',   13,    8,
    '2015-May-16',    6,    4,
    '2015-May-17',    3,    3,
    '2015-May-18',    1,    1,
    ]

# Extract the dates from the data array
date_strings = data[0::3]

# Convert date strings into numbers
date_nums = []
for d in date_strings:
  date_nums.append(date2num(datetime.strptime(d, '%Y-%b-%d')))

# Extract number of views from data array
n_views = data[1::3]

# Extract number of unique visitors from data array
n_visitors = data[2::3]

# Initialize an array with 1, 7, 14, ...
N = len(date_strings)
week_indexes = range(0, N, 7)

# Get total views and average unique viewers for each week
week_views = []
week_visitors = []
x_axis = []
for i in range(0, len(week_indexes)-1):
  start = week_indexes[i]
  stop = week_indexes[i+1]
  week_views.append(sum(n_views[start:stop]));
  week_visitors.append(np.mean(n_visitors[start:stop]));
  x_axis.append(date_nums[week_indexes[i]])

# Get a reference to the figure
fig = plt.figure()

# 111 is equivalent to Matlab's subplot(1,1,1) command
ax1 = fig.add_subplot(111)
ax1.plot(x_axis, week_views, 'bo-')
ax1.set_ylabel('Weekly page views (blue circles)')

# Choose the number of labels to create, then use linspace to create them and convert them to ints
n_labels = 4
x_axis_ticks = np.linspace(0, len(x_axis)-1, n_labels).astype(int)

# Set tick labels and positions
ax1.set_xticks([x_axis[i] for i in x_axis_ticks])
ax1.set_xticklabels(['Week of \n' + str(num2date(x_axis[i]).date()) for i in x_axis_ticks])

# Plot the average weekly unique visitors
ax2 = ax1.twinx()
ax2.plot(x_axis, week_visitors, 'gs--')
ax2.set_ylabel('Avg. Daily Unique Visitors (green squares)')

# Add title
title_string = 'Total Pageviews: ' \
               + str(sum(n_views)) \
               + ', Avg. Daily Unique Visitors: ' \
               + '%.1f' % np.mean(n_visitors)
fig.suptitle(title_string)

# Save as PDF
plt.savefig('weekly_github_traffic.pdf')



# Make monthly plot
fig.clf()

month_intervals = ['2014-Feb-17',
                   '2014-Mar-17',
                   '2014-Apr-17',
                   '2014-May-17',
                   '2014-Jun-17',
                   '2014-Jul-17',
                   '2014-Aug-17',
                   '2014-Sep-17',
                   '2014-Oct-17',
                   '2014-Nov-17',
                   '2014-Dec-17',
                   '2015-Jan-17',
                   '2015-Feb-17',
                   '2015-Mar-17',
                   '2015-Apr-17']

# Find the indexes of each date
month_indexes = []
for date in month_intervals:
  month_indexes.append(date_strings.index(date))

# Get total views and average unique viewers for each month
month_views = [];
month_visitors = [];
x_axis = []
for i in range(0, len(month_indexes)-1):
  start = month_indexes[i]
  stop = month_indexes[i+1]
  month_views.append(sum(n_views[start:stop]));
  month_visitors.append(np.mean(n_visitors[start:stop]));
  x_axis.append(date_nums[month_indexes[i]])

# 111 is equivalent to Matlab's subplot(1,1,1) command
ax1 = fig.add_subplot(111)
ax1.plot(x_axis, month_views, 'bo-')
ax1.set_ylabel('Monthly page views (blue circles)')

# For an odd number of months, include a middle tick mark, otherwise just
# label the endpoints.
n_months = len(x_axis)
x_axis_ticks = [0, len(x_axis)-1]
if n_months % 2 != 0:
  x_axis_ticks.insert(1, n_months/2)

# Set tick labels and positions
ax1.set_xticks([x_axis[i] for i in x_axis_ticks])
ax1.set_xticklabels([num2date(x_axis[i]).strftime('%b\n%Y') for i in x_axis_ticks])

# Plot the average weekly unique visitors
ax2 = ax1.twinx()
ax2.plot(x_axis, month_visitors, 'gs--')
ax2.set_ylabel('Avg. Daily Unique Visitors (green squares)')

# Save as PDF
plt.savefig('monthly_github_traffic.pdf')

# Local Variables:
# python-indent: 2
# End:
