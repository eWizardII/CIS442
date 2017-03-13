{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pymc\n",
    "import numpy as np\n",
    "\n",
    "# Some data\n",
    "n = 5*np.ones(4,dtype=int)\n",
    "x = np.array([-.86,-.3,-.05,.73])\n",
    "\n",
    "# Priors on unknown parameters\n",
    "alpha = pymc.Normal('alpha',mu=0,tau=.01)\n",
    "beta = pymc.Normal('beta',mu=0,tau=.01)\n",
    "\n",
    "# Arbitrary deterministic function of parameters\n",
    "@pymc.deterministic\n",
    "def theta(a=alpha, b=beta):\n",
    "    \"\"\"theta = logit^{-1}(a+b)\"\"\"\n",
    "    return pymc.invlogit(a+b*x)\n",
    "\n",
    "# Binomial likelihood for data\n",
    "d = pymc.Binomial('d', n=n, p=theta, value=np.array([0.,1.,3.,5.]),\\\n",
    "                  observed=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
