{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Guide the Pilots\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the altitude:1000\n",
      "Safe to Land\n"
     ]
    }
   ],
   "source": [
    "Input=int(input(\"Enter the altitude:\"))\n",
    "if(Input<=1000):\n",
    "    print(\"Safe to Land\")\n",
    "elif(Input>1000)&(Input<5000):\n",
    "    print(\"Bring down to 1000\")\n",
    "else:\n",
    "    print(\"Turn around\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Print the prime numbers between 1-200"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime numbers between 1 and 200 are:\n",
      "2\n",
      "3\n",
      "5\n",
      "7\n",
      "11\n",
      "13\n",
      "17\n",
      "19\n",
      "23\n",
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n",
      "53\n",
      "59\n",
      "61\n",
      "67\n",
      "71\n",
      "73\n",
      "79\n",
      "83\n",
      "89\n",
      "97\n",
      "101\n",
      "103\n",
      "107\n",
      "109\n",
      "113\n",
      "127\n",
      "131\n",
      "137\n",
      "139\n",
      "149\n",
      "151\n",
      "157\n",
      "163\n",
      "167\n",
      "173\n",
      "179\n",
      "181\n",
      "191\n",
      "193\n",
      "197\n",
      "199\n"
     ]
    }
   ],
   "source": [
    "Start = 1\n",
    "End = 200\n",
    "\n",
    "print(\"Prime numbers between\",Start, \"and\",End,\"are:\")\n",
    "\n",
    "for num in range(Start,End + 1):\n",
    "   if(num > 1):\n",
    "       for i in range(2, num):\n",
    "           if(num % i) == 0:\n",
    "               break\n",
    "       else:\n",
    "           print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
