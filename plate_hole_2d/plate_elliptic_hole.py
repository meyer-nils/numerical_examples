import torch
import numpy as np
from scipy.stats import qmc
import matplotlib.pyplot as plt
import random
from math import pi, ceil

class Plate:
    def __init__(self, Re_x, SuAr, L, N):
        self.Re_x = Re_x
        self.SuAr = SuAr
        self.Re_y = SuAr/(pi*Re_x) 
        self.L = L
        self.N = N
        self.NN = ceil(N * (L-Re_x)/L)
        self.collopoints = None

    def create_ellipse(self, Re_x, SuAr, max_length):
        while True:
            Re_y=  SuAr/(pi*Re_x)   #radius on the y-axis
            if (Re_x>max_length or Re_x<0):
                print("x_radius was not in range between 0 and max_length")
                Re_x = random.random()* max_length
                continue
            if (Re_y>max_length or Re_y<0):
                print("y_radius was not in range between 0 and max_length")
                continue
            else: break
        print("radius x-axis: ",Re_x)
        print("radius y-axis: ",Re_y)
        return Re_x,Re_y
    
    def plot_ellipse(self, Re_x, Re_y):
        t = np.linspace(0, 2*pi, 80)
        plt.plot( Re_x*np.cos(t) , Re_y*np.sin(t) )
        plt.axis('square')
        plt.grid(color='lightgray',linestyle='--')
        plt.show()

    def plot_quarter_elli(self, Re_x, Re_y):
        t = np.linspace(0, 0.5*pi, 80)
        plt.plot( Re_x*np.cos(t) , Re_y*np.sin(t) )
        plt.axis('square')
        plt.grid(color='lightgray',linestyle='--')
        plt.show()

    def generate_dataset(self, Re_x, Re_y, L, N):
        # Create collocation points
        points = L * qmc.LatinHypercube(d=2).random(N**2)

        #excludes points that are inside the elliptical hole
        points = points[(((points[:,0] ** 2)/(Re_x**2)) + ((points[:,1] ** 2)/(Re_y**2))) > 1]
        x_collocation = torch.tensor(points[:,0], requires_grad=True).float()
        y_collocation = torch.tensor(points[:,1], requires_grad=True).float()
        collo_points = [x_collocation, y_collocation]
        # Boundaries
        x_top = torch.linspace(0, L, N, requires_grad=True)
        y_top = L * torch.ones((N, 1), requires_grad=True) 

        x_right = L * torch.ones((N, 1))
        y_right = torch.linspace(0, L, N)

        x_left = torch.zeros(ceil(N*(1-Re_y)), 1)
        y_left = torch.linspace(Re_y, L, ceil(N*(1-Re_y)))

        x_bottom = torch.linspace(Re_x, L, ceil(N*(1-Re_x)))
        y_bottom = L * torch.zeros(ceil(N*(1-Re_x)), 1)

        phi = np.linspace(0, 0.5 * np.pi, int(N * 0.5 * np.pi * Re_x / L))
        x_hole = torch.tensor(Re_x * np.cos(phi), requires_grad=True).float()
        y_hole = torch.tensor(Re_y * np.sin(phi), requires_grad=True).float()

        n_hole = torch.tensor(np.stack([-np.cos(phi), -np.sin(phi)]).T).float()
        boundary_points= [x_top, y_top, x_right, y_right, x_left, y_left, x_bottom, y_bottom, x_hole, y_hole, n_hole]
        return [collo_points, boundary_points]
    
    def generate_dataset_test(self, Re_x, Re_y, L, N):
        # Create collocation points
        points = L * qmc.LatinHypercube(d=2).random(N**2)

        #excludes points that are inside the elliptical hole
        points = points[(((points[:,0] ** 2)/(Re_x**2)) + ((points[:,1] ** 2)/(Re_y**2))) > 1]
        x_collocation = torch.tensor(points[:,0], requires_grad=True).float()
        y_collocation = torch.tensor(points[:,1], requires_grad=True).float()
        collo_points = [x_collocation, y_collocation]
        # Boundaries
        x_top = torch.linspace(0, L, N, requires_grad=True)
        y_top = L * torch.ones((N, 1), requires_grad=True)

        x_right = L * torch.ones((N, 1))
        y_right = torch.linspace(0, L, N)

        x_left = torch.zeros(ceil(N*(1-Re_y)), 1)
        y_left = torch.linspace(Re_y, L, ceil(N*(1-Re_y)))

        x_bottom = torch.linspace(Re_x, L, ceil(N*(1-Re_x)))
        y_bottom = L * torch.zeros(ceil(N*(1-Re_x)), 1)

        phi = np.linspace(0, 0.5 * np.pi, int(N * 0.5 * np.pi * Re_x / L))
        x_hole = torch.tensor(Re_x * np.cos(phi), requires_grad=True).float()
        y_hole = torch.tensor(Re_y * np.sin(phi), requires_grad=True).float()

        n_hole = torch.tensor(np.stack([-np.cos(phi), -np.sin(phi)]).T).float()
        boundary_points= [x_top, y_top, x_right, y_right, x_left, y_left, x_bottom, y_bottom, x_hole, y_hole, n_hole]
        return collo_points, boundary_points

    def plot_plate_with_hole(self, collo_points, boundary_points):
        # Visualize geometry (Dirichlet blue, Neumann red)
        plt.plot(collo_points[0].detach(), collo_points[1].detach(), ".k")
        #top 
        plt.plot(boundary_points[0].detach(), boundary_points[1].detach(), ".r")
        #right
        plt.plot(boundary_points[2], boundary_points[3], ".b")
        #bottom
        plt.plot(boundary_points[6], boundary_points[7], ".g")
        #left
        plt.plot(boundary_points[4], boundary_points[5], ".b")
        #hole
        plt.plot(boundary_points[8].detach(), boundary_points[9].detach(), ".r")
        plt.axis("equal")
        plt.show()