{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%javascript\n",
    "IPython.load_extensions('ipykee');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "ipykee.create_project_if_not_exist(\"ape01\", repository=\"git@github.com:anaderi/ape01.git\", internal_path=\".\")\n",
    "session = ipykee.Session(notebook=\"01-ipykee-github\", project_name=\"ape01\", docker_image=\"anaderi/rep-develop:latest\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "%pylab inline\n",
    "import matplotlib.pyplot as plt  # Again, in pylab mode this import happens automatically\n",
    "import numpy as np\n",
    "x = np.linspace(0, 10, 1000)\n",
    "fig1 = plt.figure()\n",
    "ax1 = fig1.add_subplot(1, 1, 1)\n",
    "ax1.plot(x, np.sin(x))\n",
    "ax1.set_title('sine')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "session.add(x, \"x\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "session.commit(\"Plot sin x\")"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 0
}
