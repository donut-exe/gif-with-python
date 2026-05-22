import imageio.v3 as iio
filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
catty = [ ]

for i in filenames:
  catty.append(iio.imread(i))

iio.imwrite('cat.gif', catty, duration = 250, loop = 6)