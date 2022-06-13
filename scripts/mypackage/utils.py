from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

## Visual, Graphs

def histbox(data, column_name):
  
    # creating a figure composed of two matplotlib.Axes objects (ax_box and ax_hist)
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True,
                                        gridspec_kw={"height_ratios": (.15, .85)})

    # assigning a graph to each ax
    sns.boxplot(data[column_name], ax=ax_box)
    sns.histplot(data=data, x=column_name, ax=ax_hist)

    # Remove x axis name for the boxplot
    ax_box.set(xlabel='')
    plt.show()

## ----------------------------------------------------------------------------------------
import re
from datetime import datetime

## Data Versions

def findVersionFromDataName(datafileName):
  regex = r"(?<=V)(.*?)(?=_)"

  matches = re.finditer(regex, datafileName, re.MULTILINE)
  for matchNum, match in enumerate(matches, start=1):
      if(matchNum == 1):
          version = match.group()

  return version.split('.')
