import matplotlib.pyplot as plt
import numpy as np
import math

xmlInput = open('plotMe.xml','r')
xmlLines = xmlInput.readlines()
data = {'Arc':[],'Line':[]}

arcData = {}
lineData = {}

def verifyTags(line):
    if (line.find('Arc') != -1):
        return 'Arc'
    elif (line.find('Line') != -1):
        return 'Line'
    else :
        return 'unknown'

def extractValue(line):
    start_pos = line.find('>')
    end_pos = line.find('<',start_pos)
    return line[start_pos + 1:end_pos]
    
def verifyArcTags(line):       
    if(line.find('Color') != -1):
        return 'color',extractValue(line)
    elif(line.find('XCenter') != -1):
        return 'x_center', float(extractValue(line))
    elif(line.find('YCenter') != -1):
        return 'y_center', float(extractValue(line))
    elif(line.find('ArcStart') != -1):
        return 'arc_start', int(extractValue(line))
    elif(line.find('ArcExtend') != -1):
        return 'arc_extend', int(extractValue(line))
    elif(line.find('Radius') != -1):
        return 'radius', float(extractValue(line))
    else:
        return '',''

def verifyLineTags(line):
    if(line.find('Color') != -1):
        return 'color',extractValue(line)
    elif(line.find('XStart') != -1):
        return 'x_start', float(extractValue(line))
    elif(line.find('YStart') != -1):
        return 'y_start', float(extractValue(line))
    elif(line.find('XEnd') != -1):
        return 'x_end', float(extractValue(line))
    elif(line.find('YEnd') != -1):
        return 'y_end', float(extractValue(line))
    else:
        return '',''
    
def plotArc(arcData):
    print('plotting Arc: ',arcData)
    center = (arcData['x_center'],arcData['y_center'])
    radius = arcData['radius']
    start_arc = arcData['arc_start']/360*2*np.pi
    end_arc = (arcData['arc_start'] + arcData['arc_extend'])/360*2*np.pi
    theta = np.arange(start_arc,end_arc,0.01)
    x_coors = center[0] + radius*np.cos(theta)
    y_coors = center[1] + radius*np.sin(theta)
    arcData.setdefault('color','black')
    plt.plot(x_coors,y_coors,color=arcData['color'])

def generateCoors(x_start,x_end,y_start,y_end):
    coors = {'xCoors': [x_start],'yCoors': [y_start]}
    
    x_distance = x_end - x_start
    y_distance = y_end - y_start
    length = math.sqrt(x_distance * x_distance  + y_distance * y_distance)
    
    for r in range(1,int(length)):
        ratio = r/length
        coors['xCoors'].append(x_start + x_distance * ratio)
        coors['yCoors'].append(y_start + y_distance * ratio)
    return coors
    
def plotLine(lineData):
    print('plotting Line: ',lineData)
    coors = generateCoors(lineData['x_start'],lineData['x_end'],lineData['y_start'],lineData['y_end'])
    
    lineData.setdefault('color','black')
    plt.plot(coors['xCoors'],coors['yCoors'],color=lineData['color'])
    
def plotArcData(index,xmlLines,arcData):
    index = index + 1
    while (xmlLines[index].find('</Arc>') == -1):
        field,value = verifyArcTags(xmlLines[index])
        arcData[field] = value
        index = index + 1
    plotArc(arcData)
    arcData.clear()
    
    return index
    

def plotLineData(index,xmlLines,lineData):
    index = index + 1
    while (xmlLines[index].find('</Line>') == -1):
        field,value = verifyLineTags(xmlLines[index])
        lineData[field] = value
        index = index + 1
    plotLine(lineData)
    lineData.clear()
    
    return index
    
line_index = 0
while line_index < len(xmlLines):
    line = xmlLines[line_index]
    type = verifyTags(line)
    
    if (type == 'Arc'):
        line_index = plotArcData(line_index,xmlLines,arcData)
    elif (type == 'Line'):
        line_index = plotLineData(line_index,xmlLines,lineData)

    line_index = line_index + 1
plt.savefig("result.png",dpi=300,format="png")