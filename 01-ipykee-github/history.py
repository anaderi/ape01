{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "ipykee.settings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.settings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.settings.Settings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.settings.yaml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.Session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.settings()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "print ipykee.config"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
   "execution_count": 9,
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
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 0
}
