__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from tools.algorithm.QuickHull import QuickHull

cloud = list()
cloud.append((1, 0, 0))
cloud.append((-1, 0, 0))
cloud.append((0, 1, 0))
cloud.append((0, -1, 0))
cloud.append((0, 0, 1))
cloud.append((0, 0, -1))

quick_hull = QuickHull(cloud)
quick_hull.run()
faces = quick_hull.get_faces()
for ff in faces:
    print ff

def figure():
    a = 0.1
    b = 0.2
    c = 0.3
    for f in faces:
        glBegin(OpenGL.GL.GL_TRIANGLES)
        glColor3f(a, b, c)
        glVertex3fv(f.a())
        glVertex3fv(f.b())
        glVertex3fv(f.c())
        glEnd()
        a += 0.1
        b += 0.1
        c += 0.1

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
        figure()
        pygame.display.flip()
        pygame.time.wait(10)


main()
