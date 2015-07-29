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