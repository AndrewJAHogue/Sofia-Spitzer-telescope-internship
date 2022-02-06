import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import Galactic



def GetNthColumn(file, xvalue, **kwargs):
    xmin = kwargs.get('xmin', None)
    xmax = kwargs.get('xmax', None)

    ymin = kwargs.get('ymin', None)
    ymax = kwargs.get('ymax', None)

    fake = kwargs.get('fake', True)

    yvalues = np.array([])
    yvalues = file[:,xvalue]
    xdata = np.array(range(len(yvalues)))

    if min is not None and max is not None:
        yvalues = yvalues[xmin:xmax]
        xdata = xdata[xmin:xmax]
    # fake x data
    # if fake:
    return np.array([xdata, yvalues])
    # else:
        # return np.array(yvalues)

def GetNthRow(file, yvalue, **kwargs):
    # xvalues = np.array([])
    # xvalues = file[yvalue]
    # xvalues = xvalues[xvalues > min]
    # # fake data, just indeces, basically; example had 'r' but I don't know what that is in this context
    # if fake:
    #     ydata = np.array(range(len(xvalues)))
    #     return np.array([ydata, xvalues])
    # else:
    #     return np.array(xvalues)

    #
    xmin = kwargs.get('xmin', None)
    xmax = kwargs.get('xmax', None)

    ymin = kwargs.get('ymin', None)
    ymax = kwargs.get('ymax', None)

    fake = kwargs.get('fake', True)

    xvalues = np.array([])
    xvalues = file[yvalue]
    ydata = np.array(range(len(xvalues)))

    if min is not None and max is not None:
        xvalues = xvalues[xmin:xmax]
        ydata = ydata[xmin:xmax]
    # fake x data
    # if fake:
    return np.array([ydata, xvalues])
    # else:
        # return np.array(yvalues)



def SingleLinePlot(filepath, xvalue, yvalue, columnmin=0.0, rowmin=0.0):
    data = fits.open(filepath)[0].data

    column = GetNthColumn(data, xvalue)
    columnLineplot = plt.subplot(1,2,1)
    plt.title(f'Column-Pixel Saturation at X={xvalue}')
    plt.xlabel('Y Index')
    plt.ylabel('Pixel Value')
    plt.plot(column[0],column[1])
    # print(column[1][column[1] > 0.4])

    row = GetNthRow(data, yvalue)
    rowLineplot = plt.subplot(1,2,2)
    plt.title(f'Row-Pixel Saturation at Y={yvalue}')
    plt.xlabel('X Index')
    plt.ylabel('Pixel Value')
    plt.plot(row[0],row[1])
    plt.suptitle(filepath)

    plt.show()

def MultiLinePlot(xvalue, yvalue, fileset=[], columnlimits=[None,None,None,None], rowlimits=[None,None,None,None], **kwargs):
    # colxmin = kwargs.get('colxmin', None) ## limit domain of column plot
    colxmin = columnlimits[0]
    # colxmax = kwargs.get('colxmax', None)
    colxmax = columnlimits[1]
    # colymin = kwargs.get('colymin', None) ## limit range of column plot
    colymin = columnlimits[2]
    # colymax = kwargs.get('colymax', None)
    colymax = columnlimits[3]
    # rowxmin = kwargs.get('rowxmin', None) ## limit domain of row plot
    rowxmin = rowlimits[0]
    # rowxmax = kwargs.get('rowxmax', None)
    rowxmax = rowlimits[1]
    # rowymin = kwargs.get('rowymin', None) ## limit range of row plot
    rowymin = rowlimits[2]
    # rowymax = kwargs.get('rowymax', None)
    rowymax = rowlimits[3]

    x2 = keywargs.get('x2', None)
    y2 = keywargs.get('y2', None)

    legend = kwargs.get('legend', False) ## show legend or not
    
    files = fileset.copy()
    datasets = np.array([])
    for arg in kwargs:
        if 'file' in str(arg):
            files = np.append(files, kwargs.get(arg, None))
    # grid = len(files)
    # grid /= 4
    grid = 1
    print(f'grid is => {grid}')

    from math import ceil, floor

    for plot_index,file in enumerate(files):
        plot_index += 1
        if plot_index > 2:
            plot_index = 2
        print(f'plot_index is => {plot_index}')
        if isinstance(file, str):
            data = fits.open(file)[0].data
        file = file[file.find('fits/') + 5:] #test[test.find('fits/') + 5:]
        print(file)

        column = GetNthColumn(data, xvalue)
        ax1 = plt.subplot(grid,2,1)
        plt.title(f'Column-Pixel Saturation at X={xvalue}')
        plt.xlabel('Y Index')
        plt.ylabel('Pixel Value')
        ax1.margins(0)
        if colxmin != None:
            plt.xlim(left=colxmin)
        if colxmax != None:
            plt.xlim(right=colxmax)
        if colymin != None:
            plt.ylim(bottom=colymin)
        if colymax != None:
            plt.ylim(top=colymax)

        plt.plot(column[0], column[1], label=file)
        if legend:
            plt.legend()

        row = GetNthRow(data, yvalue)
        plt.subplot(grid,2,2)
        plt.title(f'Row-Pixel Saturation at Y={yvalue}')
        plt.xlabel('X Index')
        if rowxmin != None:
            plt.xlim(left=rowxmin)
        if rowxmax != None:
            plt.xlim(right=rowxmax)
        if rowymin != None:
            plt.ylim(bottom=rowymin)
        if rowymax != None:
            plt.ylim(top=rowymax)
        plt.plot(row[0],row[1], label=file) 
        if legend:
            plt.legend()
    plt.show()


# def main(data, xvalue, yvalue, colxmin, colxmax, rowmin, rowmax):
