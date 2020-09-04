{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Lists and its default functions\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'java']\n",
      "Count of the elements in List 1\n",
      "After append ['python', 'java', 'C++']\n",
      "After extend ['python', 'java', 'C++', 'C#', 'javascript']\n",
      "After Insert ['C', 'python', 'java', 'C++', 'C#', 'javascript']\n",
      "After Remove ['C', 'python', 'java', 'C++', 'C#']\n",
      "After Pop ['C', 'python', 'java', 'C++']\n",
      "After Clear None\n"
     ]
    }
   ],
   "source": [
    "#Create and print the list\n",
    "a=['python','java']\n",
    "print(a)\n",
    "#Count\n",
    "print('Count of the elements in List',a.count(\"java\"))\n",
    "#append\n",
    "a.append('C++')\n",
    "print('After append',a)\n",
    "#extend\n",
    "a.extend(['C#','javascript'])\n",
    "print('After extend',a)\n",
    "#Insert\n",
    "a.insert(0,'C')\n",
    "print('After Insert',a)\n",
    "#Remove\n",
    "a.remove('javascript')\n",
    "print('After Remove',a)\n",
    "#Pop\n",
    "a.pop()\n",
    "print('After Pop',a) #defaultly delete the last element\n",
    "#Clear\n",
    "print('After Clear',a.clear())\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Dictionary and its default functions\n"
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
      "{1: 'Google', 2: 'Microsoft', 3: 'Amazon'}\n",
      "Microsoft\n",
      "{1: 'Google', 2: 'TATA', 3: 'Amazon'}\n",
      "{1: 'Google', 2: 'TATA', 3: 'Amazon', 4: 'Facebook'}\n",
      "Amazon\n",
      "{1: 'Google', 2: 'TATA', 4: 'Facebook'}\n",
      "{}\n"
     ]
    }
   ],
   "source": [
    "#create a dictionary and print\n",
    "D={1:'Google',2:'Microsoft',3:'Amazon'}\n",
    "print(D)\n",
    "#Get the elements in dict\n",
    "print(D.get(2))\n",
    "#change the elements in dict\n",
    "D[2]='TATA'\n",
    "print(D)\n",
    "#Add the elements in dict\n",
    "D[4]='Facebook'\n",
    "print(D)\n",
    "#Pop\n",
    "print(D.pop(3))\n",
    "print(D)\n",
    "#Delete\n",
    "D.clear()\n",
    "print(D)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# sets and default functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 'day', 7.5}\n",
      "{1, 'day', 2, 7.5}\n",
      "{1, 'day', 2}\n",
      "set()\n"
     ]
    }
   ],
   "source": [
    "#create a set\n",
    "S={1,'day',7.5}\n",
    "print(S)\n",
    "# add an element\n",
    "S.add(2)\n",
    "print(S)#\n",
    "#remove an element\n",
    "S.remove(7.5)\n",
    "print(S)\n",
    "# clear my_set\n",
    "S.clear()\n",
    "print(S)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tuples  and it default functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'joy', 3.6)\n",
      "<class 'tuple'>\n",
      "joy\n",
      "('joy', 3.6)\n",
      "(1, 'joy', 3.6, 2, 'hen', 4.7)\n"
     ]
    }
   ],
   "source": [
    "#Create a tuple\n",
    "T = (1, 'joy', 3.6)\n",
    "print(T)\n",
    "#do found the type\n",
    "print(type(T))\n",
    "# Negative indexing for accessing tuple elements\n",
    "print(T[1])\n",
    "#slicing\n",
    "print(T[1:])\n",
    "#Concatenation\n",
    "T1=(2,'hen',4.7)\n",
    "print(T+T1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# String and its methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mark jugerbeg\n",
      "rk \n",
      "jugerbe\n",
      "13\n",
      "Mark jugerbeg\n",
      "<built-in method lower of str object at 0x000001C3D5EDD9F0>\n",
      "<built-in method upper of str object at 0x000001C3D5EDD9F0>\n",
      "['Mark', 'jugerbeg']\n"
     ]
    }
   ],
   "source": [
    "#create a string\n",
    "string1='Mark jugerbeg'\n",
    "print(string1)\n",
    "#Slicing\n",
    "print(string1[2:5])\n",
    "#Negative Indexing\n",
    "print(string1[-8:-1])\n",
    "#string length\n",
    "print(len(string1))\n",
    "#remove white spaces\n",
    "print(string1.strip())\n",
    "#lower\n",
    "print(string1.lower)\n",
    "#upper\n",
    "print(string1.upper)\n",
    "#split\n",
    "print(string1.split())\n"
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
