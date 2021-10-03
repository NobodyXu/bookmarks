 - [How to save the plot to image](https://stackoverflow.com/a/29931148/8375400)
   
   ```
   import matplotlib.pyplot as plt
   fig, ax = plt.subplots(nrows=1, ncols=1)
   ax.plot([0,1,2], [10,20,3])
   fig.savefig('path/to/save/image/to.png')   # save the figure to file
   plt.close(fig)
   ```
