#! /usr/bin/env python
# coding: utf-8

""" Routines common to ppfig, pptex, ppfigdim, pprldistr."""

from __future__ import absolute_import

import scipy
import scipy.io
from pdb import set_trace

__version__ = "$Revision$"
# $URL$
# $Date$

#TODO: at this point only split is used elsewhere.

#class Error(Exception):
    #""" Base class for errors. """
    ##TODO: what the?
    #pass


#class MissingValueError(Error):
    #""" Error if a mandatory value is not found within a file.
        #Returns a message with the missing value and the respective
        #file."""

    #def __init__(self,value, filename):
        #self.value = value
        #self.filename = filename

    #def __str__(self):
        #message = 'The value %s was not found in file %s!' % \
                  #(self.value, self.filename)
        #return repr(message)


def split(dataFiles):
    """Split the data files into arrays corresponding to the data sets."""
    #TODO: optimize by splitting using %
    dataSets = []
    for fil in dataFiles:
        try:
            content = scipy.io.read_array(fil,comment='%')
        except IOError:
            print 'Could not find %s.' % fil
            continue
        dataSetFinalIndex = scipy.where(scipy.diff(content[:,0])<=0)[0]
        #splitting is done by comparing the number of function evaluations
        #which should be monotonous.
        if len(dataSetFinalIndex)> 0:
            dataSetFinalIndex += 1
            dataSetFinalIndex = scipy.append(scipy.append(0,dataSetFinalIndex),
                                             None)
            #dataSetFinalIndex = scipy.insert(dataSetFinalIndex,0,-2)
            for i in range(len(dataSetFinalIndex)-1):
                dataSet = DataSet(content[dataSetFinalIndex[i]:
                                          dataSetFinalIndex[i+1],:])
                dataSets.append(dataSet)
        else:
            dataSet = DataSet(content)
            dataSets.append(dataSet)

    return dataSets


def alignData(dataSets, align):
    """Returns data aligned according to align."""
    current = CurrentState('align')

    data = []

    # read status of dataSets.

    while any(current.isReading):
        for i in range(len(dataSets)):
            curDataSet = dataSets[i]
            if current.isReading[i]:
                evals[i] = curDataSet.set[curDataSet.currentPos, idxEvals]
                f[i] = curDataSet.set[curDataSet.currentPos, idxF]
                while (curDataSet.currentPos < len(curDataSet.set) - 1 and
                       not current.isValid(slice(i,i+1))): # minimization
                    curDataSet.currentPos += 1
                    evals[i] = curDataSet.set[curDataSet.currentPos,
                                              idxEvals]
                    f[i] = curDataSet.set[curDataSet.currentPos, idxF]
                if not (curDataSet.currentPos < len(curDataSet.set) - 1):
                    current.isReading[i] = False

        set_trace()
        data.append(current.getVector())

        if current.any(isReading):
            #Gets the closest fitness which can be written as 10**(i/5)
            #from above
            if scipy.isinf(currentF):
                idxCurrentF = int(scipy.ceil(scipy.log10(max(f))*nbPtsF))
                currentF = scipy.power(10, float(idxCurrentF) / nbPtsF)
            tmp = [currentF]
            tmp.extend(evals)
            tmp.extend(f)
            hData.append(tmp)
            while all(scipy.power(10, float(idxCurrentF) / nbPtsF) > f):
                idxCurrentF -= 1
            currentF = scipy.power(10, float(idxCurrentF) / nbPtsF)

    tmp = [currentF]
    tmp.extend(evals)
    tmp.extend(f)
    hData.append(tmp)
    set_trace()
    self.hData = scipy.vstack(hData)
    return hData


class CurrentState:
    def __init__(self, align, size):
        self.evals = size * [0] # updated list of function evaluations
        self.f = size * [0] # updated list of function values.
        self.isReading = size * [True]
        if align == 'horizontal':
            self =  HCurrentState()

        elif align == 'vertical':
            self = VCurrentState()
        else:
            print 'Error'

        self.curIdF = scipy.inf #minimization
        self.curIdEv = -scipy.inf

    def getF(self):
        return scipy.power(10, self.idxVal/nbPtsF)

    def getEv(self):
        return int(scipy.floor(scipy.power(10, idxVal/nbPtsEvals)))

    def getVector(self):
        res = self.getVal()


class HCurrentState(CurrentState):

    def isValid(self, s): #= slice(len(self.f))):
        """Tests if a slice of self.f is lesser than the current value."""
        res = []
        tmp = self.getVal()
        for i in self.f[s]:
            res.append(i <= tmp)

        return all(res)

    def getVal(self):
        return getF(self)

    def getCurVal(self):
        self.idxF = scipy.ceil(scipy.log10(max(self.f)) * nbPtsF)
        return getF


class VCurrentState(CurrentState):

    def isValid(self, s ):#= slice(len(self.f))):
        """Tests if a slice of self.f is greater than the current value."""
        res = []
        tmp = self.getVal()
        for i in self.f[s]:
            res.append(i >= tmp)

        return all(res)

    def getVal(self):
        return getEv(self)


class DataSet:
    def __init__ (self, set):
        self.currentPos = 0
        self.currentPos2 = 0
        self.set = set
        self.userDefMaxEvals = set[-1, 0]
