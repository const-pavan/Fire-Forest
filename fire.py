import numpy as np
from matplotlib import animation
from matplotlib import colors
import matplotlib.pyplot as plt

neighbourhood = ((-1,0), (0,-1), (0, 1), (1,0))
EMPTY, TREE, FIRE = 0, 1, 2
p, q = 0.65,0.5
probImmune=0.1
c_list = ['#D3D3D3', (0,0.6,0), (0.5,0,0), 'orange']
cmap = colors.ListedColormap(c_list)
b = [0,1,2,3]
norm = colors.BoundaryNorm(b, cmap.N)

def animate(i):
 
        im.set_data(animate.X,)
        animate.X = iterate(animate.X,animate.I)
    
def iterate(X,I):
        i=I
        X1 = np.zeros((ny, nx))
        for ix in range(0,nx):
            for iy in range(0,ny):
                if X[iy,ix] == EMPTY :
                    X1[iy,ix] = EMPTY
                if X[iy,ix] == TREE:
                    X1[iy,ix] = TREE
                    for dx,dy in neighbourhood:
                        if X[(iy+dy)%ny,(ix+dx)%nx] == FIRE and np.random.random() >= i:
                            X1[iy,ix] = FIRE
                            break

                    # case 1: 2 days burn    
                        # else:
                        #     if np.random.random() <= f:
                        #         X1[iy,ix] = FIRE
                    
                    
                    #case 2: depend on neighbourhood  
                    # for dx,dy in neighbourhood:
                    #     if X[(iy+dy)%ny,(ix+dx)%nx] == FIRE: 
                    #         sum+=1 
                    # if(sum*k>np.random.random()):
                    #     X1[iy,ix] = FIRE 
                    # 
                    

                    #case 3,4: wind speed slow->ws=1.2 fast->ws=1.8
                    # sum=0
                    # ws = 1.2
                    # for dx,dy in neighbourhood:
                        
                    #     if X[(iy+dy)%ny,(ix+dx)%nx] == FIRE:
                    #         if (dx, dy) == neighbourhood[0]: 
                    #             sum += ws
                    #         elif (dx, dy) == neighbourhood[3]:
                    #             sum += (2 - ws)
                    #         else:
                    #             sum += 1
                    # if(sum*k>np.random.random()):
                    #     X1[iy,ix] = FIRE     
                    
                    

                        
                    # for dx,dy in neighbourhood:
                    #     if X[(iy+dy)%ny,(ix+dx)%nx] == FIRE and np.random.random() >= i:
                    #         X1[iy,ix] = FIRE
                    #         break
                else:
                    X1[iy,ix] = EMPTY 
                
                
                # if X[iy,ix] == TREE and np.random.random() <= light and np.random.random() >= i:
                #     X1[iy,ix] = FIRE
        return X1
burningp=0.001
def definegrid(X):# Initialize the forest grid.
    X1 = np.zeros((ny, nx))
    for ix in range(0,nx):
        for iy in range(0,ny):

            if X[iy,ix] == EMPTY and np.random.random() <= 0.8:
                X1[iy,ix] = TREE
                # if np.random.random() <= burningp:
                #     X1[iy,ix] = FIRE
    X1[50,50]=FIRE           
    return X1
nx, ny = 100, 100

# i=[0.1,0.2,0.3,0.4,0.5,0.9,0.9,0.9,0.9] for monte carlo
# ans=[]
# for ii in i:
#     count=0
#     for j in (1,100):
#         plt.close()
#         X  = np.zeros((ny, nx))
#         X=definegrid(X)

#         fig = plt.figure(figsize=(25/3, 6.25))
#         ax = fig.add_subplot(111)
#         ax.set_axis_off()
#         im = ax.imshow(X, cmap=cmap, norm=norm)

#         I=0.5
#         animate.X = X
#         animate.I = ii
#         interval = 100
#         anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)

#         #plt.show()
#         for ix in range(0,nx):
#                     for iy in range(0,ny):
#                         if animate.X[iy,ix] == TREE: 
#                             count+=1; 
#         #print(count)
#         plt.close()
#     ans.append(count)
# plt.plot(i,ans,'r-o')
# plt.show()

plt.close()
X  = np.zeros((ny, nx))
X=definegrid(X)

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)

I=0.1
animate.X = X
animate.I = I
interval = 200
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
fig.suptitle('Fire in Forest ', fontsize=14)
anim.save("forest_fire1.mp4")
anim.save("1 Fire in Forest .gif", writer='imagemagick',fps=60)
plt.show()
plt.close()
