# -*- coding: utf-8 -*-


# <codecell>

%%javascript
IPython.load_extensions('ipykee');

# <codecell>

import ipykee
ipykee.create_project_if_not_exist("ape01", repository="git@github.com:anaderi/ape01.git", internal_path=".")
session = ipykee.Session(notebook="01-ipykee-github", project_name="ape01", docker_image="anaderi/rep-develop:latest")

# <codecell>

%pylab inline
import matplotlib.pyplot as plt  # Again, in pylab mode this import happens automatically
import numpy as np
x = np.linspace(0, 10, 1000)
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(x, np.sin(x))
ax1.set_title('sine')

# <codecell>

session.add(x, "x")

# <codecell>

session.commit("Plot sin x")

# <codecell>

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.plot(x, np.cos(x))
ax2.set_title('cosine')