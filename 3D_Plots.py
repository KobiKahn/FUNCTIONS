
def scatter_3d(x, y, z, n_range):
    for n in range(n_range):
        z.append(.1 * n * math.pi)
        x.append(math.cos(z[n]))
        y.append(math.sin(z[n]))

    fig = plt.figure(1)  # open a figure for the plot
    ax = fig.add_subplot(111, projection='3d')  # define the axes to 3 dimensional
    ax.plot(x, y, z, '-r*')  # plot the data
    ax.set_xlabel('cos(z))')  # label the x-axis
    ax.set_ylabel('sin(z))')  # label the y-axis
    ax.set_zlabel('z')  # label the z-axis
    ax.set_title('A Helix')
    plt.show()


def surface_3d(x, y, z):
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z,linewidth=0, antialiased=True,color='aquamarine')
    plt.show()


def wire_3d(x, y, z, title):
    fig = plt.figure(3)
    ax = fig.subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, rstride=10, cstride=10)
    ax.set_xlabel('X Axis')  # label the x-axis
    ax.set_ylabel('Y Axis')  # label the y-axis
    ax.set_zlabel('Z Axis')  # label the z-axis
    ax.set_title(title)
    plt.show()