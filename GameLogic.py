#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
def Start():
    mat=[[0 for i in range(4)]for j in range(4)]
    return mat

def add2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    
def currState(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==2048):
                return "WON"
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                return "Continue "
    
    for i in range(3):
        for j in range(3):
            if(mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]):
                return "Continue "
    
    for i in range(3):
        if(mat[i][3]==mat[i+1][3]):
            return "Continue "
        
    for j in range(3):
        if(mat[3][j]==mat[3][j+1]):
            return "Continue "
    return "LOST"

def reverse(grid):
    for i in range(4):
        for j in range(2):
            grid[i][j],grid[i][4-j-1]=grid[i][4-j-1],grid[i][j]
    return grid

def transpose(grid):
    for i in range(4):
        for j in range(4):
            if(j>i):
            	grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
    return grid

def compress(grid):
    changed=False
    for i in range(4):
        for j in range(4):
            if(grid[i][j]==0):
                k=j
                while(k!=4 and grid[i][k]==0):
                    k+=1
                if(k!=4):
                    grid[i][j]=grid[i][k]
                    grid[i][k]=0
                    changed=True
    return grid,changed

def merge(grid):
    changed=False
    for i in range(4):
        for j in range(3):
            if(grid[i][j]==grid[i][j+1] and grid[i][j]!=0):
                grid[i][j]=grid[i][j]*2
                grid[i][j+1]=0
                changed=True
    return grid,changed

def move_up(grid):
    #Implement This Function
    changed=False
    new_grid=transpose(grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    if(changed1 or changed2 or changed3):
        changed=True
    new_grid=transpose(new_grid)
    return new_grid,changed
    
def move_down(grid):
    #Implement This Function
    changed=False
    new_grid=transpose(grid)
    new_grid=reverse(new_grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    if(changed1 or changed2 or changed3):
        changed=True
    new_grid=reverse(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,changed

def move_right(grid):
    #Implement This Function
    changed=False
    new_grid=reverse(grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    if(changed1 or changed2 or changed3):
        changed=True
    new_grid=reverse(new_grid)
    return new_grid,changed

def move_left(grid):
    #Implement This Function
    changed=False
    new_grid,changed1=compress(grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    if(changed1 or changed2 or changed3):
        changed=True
    return new_grid,changed

